# -*- coding: utf-8 -*-
import scrapy
import json
import json
from selenium import webdriver
import time



class SpSpider(scrapy.Spider):
    name = 'sp'
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        print(response.text)

