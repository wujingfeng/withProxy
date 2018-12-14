# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

# USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'
import random
user_agent_list = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]
UA = random.choice(user_agent_list)
USER_AGENT = UA

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

RETRY_ENABLED = True
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408, 429, 803]
RETRY_TIMES = 100

DOWNLOADER_MIDDLEWARES = {
   # 'my_test.middlewares.MyTestDownloaderMiddleware': 543,
   'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': None,
   'example.middlewares.MyRetryMiddleware': 80,
   # 'example.middlewares.ABProxyMiddleware': 543,
}

ITEM_PIPELINES = {
    'example.pipelines.CommPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'
LOG_FILE = "mySpider.log"

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 3
# DOWNLOAD_DELAY = 1

REDIS_HOST = '118.190.82.125'
REDIS_PORT = 6379
REDIS_PASSWORD = 'JonQWE520'
DB = 9
REDIS_PARAMS = {
    'password': REDIS_PASSWORD,
    'db': DB
}

MYSQL_HOST = 'rm-m5enjpq0701d13qsvmo.mysql.rds.aliyuncs.com'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'zjkl@007'
MYSQL_DB = "mohurd_crawler"
MYSQL_CHATSET = 'utf8'
MYSQL_PORT = 3306

SNAP_SAVEPATH = 'd:/crawled_files/'
# SNAP_SAVEPATH = '/nfs/crawled_files/'

#处理规则
rules = [
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/compDetail/00[\d]{16}',#用来匹配的正则
        'save_page' : False,#是否需要保存快照
        'main_area' : '//div[@class="main_box nav_mtop"]',#需要保存的主要页面区域，xpath语法
        'func' : 'comp_main'#解析函数的名字(同时控制handler,item和pipline)
    },#建筑市场公司基本信息
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/caDetailList/00[\d]{16}',
        'save_page' : False,
        'main_area' : '//table[@id="catabled"]',
        'func' : 'comp_quali'
    },#建筑市场公司资质
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/regStaffList/00[\d]{16}',
        'save_page' : False,
        'main_area' : '//table[@class="pro_table_box pro_table_borderright"]',
        'func' : 'comp_staff'
    },#建筑市场公司人员
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/compPerformanceListSys/00[\d]{16}',
        'save_page' : False,
        'main_area' : '//table[@class="pro_table_box pro_table_borderright"]',
        'func' : 'comp_proj'
    },#建筑市场公司项目
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/staff/staffPerformanceListSys/00[\d]{16}',
        'save_page' : False,
        'main_area' : '//table[@class="pro_table_box pro_table_borderright"]',
        'func' : 'staff_proj'
    },#建筑市场人员项目
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/project/projectDetail/[\d]{16}',
        'save_page' : False,
        'main_area' : '//div[@class="main_box nav_mtop"]',
        'func' : 'proj_main'
    },#建筑市场项目基本信息
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/project/tenderInfo/[\d+]',
        'save_page' : False,
        'main_area' : '//div[@class="main_box nav_mtop"]',
        'func' : 'proj_tender'
    },#建筑市场项目招投标
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/project/censorInfo/[\d+]',
        'save_page' : False,
        'main_area' : '//div[@class="main_box nav_mtop"]',
        'func' : 'proj_censor'
    },#建筑市场项目施工图审查
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/project/contractInfo/[\d+]',
        'save_page' : False,
        'main_area' : '//div[@class="main_box nav_mtop"]',
        'func' : 'proj_contract'
    },#建筑市场项目合同备案
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/project/buildliseInfo/[\d+]',
        'save_page' : False,
        'main_area' : '//div[@class="main_box nav_mtop"]',
        'func' : 'proj_buildlise'
    },#建筑市场项目施工许可
    {
        're' : 'http://jzsc.mohurd.gov.cn/dataservice/query/project/bafinishInfo/[\d+]',
        'save_page' : False,
        'main_area' : '//div[@class="main_box nav_mtop"]',
        'func' : 'proj_bafinish'
    },#建筑市场项目竣工验收备案
    {
        're' : 'http://jzsc.mohurd.gov.cn/asite/credit/record/query',
        'save_page' : False,
        'main_area' : '//tbody',
        'func' : 'credit_record'
    },#建筑市场诚信数据
    {
        're' : 'http://jzsc.mohurd.gov.cn/asite/credit/record/blackList',
        'save_page' : False,
        'main_area' : '//tbody',
        'func' : 'black_list'
    },#建筑市场黑名单数据

    {
        're' : 'http://xxgx.scjst.gov.cn/Enterprise/eZsxx.aspx[\?]id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}[\d]{0,3}',
        'save_page' : False,#页面里有一个查询时间随时变，保存快照失去意义
        'main_area' : '//div[@class="page-wrap"]',
        'func' : 'jst_comp_main'
    },#建设厅公司基本信息
    {
        're' : 'http://xxgx.scjst.gov.cn/api/getdata/GetEnteZsList/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}[\d]{0,3}',
        'save_page' : False,
        'main_area' : '//p',#这个页面直接是json接口
        'func' : 'jst_comp_quali'
    },#建设厅公司资质
    {
        're' : 'http://xxgx.scjst.gov.cn/Enterprise/rcZs.aspx[\?]id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}[\d]{0,3}',
        'save_page' : False,
        'main_area' : '//table[@class="pro_table_box datas_table"]',#这个页面直接是json接口
        'func' : 'jst_comp_quali_rc'
    },#建设厅入川公司资质
    {
        're' : 'http://xxgx.scjst.gov.cn/Enterprise/eRyxx.aspx[\?]isRc=[01]&id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}[\d]{0,3}',
        'save_page' : False,
        'main_area' : '//table[@id="catabled"]',
        'func' : 'jst_staff_list'
    },#建设厅公司人员列表
    {
        're' : 'http://xxgx.scjst.gov.cn/Person/rZsxx.aspx[\?]id=[a-fA-F0-9]{32,48}',
        'save_page' : False,
        'main_area' : '//ul[@class="tinyTab datas_tabs clearfix"]',
        'func' : 'jst_staff_cnt'
    },#建设厅人员子表个数
    {
        're' : 'http://xxgx.scjst.gov.cn/Person/rYjxx.aspx[\?]ptype=[01]&id=[a-fA-F0-9]{32,48}',
        'save_page' : False,
        'main_area' : '//tbody[@class="cursorDefault"]',
        'func' : 'jst_staff_proj'
    },#建设厅人员项目(在建、业绩)
    {
        're' : 'http://xxgx.scjst.gov.cn/api/getdata/GetryZsList/[a-fA-F0-9]{32,48}',
        'save_page' : False,
        'main_area' : '//p',#这个页面直接是json接口
        'func' : 'jst_comp_staff'
    },#建设厅公司人员
    {
        're' : 'http://xxgx.scjst.gov.cn/Enterprise/eYjxx.aspx[\?]ptype=[01]&id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}[\d]{0,3}',
        'save_page' : False,
        'main_area' : '//div[@class="plr spmtop"]',
        'func' : 'jst_proj_list'
    },#建设厅公司项目(在建、业绩)列表
    {
        're' : 'http://xxgx.scjst.gov.cn/Project/pBidxx.aspx[\?]ptype=[01]&id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//div[@id="apt_tabcontent"]',
        'func' : 'jst_proj_main'
    },#建设厅公司项目(在建、业绩)招投标列表(带基本信息)
    {
        're' : 'http://xxgx.scjst.gov.cn/Project/DiglogBid.aspx[\?]id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//div[@id="dialog_1"]',
        'func' : 'jst_proj_tender'
    },#建设厅公司项目(在建、业绩)招投标
    {
        're' : 'http://xxgx.scjst.gov.cn/project/psgtsc.aspx[\?]id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//div[@id="apt_tabcontent"]',
        'func' : 'jst_proj_censor_list'
    },#建设厅公司项目(在建、业绩)施工图审查列表
    {
        're' : 'http://xxgx.scjst.gov.cn/Project/DiglogSgt.aspx[\?]id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//div[@id="dialog_1"]',
        'func' : 'jst_proj_censor'
    },#建设厅公司项目(在建、业绩)施工图审查
    {
        're' : 'http://xxgx.scjst.gov.cn/api/getdata/GetProjHtbaList/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//p',#这个页面直接是json接口
        'func' : 'jst_proj_contract_list'
    },#建设厅公司项目(在建、业绩)合同备案列表
    {
        're' : 'http://xxgx.scjst.gov.cn/api/getdata/GetProjHtbadetail/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//p',#这个页面直接是json接口
        'func' : 'jst_proj_contract'
    },#建设厅公司项目(在建、业绩)合同备案
    {
        're' : 'http://xxgx.scjst.gov.cn/api/getdata/GetProjSgxkzList/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//p',#这个页面直接是json接口
        'func' : 'jst_proj_buildlise_list'
    },#建设厅公司项目(在建、业绩)施工许可证列表
    {
        're' : 'http://xxgx.scjst.gov.cn/api/getdata/GetProjSgxkzdetail/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//p',#这个页面直接是json接口
        'func' : 'jst_proj_buildlise'
    },#建设厅公司项目(在建、业绩)施工许可证
    {
        're' : 'http://xxgx.scjst.gov.cn/api/getdata/GetProjJgbaList/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//p',#这个页面直接是json接口
        'func' : 'jst_proj_bafinish_list'
    },#建设厅公司项目(在建、业绩)竣工验收列表
    {
        're' : 'http://xxgx.scjst.gov.cn/api/getdata/GetProjJgbadetail/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//p',#这个页面直接是json接口
        'func' : 'jst_proj_bafinish'
    },#建设厅公司项目(在建、业绩)竣工验收
    {
        're' : 'http://xxgx.scjst.gov.cn/api/getdata/GetProjEnteList/[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}',
        'save_page' : False,
        'main_area' : '//p',#这个页面直接是json接口
        'func' : 'jst_proj_comp'
    },#建设厅公司项目(在建、业绩)各方责任主体列表
    {
        're' : 'http://xxgx.scjst.gov.cn/Project/ProjEmp.aspx[\?]ptype=&id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}&qyid=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}[\d]{0,3}',
        'save_page' : False,
        'main_area' : '//div[@class="plr spmtop"]',
        'func' : 'jst_proj_staff'
    },#建设厅公司项目(在建、业绩)各方责任主体
    {
        're' : 'http://xxgx.scjst.gov.cn/Enterprise/eBlxx.aspx[\?]id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}[\d]{0,3}',
        'save_page' : False,
        'main_area' : '//div[@id="div0"]',#这个页面直接是json接口
        'func' : 'jst_comp_bad'
    },#建设厅公司不良
    {
        're' : 'http://xxgx.scjst.gov.cn/Enterprise/eLhxx.aspx[\?]id=[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}[\d]{0,3}',
        'save_page' : False,
        'main_area' : '//div[@id="ent-good"]',#这个页面直接是json接口
        'func' : 'jst_comp_good'
    },#建设厅公司良好
]