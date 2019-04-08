# -*- coding: utf-8 -*-
import scrapy

import json
from selenium import webdriver
import time
from zhihu.items import ZhihuItem
from scrapy.utils.project import get_project_settings


class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuspider'

    start_urls = ['https://www.zhihu.com']

    def start_requests(self):
        browser = webdriver.Chrome(
            executable_path="C:/Users/天选之人/AppData/Local/Google/Chrome/Application/chromedriver.exe")
        browser.get("https://www.zhihu.com/signin")
        time.sleep(5)
        browser.find_element_by_name("username").send_keys("15521155912")
        browser.find_element_by_name("password").send_keys("87937149a")
        browser.find_element_by_xpath(
            "//button[@class='Button SignFlow-submitButton Button--primary Button--blue']").click()
        time.sleep(3)
    #    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
        cookies = browser.get_cookies()

        print(cookies)
        f1 = open("cookie.txt", "w")
        f1.write(json.dumps(cookies))
        f1.close()

        browser.quit()
        url = "https://www.zhihu.com/explore"
        yield scrapy.Request(url=url)


    #    url = "https://www.zhihu.com/explore"
    #    settings = get_project_settings()
    #    cookies = settings['COOKIES']
    #    print(cookies)
    #    yield scrapy.Request(url=url, cookies=cookies)

    def parse(self, response):
        data = response.xpath("//a[@class='zu-top-nav-userinfo ']/span[@class='name']/text()").extract()
        item = ZhihuItem()
        item['name'] = data
        url = "https://www.baidu.com"
        yield scrapy.Request(url = url, meta={'item': item}, callback=self.parse_page)

    def parse_page(self, response):
        item = response.meta['item']

        print(item)





