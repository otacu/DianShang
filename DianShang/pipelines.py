# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors


class DianshangPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', '123456', 'python', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if spider.name == 'jd':
            insert_sql = """
                insert into tb_dianshang_item(`name`, img, price, shop)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(insert_sql, (item["name"], item["img"], item["price"], item["shop"]))
            self.conn.commit()
