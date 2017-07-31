# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YysItem(scrapy.Item):
    rep_id=scrapy.Field()
    get_time=scrapy.Field()
    whi=scrapy.Field()
    level=scrapy.Field()
    name=scrapy.Field()
    nick=scrapy.Field()
    server=scrapy.Field()
    uid=scrapy.Field()

