# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .settings import MONGODB_DOCNAME,MONGODB_DBNAME,MONGODB_PORT,MONGODB_HOST


class MongodbPipeline(object):
    def __init__(self):
        connect = pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
        db = connect[MONGODB_DBNAME]
        self.coll = db[MONGODB_DOCNAME]

    def process_item(self, item, spider):
        data = dict(item)
        self.coll.insert(data)
        return item


class JdPipeline(object):
    def process_item(self, item, spider):
        return item
