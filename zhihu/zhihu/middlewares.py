# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium import webdriver
import time
import json
import scrapy


class ZhihuDownloaderMiddleware(object):
   def process_request(self, request, spider):
      f1 = open("cookie.txt")
      cookies = f1.read()
      cookies = json.loads(cookies)
      request.cookies = cookies




