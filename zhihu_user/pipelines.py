# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class ZhihuUserPipeline(object):
    #
    # def process_item(self, item, spider):
    #     return item

    def __init__(self):
        # 打开文件，指定方式为写，利用第3个参数把csv写数据时产生的空行消除
        self.f = open("zhihu_user.csv", "a", newline="", encoding='utf-8')
        # 设置文件第一行的字段名，注意要跟spider传过来的字典key名称相同
        self.fieldnames = ['id', 'url_token', 'name', 'use_default_avatar', 'avatar_url', 'avatar_url_template',
                           'is_org', 'type', 'url', 'user_type', 'headline', 'gender',
                           'is_advertiser', 'vip_info', 'badge', 'badge_v2', 'is_following', 'is_followed',
                           'follower_count', 'answer_count', 'articles_count', 'is_realname',
                           ]

        # 指定文件的写入方式为csv字典写入，参数1为指定具体文件，参数2为指定字段名
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        # 写入第一行字段名，因为只要写入一次，所以文件放在__init__里面
        self.writer.writeheader()

    def process_item(self, item, spider):
        # 写入spider传过来的具体数值
        self.writer.writerow(item)
        # 写入完返回
        return item

    def close(self, spider):
        self.f.close()
