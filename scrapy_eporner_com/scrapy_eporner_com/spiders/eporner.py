# -*- coding: utf-8 -*-
import scrapy


class EpornerSpider(scrapy.Spider):
    name = 'eporner'
    allowed_domains = ['epoener.com']
    start_urls = ['http://epoener.com/']

    def parse(self, response):
        with open("./log","a+") as f:
            f.write("aaaa")
        pass
