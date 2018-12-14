from redis import Redis
import pymysql

from example import settings
from scrapy.exceptions import DontCloseSpider
from scrapy_redis.spiders import RedisSpider

class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'master'
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
            host = settings.REDIS_HOST,
            port = settings.REDIS_PORT,
            password = settings.REDIS_PASSWORD,
            db = settings.DB
        )
        try:
            my_len = r.llen('haina:start_urls')
        except Exception as e:
            print(e)
        # print(my_len)
        my_len1 = r.zcard('haina:requests')
        # print(my_len1)
        total = my_len + my_len1
        print(total)
        if (total < 1024):#64进程*每次获取16个
            conn = pymysql.connect(
                host = settings.MYSQL_HOST,
                user = settings.MYSQL_USER,  
                password = settings.MYSQL_PASSWORD,
                db = settings.MYSQL_DB,
                charset = settings.MYSQL_CHATSET,
                port = settings.MYSQL_PORT
            )
            cursor = conn.cursor()

            sql = 'select site from bad_site'
            print(sql)
            cursor.execute(sql)    #执行sql语句  
            results = cursor.fetchall()
            if (len(results) > 0):
                sql = 'select id, url from task where 1 = 1'
                for row in results:
                    sql += ' and url not like "' + row[0] + '%"'
                sql += ' order by pri_level desc, created limit 1024'
                print(sql)
                cursor.execute(sql)    #执行sql语句  
                results = cursor.fetchall()
                print(len(results))
            if (len(results) == 0):
                sql = 'select id, url from task order by pri_level desc, created limit 1024'
                print(sql)
                cursor.execute(sql)    #执行sql语句  
                results = cursor.fetchall()
            print(len(results))
            ids = []
            for row in results:
                url = row[1]
                ids.append(row[0])
                r.lpush('haina:start_urls', url)
            sql = 'delete from task where id in %s'
            cursor.execute(sql, [ids])
            conn.commit()

            cursor.close()
            conn.close()