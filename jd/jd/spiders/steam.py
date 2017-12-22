# -*- coding: utf-8 -*-
import scrapy
import re
import json
import time
from ..items import JdItem


class SteamSpider(scrapy.Spider):
    name = 'steam'
    allowed_domains = ['list.jd.com', 'p.3.cn']
    page = 1
    urls = 'https://list.jd.com/list.html?cat=9987,653,655&page='
    start_urls = ['https://list.jd.com/list.html?cat=9987,653,655&page='+str(page)]

    def parse(self, response):
        # 商品属性
        product_all = response.xpath('//*[@id="plist"]/ul/li/div')
        # 时间戳
        now = str(time.time()).replace('.', '')
        # 价格接口
        price_url = 'https://p.3.cn/prices/mgets?skuIds=J_%s&pduid=%s904312'
        for i in product_all:
            item = JdItem()
            # 商品链接
            item['product_url'] = 'https:' + i.xpath('./div[1]/a/@href').extract()[0]
            # 商品名称
            item['product_name'] = i.xpath('./div[4]/a/em/text()').extract()[0]
            # 商品id
            item['product_id'] = i.xpath('./@data-sku').extract()[0]
            # 商品价格的url
            item['product_price_url'] = price_url % (item['product_id'], now)

            yield scrapy.Request(url=item['product_price_url'], meta={'item': item}, callback=self.get_price)
        # self.page += 1
        # # 只获得前三页
        # if self.page <= 3:
        #     yield scrapy.Request(self.urls+str(self.page),callback=self.parse)

    # 获取商品价格
    def get_price(self, response):
        item = response.meta['item']
        reg = re.compile(r'"op":"(.*?)","m"', re.S)
        item['product_price'] = reg.search(response.text).group(1)
        # print(item['product_price'])
        # print(item['product_url'])
        yield scrapy.Request(url=item['product_url'], meta={'item': item}, callback=self.get_appraise_url,
                             dont_filter=True)

    # 评论接口
    def get_appraise_url(self, response):
        item = response.meta['item']
        product_id = item['product_id']
        # 评价页码
        appraise_page = 0
        # 只抓取前五页评论
        if appraise_page < 5:
            # 评论初始接口
            appraise_url = 'http://sclub.jd.com/comment/productPageComments.action?' \
                           'productId='+str(product_id)+'&score=0&sortType=5&page='+str(appraise_page)+'&pageSize=10'
            appraise_page += 1
            yield scrapy.Request(
                url=appraise_url, method='GET', callback=self.get_appraise, meta={'item': item}, dont_filter=True,
                headers={
                    'user - agent': 'Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36'
                                   ' (KHTML, likeGecko) Chrome / 62.0.3202.94Safari / 537.36',
                    'referer': 'https://item.jd.com/'+product_id+'.html'
                },
            )

    # 获取评论
    def get_appraise(self, response):
        item = response.meta['item']
        # reg = re.compile(r'\((.*?)\);', re.S)
        # data = reg.search(response.text).group(1)
        new_data = json.loads(response.text)
        user_dict = {}
        user_list = []
        # 总体评价
        all_appraise = new_data.get('productCommentSummary')
        # 评价人数
        item['all_comment'] = all_appraise.get('commentCount')
        # 好评
        item['good_comment'] = all_appraise.get('goodCount')
        # 中评
        item['gen_comment'] = all_appraise.get('generalCount')
        # 差评
        item['bad_comment'] = all_appraise.get('poorCount')
        # 追评
        item['add_comment'] = all_appraise.get('afterCount')
        # 用户评价,列表
        comments = new_data.get('comments')

        for i in comments:
            # 每个用户的信息,用字典存起来
            user_dict['id'] = i['id']
            user_dict['nickname'] = i['nickname']
            user_dict['content'] = i['content']
            user_dict['creationTime'] = i['creationTime']
            user_dict['replyCount'] = i['replyCount']
            user_dict['score'] = i['score']
            user_dict['usefulVoteCount'] = i['usefulVoteCount']
            user_dict['userExpValue'] = i['userExpValue']  # 京享值
            user_dict['userLevelName'] = i['userLevelName']  # 会员等级
            user_dict['productColor'] = i['productColor']  # 手机颜色
            user_dict['productSize'] = i['productSize']  # 手机参数
            # 将一个用户的信息和评论存到列表中
            user_list.append(user_dict)
        item['comment_info'] = user_list
        yield item
