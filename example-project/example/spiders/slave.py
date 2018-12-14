import os
import re
import hashlib
import json
import datetime
import time

from example import settings
from scrapy import Request, FormRequest
from scrapy_redis.spiders import RedisSpider

from example.myhandlers import *
from example.myitems import *


class HianaSpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'haina'
    redis_key = 'haina:start_urls'
    allowed_domains = ['mohurd.gov.cn']

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(HianaSpider, self).__init__(*args, **kwargs)

    # 生成MD5
    def genearteMD5(self, str, code):
        hl = hashlib.md5()
        # hl.update(str)
        hl.update(str.encode(encoding = code))
        return hl.hexdigest()

    def parse(self, response):
        self.logger.info("parse start for url: " + response.url)
        start = datetime.datetime.now()

        found_rule = False
        for rule in settings.rules:
            pattern = re.compile(rule['re'])
            ret = re.search(pattern, response.url)
            # print(rule['re'], response.url, ret)
            if (ret):
                found_rule = True
                # print(rule['func'])
                break
        if (found_rule):
            changed = True#页面内容是否有变化
            if (rule['save_page']):
                #先直接把内容原样保存成文件，按MD5校验，如果已经存在则表示对应URL内容无变化
                self.logger.info("start save page for url: " + response.url)

                main_url = response.url.split('://')
                # print(main_url)
                main_url = main_url[1]
                main_url = main_url.split('?')
                content = ''
                get_params = ''
                post_params = ''
                if (len(main_url) > 1):
                    get_params = main_url[1]
                    content += '<div id="get_params">get_params:' + get_params + "</div>\n"
                if ('post_params' in response.meta):
                    post_params = json.dumps(response.meta['post_params'])
                    content += '<div id="post_params">post_params:' + post_params + "</div>\n"
                main_url = main_url[0]
                # print(main_url)
                #对参数MD5增加一级目录
                params_md5 = self.genearteMD5(get_params + post_params, response.encoding)
                # main_path = 'd:/crawled_files/' + main_url.replace('.', '_') + '/' + params_md5 + '/'
                main_path = settings.SNAP_SAVEPATH + main_url.replace('.', '_') + '/' + params_md5 + '/'
                # main_path = 'd:/crawled_files/'
                # print(main_path)
                content += response.xpath(rule['main_area']).extract_first()
                # content = response.body.decode(response.encoding)
                md5 = self.genearteMD5(content, response.encoding)
                real_file = main_path + md5 + '.html'
                if (os.path.exists(real_file)):
                    print(real_file + ' is exists!!!')
                    self.logger.warning(real_file + ' is exists!!!')
                    changed = False
                else:
                    if (not os.path.exists(main_path)):
                        os.makedirs(main_path)
                    else:
                        #检查同一个页面的备份是否超过阈值，超过就删除最老的
                        list = os.listdir(main_path) #列出文件夹下所有的目录与文件
                        if (len(list) >= 5):
                            oldest_time = '2099-12-31 23:59:59'
                            oldest_file = ''
                            for i in range(0, len(list)):
                                file_name = os.path.join(main_path, list[i])
                                create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(file_name)))
                                if (create_time < oldest_time):
                                    oldest_time = create_time
                                    oldest_file = file_name
                            os.remove(oldest_file)
                    #保存最新一个备份
                    with open(main_path + md5 + '.html', 'w', encoding = response.encoding) as f:
                        f.write(content)
                self.logger.info("page saved for url: " + response.url)
            changed = True#不管是否更新，强制进入处理页面流程
            if (changed):
                #按配置做解析动作
                self.logger.info("start handle data for url: " + response.url)
                data = eval(rule['func'] + '.' + rule['func'] + '(response)')
                # print(data)
                self.logger.info("handled data for url: " + response.url)
                self.logger.info("return data: " + str(data))
                self.logger.info("start yield requests: " + response.url)
                if ('requests' in data):
                    for url in data['requests']:
                        yield Request(
                            url = url,
                            dont_filter = True
                        )
                # print('meta = ', response.meta)
                self.logger.info("end yield requests: " + response.url)
                self.logger.info("start yield form requests: " + response.url)
                if ('form_requests' in data):
                    for post in data['form_requests']:
                        yield FormRequest(
                            url = post['url'],
                            formdata = post['post_params'],
                            meta = {'post_params' : post['post_params']},
                            dont_filter = True
                        )
                self.logger.info("end yield form requests: " + response.url)
                self.logger.info("start yield items: " + response.url)
                if ('items' in data):
                    for tmp_items in data['items']:
                        # print(tmp_items)
                        if ('item_cfg' in tmp_items):
                            item = eval(tmp_items['item_cfg'] + '_item.' + tmp_items['item_cfg'] + '_item()')
                        else:
                            item = eval(rule['func'] + '_item.' + rule['func'] + '_item()')
                        for tmp_item in tmp_items['data']:
                            for item_key in tmp_item:
                                item[item_key] = tmp_item[item_key]
                                if ('item_cfg' in tmp_items):
                                    item['pipline_func'] = tmp_items['item_cfg'] + '_pipline.' + tmp_items['item_cfg'] + '_pipline'
                                else:
                                    item['pipline_func'] = rule['func'] + '_pipline.' + rule['func'] + '_pipline'
                            # print(item)
                            yield item
                self.logger.info("end yield items for url: " + response.url)
        else:
            # print('no rule matched for url: ' + response.url)
            self.logger.warning('no rule matched for url: ' + response.url)
        end = datetime.datetime.now()

        self.logger.info("parse end for url: " + response.url + ', cost ' + str((end-start).seconds) + ' seconds')



