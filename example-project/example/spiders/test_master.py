from redis import Redis
import pymysql

from example import test_settings
from scrapy.exceptions import DontCloseSpider
from scrapy_redis.spiders import RedisSpider

class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'test_master'
    redis_key = 'master:start_urls'

    def spider_idle(self):
        """Schedules a request if available, otherwise waits."""
        # XXX: Handle a sentinel to close the spider.
        print('idle')

        self.add_url()
        # self.schedule_next_requests()
        raise DontCloseSpider

    def add_url(self):
        print('in add')
        r = Redis(
            host = test_settings.REDIS_HOST,
            port = test_settings.REDIS_PORT,
            password = test_settings.REDIS_PASSWORD,
            db = test_settings.DB
        )
        url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/caDetailList/001607230057395102?get_cnt='
        r.lpush('haina:start_urls', url)



#rtn_data完整格式
# rtn_data = {
#     'items' : [
#         {
#             'item_cfg' : 'comp_quali_cnt',#可选
#             'data' : [
#                 {
#                     'comp_id' : comp_id,
#                     'qymc' : qymc,
#                     'tyshxydm' : tyshxydm,
#                     'qyfddbr' : qyfddbr,
#                     'qydjzclx' : qydjzclx,
#                     'qyzcsd' : qyzcsd,
#                     'qyjydz' : qyjydz
#                 },
#                 {
#                     'comp_id' : comp_id,
#                     'qymc' : qymc,
#                     'tyshxydm' : tyshxydm,
#                     'qyfddbr' : qyfddbr,
#                     'qydjzclx' : qydjzclx,
#                     'qyzcsd' : qyzcsd,
#                     'qyjydz' : qyjydz
#                 }
#             ]
#         },
#         {
#             'item_cfg' : 'comp_quali_cnt',#可选
#             'data' : [
#                 {
#                     'comp_id' : comp_id,
#                     'qymc' : qymc,
#                     'tyshxydm' : tyshxydm,
#                     'qyfddbr' : qyfddbr,
#                     'qydjzclx' : qydjzclx,
#                     'qyzcsd' : qyzcsd,
#                     'qyjydz' : qyjydz
#                 },
#                 {
#                     'comp_id' : comp_id,
#                     'qymc' : qymc,
#                     'tyshxydm' : tyshxydm,
#                     'qyfddbr' : qyfddbr,
#                     'qydjzclx' : qydjzclx,
#                     'qyzcsd' : qyzcsd,
#                     'qyjydz' : qyjydz
#                 }
#             ]
#         }
#     ],
#     'form_requests' : [
#         {
#             'url' : response.url,
#             'post_params' : {
#                 '$total': str(total),
#                 '$reload': '0',
#                 '$pg': str(i),
#                 '$pgsz': '48'
#             }
#         },
#         {
#             'url' : response.url,
#             'post_params' : {
#                 '$total': str(total),
#                 '$reload': '0',
#                 '$pg': str(i),
#                 '$pgsz': '48'
#             }
#         }
#     ],
#     'requests' : [
#         url,
#         url
#     ],
#    'msg' : 'find not main comp_id: ' + comp_id + ', main_comp_id: ' + main_comp_id
# }