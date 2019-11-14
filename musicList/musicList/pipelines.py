# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy
from scrapy.utils.project import get_project_settings


class MusiclistPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        c = settings['CHARSET']
        port = settings['MYSQL_PORT']
        self.con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)

    def process_item(self, item, spider):

        cue = self.con.cursor()
        cue.execute('insert into songList(tid, listName, uid, userName, type, favor)values (%s, %s, %s, %s, %s, %s)',
                    (item['tid'], item['listName'], item['uid'], item['userName'], item['type'], item['favor']))
        self.con.commit()
        return item


