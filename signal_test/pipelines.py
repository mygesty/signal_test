# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from redis import StrictRedis


class SignalTestPipeline(object):
    def open_spider(self, spider):
        self.db = StrictRedis(host='114.116.123.62', port=6379, db=0)
        # self.client = pymongo.MongoClient('114.116.122.217', port=27017)
        # self.db = self.client['signal_test']
        # self.collection = self.db['proxies']

    def process_item(self, item, spider):
        proxy = item['proxy']
        if not self.db.zscore('proxies', proxy):
            self.db.zadd('proxies', 10, proxy)
        return item
