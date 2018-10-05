# -*- coding: utf-8 -*-
import scrapy


class Hotels168comSpider(scrapy.Spider):
    name = 'hotels168com'
    allowed_domains = ['http://hotel.168.com']
    start_urls = ['http://http://hotel.168.com/']

    def parse(self, response):
        pass
