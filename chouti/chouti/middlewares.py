# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http import HtmlResponse


class ChoutiDownloaderMiddleware(object):
    def process_request(self, request, spider):
        browser = webdriver.Chrome(
            executable_path="C:/Users/天选之人/AppData/Local/Google/Chrome/Application/chromedriver.exe")
        browser.get(request.url)
        time.sleep(4)
        for i in range(30):
            time.sleep(0.5)
            browser.execute_script("window.scrollBy(0, 100)")

        html = browser.page_source

        browser.close()
        return HtmlResponse(url=request.url, body=html.encode("utf-8"), encoding='utf-8', request=request)





