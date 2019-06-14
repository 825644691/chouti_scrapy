# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os
from chouti.settings import IMAGES_STORE


class ChoutiPipeline(object):
    def process_item(self, item, spider):
        settings = get_project_settings()

        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c = settings['CHARSET']
        port = settings['MYSQL_PORT']
        con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
        cue = con.cursor()
        cue.execute('insert into chouti(title,content,praise_count,username,count)values(%s,%s,%s,%s,%s)',
                    (item["title"], item['summary'], item['praise_count'], item['username'], item["comment_count"]))
        con.commit()
        return item


class CTPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['img_url']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        # print(results)
        # [(True, {'url': 'https://rpic.douyucdn.cn/acrpic/170827/3034164_v1319.jpg',
        # 'checksum': '7383ee5f8dfadebf16a7f123bce4dc45', 'path': 'full/6faebfb1ae66d563476449c69258f2e0aa24000a.jpg'})]
        image_path = [x['path'] for ok, x in results if ok]
        os.rename(IMAGES_STORE + image_path[0], IMAGES_STORE + item['username'] + '.jpg')

        settings = get_project_settings()

        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c = settings['CHARSET']
        port = settings['MYSQL_PORT']
        con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
        cue = con.cursor()
        cue.execute('insert into chouti(title,content,praise_count,username,count)values(%s,%s,%s,%s,%s)',
                    (item["title"], item['summary'], item['praise_count'], item['username'], item["comment_count"]))
        con.commit()
        return item


