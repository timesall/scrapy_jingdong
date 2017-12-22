# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 商品名称
    product_name = scrapy.Field()
    # 商品参数
    product_type = scrapy.Field()
    # 商品价格
    product_price = scrapy.Field()
    # 商品链接
    product_url = scrapy.Field()
    # 商品id
    product_id = scrapy.Field()
    # 商品价格url
    product_price_url = scrapy.Field()
    # 店铺名字
    shop_name = scrapy.Field()
    # 评价内容
    comment_info = scrapy.Field()
    all_comment = scrapy.Field()
    good_comment = scrapy.Field()
    gen_comment = scrapy.Field()
    bad_comment = scrapy.Field()
    add_comment = scrapy.Field()

