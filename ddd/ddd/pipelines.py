# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.media import MediaPipeline
from scrapy.utils.project import get_project_settings

class ImagesPipeline(MediaPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        mv_link = item['mv_link']
        yield scrapy.Request(mv_link)



