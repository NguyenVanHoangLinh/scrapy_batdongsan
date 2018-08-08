# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
class TutorialPipeline(object):
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '123' # your password
        database = 'real_estate'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

    def close_spider(self, spider):
        self.connection.cursor().close()
        self.connection.close()

    def process_item(self, item, spider):
        self.connection.cursor().execute("insert into estate(estate_title,estate_address,estate_area,estate_description,estate_price,estate_type,estate_tag,estate_date,estate_seller_name,estate_seller_address,estate_seller_phone,estate_seller_mobile,estate_seller_email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['estate_title'],item['estate_address'],item['estate_area'],item['estate_description'],item['estate_price'],item['estate_type'],item['estate_tag'],item['estate_date'],item['estate_seller_name'],item['estate_seller_address'],item['estate_seller_phone'],item['estate_seller_mobile'],item['estate_seller_email']))
        self.connection.commit()
        return item
    
