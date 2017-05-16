# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy import Spider

class Movie250Spider(Spider):
    name = "movie250"
    allowed_domains = ["movie.douban.com"]

    def start_requests(self):
        head = 'https://movie.douban.com/top250?start='
        for i in range(0, 1):
            url = head + str(i)
            yield Request(url, callback=self.parse_url)

    def parse_url(self, response):
        sel = Selector(response)
        url = sel.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/@href').extract()
        print url
        return Request(url, callback=self.parse_item)

    def parse_item(self, response):
        sel = Selector(response)
        item = DoubanItem()
        item['name'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['year'] = sel.xpath('//*[@id="content"]/h1/span[2]/text()').extract()
        item['score'] = sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        item['director'] = sel.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        print item
        return item
    
