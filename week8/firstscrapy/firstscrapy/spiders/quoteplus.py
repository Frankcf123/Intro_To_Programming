# -*- coding: utf-8 -*-
import scrapy


class QuoteplusSpider(scrapy.Spider):
    name = 'quoteplus'
    # allowed_domains = ['http://quotes.toscrape.com/page/1/']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "sentence":quote.css('span.text::text').extract_first(),
                "author":quote.css('small.author::text').extract()[0]
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


