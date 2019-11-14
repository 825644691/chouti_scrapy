# -*- coding: utf-8 -*-
import scrapy
from musicList.items import MusicListItem
import json

class MuSpider(scrapy.Spider):
    name = 'ml'
    start_urls = ['https://u.y.qq.com/cgi-bin/musicu.fcg?_=1573699260580&g_tk=240417613&uin=825644691&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&ct=23&cv=0&data=%7B%22list%22%3A%7B%22module%22%3A%22playlist.PlayListCategoryServer%22%2C%22method%22%3A%22get_category_content%22%2C%22param%22%3A%7B%22cmd%22%3A0%2C%22caller%22%3A%22825644691%22%2C%22category_id%22%3A3056%2C%22last_id%22%3A%227256512634%22%2C%22size%22%3A20%7D%7D%7D']

    def parse(self, response):
        items = json.loads(response.text)['list']['data']['content']['v_item']
        for i in items:
            item = MusicListItem()
            item['tid'] = int(i['basic']['tid'])
            item['listName'] = i['basic']['title']
            item['uid'] = int(i['basic']['creator']['uin'])
            print(type(item['uid']))
            item['userName'] = i['basic']['creator']['nick']
            item['type'] = 1
            item['favor'] = int(i['basic']['play_cnt'])
            yield item
