# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class real_estateItem(scrapy.Item):
     estate_title = scrapy.Field()
     estate_address= scrapy.Field()
     estate_area = scrapy.Field()
     estate_description = scrapy.Field()
     estate_price = scrapy.Field()
     estate_type = scrapy.Field()
     estate_tag = scrapy.Field()
     estate_date = scrapy.Field()
     estate_seller_name = scrapy.Field()
     estate_seller_address = scrapy.Field()
     estate_seller_phone = scrapy.Field()
     estate_seller_mobile = scrapy.Field()
     estate_seller_email = scrapy.Field()
    