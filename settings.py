from .spiders.utils import load_proxies

BOT_NAME = 'google_scraper'

PROXIES_FN = 'google_scraper/data/proxies.json'
SPIDER_MODULES = ['google_scraper.spiders']
NEWSPIDER_MODULE = 'google_scraper.spiders'

ROTATING_PROXY_LIST = load_proxies(PROXIES_FN, 'google_scraper/data/proxies_l.txt')
MAX_NUM_ITEMS = 3
MAX_CONCURRENT_SPIDERS = 1
NO_DOMAINS_PER_SPIDER = 1

ITEM_PIPELINES = {
    'google_scraper.pipelines.GoogleScraperPipeline': 300,
    # 'google_scraper.pipelines.ProxyPipeline': 800,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

PROXY_ADDRESS = '206.221.176.130'
PROXY_PORT = '3128'
PROXY_AUTHENTICATED = False
AUTHENTICATED_PROXY_USERNAME = None
AUTHENTICATED_PROXY_PASSWORD = None
# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'google_scraper.middlewares.GoogleScraperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# Enable proxies rotation
# DOWNLOADER_MIDDLEWARES = {
#    'google_scraper.middlewares.GoogleScraperDownloaderMiddleware': 543,
# }
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy_rotated_proxy.downloadmiddlewares.proxy.RotatedProxyMiddleware': 750,
}
# BFO
DEPTH_PRIORITY = 1
ROTATED_PROXY_ENABLED = True
# increase performance
CONCURRENT_REQUESTS = 3
REACTOR_THREADPOOL_MAXSIZE = 200
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 200
# 'REDIRECT_ENABLED = False
# 'LOG_FILE = 'file.log'
LOG_LEVEL = 'INFO'
# 'CLOSESPIDER_ITEMCOUNT = NO_DOMAINS_PER_SPIDER * MAX_NUM_ITEMS
# 'CLOSESPIDER_PAGECOUNT = MAX_NO_ITEMS_PER_PAGE
# 'CLOSESPIDER_TIMEOUT = 1800  # 30 minutes
CONCURRENT_ITEMS = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 3
DOWNLOAD_DELAY = 3

RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 400, 403, 404]
# 'RETRY_ENABLED = False
# 'DEPTH_LIMIT = 10

# using random port for each spider
# TELNETCONSOLE_PORT = None

# encoding
FEED_EXPORT_ENCODING = 'utf-8'

USER_AGENT_LIST = 'google_scraper/data/user_agents.txt'
ROTATING_PROXY_LIST = load_proxies(PROXIES_FN, 'google_scraper/data/proxies_l.txt')
ROTATING_PROXY_CLOSE_SPIDER = False