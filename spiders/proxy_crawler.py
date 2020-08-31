import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider
from scrapy.exceptions import CloseSpider
from ..items import ProxyItem
import sys

class ProxyCrawler(CrawlSpider):
    name = "proxy_crawler"
    allowed_domains = ['proxynova.com']
    start_urls = []

    def __init__(self, *a, **kw):
        super(ProxyCrawler, self).__init__(*a, **kw)
        with open('google_scraper/data/proxy_crawl_list.txt', 'r') as f:
            for line in f.readlines():
                self.start_urls.append(line.strip())
    
    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url, self.parse, dont_filter=True)
    
    def parse(self, response):
        proxies = [x[16:-3] for x in response.xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr/td[1]/abbr/script/text()').extract()]
        ports = [x.strip() for x in response.xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr/td[2]/text()').extract()]
        for i in range(len(proxies)):
            proxy_item = ProxyItem()
            proxy_item["proxy_address"] = proxies[i]
            proxy_item["proxy_port"] = ports[i]
            yield proxy_item

