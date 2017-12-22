from django.db import models

# Create your models here.
from mongoengine import *
connect('JD', host='127.0.0.1', port=27017)


class mobile(Document):
    # 商品名称
    product_name = StringField(required=True, max_length=200)
    # 商品参数
    product_type = StringField(required=True, max_length=200)
    # 商品价格
    product_price = StringField(required=True, max_length=200)
    # 商品链接
    product_url = StringField(required=True, max_length=200)
    # 商品id
    product_id = StringField(required=True, max_length=200)
    # 商品价格url
    product_price_url = StringField(required=True, max_length=200)
    # 店铺名字
    shop_name = StringField(required=True, max_length=200)
    # 评价内容
    comment_info = StringField(required=True, max_length=200)
    # 所有评价
    all_comment = StringField(required=True, max_length=200)
    # 好评
    good_comment = StringField(required=True, max_length=200)
    # 中评
    gen_comment = StringField(required=True, max_length=200)
    # 差评
    bad_comment = StringField(required=True, max_length=200)
    # 追评
    add_comment = StringField(required=True, max_length=200)

    # 自定义的管理
    # meta = {
    #     'collection': 'mobile', # 指定要连接的集合
    #     'ordering': ['-product_price'], # 默认使用评论进行排序
    # }
