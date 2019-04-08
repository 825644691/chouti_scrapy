# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = ''

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 ',
     'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'zhihu.middlewares.ZhihuDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu.pipelines.MysqlTwistedPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'

#你自己数据库的密码
MYSQL_PASSWORD = '8256'
MYSQL_PORT = 3306
COOKIES = {'__utmz': '51854390.1532780422.3.3.utmcsr', '_xsrf': 'SgZQS6L3lTNIhzeCELXx9ZtVYGrg5M0Z', 'cap_id': 'OWFlYzc2ODY4NTg5NDBlYjhhZjllNWEwNGYyY2ZkMjU', 'l_cap_id': 'NzQyOGUwMWVlNGI0NDNjM2FlOWViYTRjNTQ2NTRmNDU', 'q_c1': '0aae74e465ce4dd2b6a3fa4d58c38f10|1532519787000|1532519787000', '__utma': '51854390.689596102.1532764416.1532778135.1532780422.3', 'r_cap_id': 'ZjIyM2NmODdkYmMxNDE1ZmEyMzgwMzZjMTQyMTE0YmI', 'd_c0': 'AIAkIbZm9A2PTgYcV52GGXa5SKpBy_abuYs', '__utmv': '51854390.100--|2', 'capsion_ticket': '2|1:0|10:1532785744|14:capsion_ticket|44:ZGE4MzNiMDFhZGVlNDNkOGE2ZWEwM2VjYTFhYzAzNzc', '_zap': '46f0a358-61a3-4ac7-82b9-2fce5bc0bd80', 'l_n_c': '1', 'n_c': '1', 'z_c0': '2|1:0|10:1532785779|4:z_c0|92:Mi4xRlNBdUNBQUFBQUFBZ0NRaHRtYjBEU1lBQUFCZ0FsVk5jOEpKWEFCZEpLRDc2aXYxZk5HSHhQVS1qdTFUZEl0YUp3|200d89b8ec1fcbe903aab70120b24e9dfd9ec67e7f7d197d5c070caa3c2faac8', 'tgw_l7_route': '3072ae0b421aa02514eac064fb2d64b5'}
#你自己数据库的名称
MYSQL_DB = 'mysql'
CHARSET = 'utf8'