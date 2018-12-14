# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class MyTestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyTestDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



import base64

""" 阿布云ip代理配置，包括账号密码 """
proxyServer = "http://http-dyn.abuyun.com:9020"
# 5+ 15
proxyUser = "HQ1F5O5K7B43V0KD"
proxyPass = "10E66932CE6519AE"
# 5+17
# proxyUser = "HW3S31ME708FR7GD"
# proxyPass = "3D75CFF85FD6E2F4"
# 5+20
# proxyUser = "HLJ47B72M43284BD"
# proxyPass = "43E3C62AE0A9BC17"

# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")
class ABProxyMiddleware(object):
    """ 阿布云ip代理配置 """
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth


from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.python import global_object_name
import time

class MyRetryMiddleware(RetryMiddleware):

    def _retry(self, request, reason, spider):
        spider.logger.info("request: %(request)s", {'request': request})
        if (str(request) != '<GET http://gd.chinavnet.com>' and str(request) != '<GET http://58.53.197.134>'):
            # spider.logger.info("good retry request: %(request)s", {'request': request})
            retries = request.meta.get('retry_times', 0) + 1

            retry_times = self.max_retry_times

            if 'max_retry_times' in request.meta:
                retry_times = request.meta['max_retry_times']

            stats = spider.crawler.stats
            if retries <= retry_times:
                spider.logger.warning("Retrying %(request)s (failed %(retries)d times): %(reason)s",
                             {'request': request, 'retries': retries, 'reason': reason},
                             extra={'spider': spider})
                retryreq = request.copy()
                retryreq.meta['retry_times'] = retries
                retryreq.dont_filter = True
                retryreq.priority = request.priority + self.priority_adjust

                if isinstance(reason, Exception):
                    reason = global_object_name(reason.__class__)

                stats.inc_value('retry/count')
                stats.inc_value('retry/reason_count/%s' % reason)
                return retryreq
            else:
                stats.inc_value('retry/max_reached')
                spider.logger.warning("Gave up retrying %(request)s (failed %(retries)d times): %(reason)s",
                             {'request': request, 'retries': retries, 'reason': reason},
                             extra={'spider': spider})
        # else:
        #     spider.logger.info("bad retry request: %(request)s", {'request': request})