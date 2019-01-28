# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

"""
taptap游戏评论数据爬取,不登录爬取
"""


class TaptapSpider(scrapy.Spider):
    name = 'taptap'
    allowed_domains = ['taptap.com']
    start_urls = 'https://www.taptap.com/{}'
    game_name = ''

    def start_requests(self):
        """
        第一个请求
        :return:
        """
        yield Request(url=self.start_urls.format(self.game_name), callback=self.parse())

    def parse(self, response):
        pass
