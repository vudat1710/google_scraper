# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class GoogleScraperItem(Item):
    keyword = Field()
    url = Field()
    title = Field()
    description = Field()

class ProxyItem(Item):
    proxy_address = Field()
    proxy_port = Field()
