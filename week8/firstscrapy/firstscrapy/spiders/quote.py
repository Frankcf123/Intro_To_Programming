# -*- coding: utf-8 -*-
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['http://quotes.toscrape.com/page/1/']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        with open("response.html",'wb') as f:
            f.write(response.body)
