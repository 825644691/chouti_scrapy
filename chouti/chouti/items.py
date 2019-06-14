# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChoutiItem(scrapy.Item):
    title = scrapy.Field()
    summary = scrapy.Field()
    praise_count = scrapy.Field()
    username = scrapy.Field()
    comment_count = scrapy.Field()
    img_url = scrapy.Field()
