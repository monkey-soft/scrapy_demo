# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 封面
    cover = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 简述
    dec = scrapy.Field()
    # 播放地址
    playUrl = scrapy.Field()
