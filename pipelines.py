# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json, codecs

class GoogleScraperPipeline:
    def __init__(self):
        self.items = []
        self.file = open('google_scraper/data/gg_search.json', 'w') # open('items.json', 'w')

    def close_spider(self, spider):
        json.dump(self.items, self.file)
        self.file.close()

    def process_item(self, item, spider):            
        self.items.append(dict(item))
        return item

class ProxyPipeline(object):
    def __init__(self):
        self.items = []
        self.file = open('google_scraper/data/proxies.json', 'w') # open('items.json', 'w')

    def close_spider(self, spider):
        json.dump(self.items, self.file)
        self.file.close()

    def process_item(self, item, spider):            
        self.items.append(dict(item))
        return item
