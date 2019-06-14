# -*- coding: utf-8 -*-
import scrapy
from Yamaxun.items import YamaxunItem
from selenium import webdriver

class YmxSpider(scrapy.Spider):

    name = 'ymx'
    allowed_domains = ['taobao.com/']
    start_urls = ['https://uland.taobao.com/sem/tbsearch?keyword="悬疑"']


    # def start_requests(self):
    #     browser = webdriver.Chrome(
    #         executable_path="C:/Users/天选之人/AppData/Local/Google/Chrome/Application/chromedriver.exe")
    #     browser.get("https://www.zhihu.com/signin")
    #     time.sleep(5)


    def parse(self, response):
        items = response.xpath('//div[@class="item"]')
        for i in items:
            item = YamaxunItem()
            item['book'] = i.xpath('.//span[@class="title"]/@title').extract()[0]
            yield item

