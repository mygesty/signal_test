# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class SignalTestPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient('114.116.122.217', port=27017)
        self.db = self.client['signal_test']
        self.collection = self.db['proxies']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
