# -*- coding: utf-8 -*-
import scrapy


class TaptapSpider(scrapy.Spider):
    name = 'taptap'
    allowed_domains = ['taptap.com']
    start_urls = ['https://www.taptap.com/']

    def parse(self, response):
        pass
