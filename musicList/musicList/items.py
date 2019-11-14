# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicListItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tid = scrapy.Field()
    listName = scrapy.Field()
    uid = scrapy.Field()
    userName = scrapy.Field()
    type = scrapy.Field()
    favor = scrapy.Field()

