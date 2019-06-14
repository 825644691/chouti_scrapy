# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class SeSpider(scrapy.Spider):
    name = 'se'

    start_urls = ['https://www.baidu.com/']

    def __init__(self):
        self.browser = webdriver.Chrome(
            executable_path="C:/Users/天选之人/AppData/Local/Google/Chrome/Application/chromedriver.exe")
        super(SeSpider, self).__init__()
        dispatcher.connect(self.spider_closed,signals.spider_closed)

    def spider_closed(self,spider):
        self.browser.quit()


    def parse(self, response):
        url = response.xpath("//a[@name='tj_trnews']/@href")[0].extract()
        print(url)
        yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        print(response.text)
