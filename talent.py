# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TalentSpider(scrapy.Spider):
    name = 'talent'
    source_url = 'https://www.tv-ranking.com'
    allowed_domains = ['tv-ranking.com']
    start_urls = [
        source_url
    ]

    def parse(self, response):
        if 'tv-ranking.com/detail/' in response.url:
            talent_name = response.css('h1::text').get()
            if talent_name:
                yield {'name': talent_name}

        urls = response.css('a::attr(href)').extract()
        for url in urls:
            yield response.follow(f"https://www.tv-ranking.com{url}", callback=self.parse)
