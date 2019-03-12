# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import SignalTestItem


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = r'https://www.kuaidaili.com/free/inha/{page}/'

    def start_requests(self):
        for i in range(1, self.settings.get('PAGE')+1):
            yield Request(self.start_urls.format(page=i), callback=self.parse)

    def parse(self, response):
        ip = response.xpath("//tr/td[1]/text()").extract()
        port = response.xpath("//tr/td[2]/text()").extract()
        proxies = map(lambda x, y: 'http://'+x+':'+y, ip, port)
        for k in proxies:
            item = SignalTestItem()
            item['proxy'] = k
            yield item
