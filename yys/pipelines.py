# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from yys import settings
from yys.items import YysItem #数据库结构
class YysPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            port=settings.MYSQL_PORT,
            charset='utf8',
            use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if item.__class__ == YysItem:
            try:
                print ('执行sql')
                # print (item)
                insert_sql= "insert into yys values(%s,%s,%s,%s,%s,%s,%s,%s)"
                # print (insert_sql)
                # print (item['id'])
                # self.cursor.execute(insert_sql,('test','1','2','3','44','5','5','6'))
                self.cursor.execute(insert_sql,(item['rep_id'],item['get_time'],item['whi'],item['level'],item['name'],item['nick'],item['server'],item['uid']))
                self.connect.commit()
            except Exception as e:
                print (e)
            return item
