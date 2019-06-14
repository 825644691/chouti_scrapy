# -*- coding: utf-8 -*-
import scrapy
from chouti.items import ChoutiItem
from scrapy.http import Request


class CtSpider(scrapy.Spider):
    name = 'ct'
    allowed_domains = ['chouti.com']
    start_urls = ['https://dig.chouti.com']

    def parse(self, response):

        items = response.xpath('//div[@class="content-list"]/div[@class="item"]')
        for i in items:
            item = ChoutiItem()
            item['title'] = i.xpath('normalize-space(.//div[@class="news-content"]/div[@class="part1"]/a[@class="show-content color-chag"]/text())').extract_first()
            if i.xpath('.//div[@class="news-content"]/div[@class="area-summary"]/span[@class="summary"]/text()'):
                item['summary'] = i.xpath('.//div[@class="news-content"]/div[@class="area-summary"]/span[@class="summary"]/text()').extract()[0]
            else:
                item['summary'] = None
            item['praise_count'] = i.xpath('.//div[@class="news-content"]/div[@class="part2"]/a[@class="digg-a"]/b/text()').extract()[0]
            item['username'] = i.xpath('.//div[@class="news-content"]/div[@class="part2"]/a[@class="user-a"]/b/text()').extract()[0]
            item['comment_count'] = i.xpath('.//div[@class="news-content"]/div[@class="part2"]/a[@class="discus-a"]/b/text()').extract()[0]
            img_url = i.xpath('.//div[@class="news-pic"]/img/@original').extract()[0]
            item['img_url'] = response.urljoin(img_url)
            yield item

        page_list = response.xpath("//a[@class='ct_page_edge']/@href").extract()
        for url in page_list:
            url = "https://dig.chouti.com"+str(url)
            yield Request(url)

