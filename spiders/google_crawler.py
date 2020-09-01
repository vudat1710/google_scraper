import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider
from scrapy.exceptions import CloseSpider
from ..items import GoogleScraperItem
import sys, pickle
from .utils import check_crawled_url

class GoogleSearchSpider(CrawlSpider):
    name = "google_search_crawler"
    allowed_domains = "google.com"
    start_urls = []

    def __init__(self, *a, **kw):
        super(GoogleSearchSpider, self).__init__(*a, **kw)
        dn = pickle.load(open('google_scraper/data/domain_name.pkl', 'rb'))
        for x in dn:
            self.start_urls.append('https://www.google.com/search?q={}'.format(x))
    
    def start_requests(self):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def make_requests_from_url(self, url):
        return Request(url, self.parse, dont_filter=True)

    def parse(self, response):
        selectors = response.xpath('//div[@class="ZINbbc xpd O9g5cc uUPGi"]')
        keyword = response.url.split("?q=")[1]
        for selector in selectors:
            url = selector.xpath('.//*[@class="BNeawe UPmit AP7Wnd"]/text()').extract_first()
            status, url = check_crawled_url(url, keyword)
            if status:
                item = GoogleScraperItem()
                item["keyword"] = keyword
                item["url"] = url
                item["title"] = selector.xpath('.//*[@class="BNeawe vvjwJb AP7Wnd"]/text()').extract_first()
                item["description"] = " ".join(selector.xpath('.//*[@class="BNeawe s3v9rd AP7Wnd"]/text()').extract())
                yield item