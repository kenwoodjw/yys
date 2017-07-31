#coding:utf-8

import scrapy,json
from yys.items import YysItem
from scrapy.selector import  Selector #选择器
from .get_urls import get_url

class Yyspider(scrapy.Spider):
    name='yys'
    allow_domain=['comp-sync.webapp.163.com']
    start_urls=get_url()

    def parse(self, response):
        items=[]
        item=YysItem()
        jsonresponse = json.loads(response.body_as_unicode())
        # print (jsonresponse)
        try:
            for j in jsonresponse['data']:
                item['rep_id']=j['req_id']
                item['get_time']=j['get_time']
                item['whi']=j['prop_info']['from']
                item['level']=j['prop_info']['prop_name'].split("式神")[0]
                item['name']=j['prop_info']['prop_name'].split("式神")[-1]
                item['nick']=j['user_info']['nick']
                item['server']=j['user_info']['server']
                item['uid']=j['user_info']['uid']
                yield item
        except Exception as e:
            print (e)


