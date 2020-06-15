# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuUserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    url_token = scrapy.Field()
    name = scrapy.Field()
    use_default_avatar = scrapy.Field()
    avatar_url = scrapy.Field()
    avatar_url_template = scrapy.Field()
    is_org = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    user_type = scrapy.Field()
    headline = scrapy.Field()
    gender = scrapy.Field()
    is_advertiser = scrapy.Field()
    vip_info = scrapy.Field()
    badge = scrapy.Field()
    badge_v2 = scrapy.Field()
    is_following = scrapy.Field()
    is_followed = scrapy.Field()
    follower_count = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    is_realname = scrapy.Field()


    #
    # avatar_url = Field()
    # avatar_url_template = Field()
    # badge = Field()
    # employments = Field()
    # follower_count = Field()
    # gender = Field()
    # headline = Field()
    # id = Field()
    # is_advertiser = Field()
    # is_blocking = Field()
    # is_followed = Field()
    # is_following = Field()
    # is_org = Field()
    # name = Field()
    # type = Field()
    # url = Field()
    # url_token = Field()
    # user_type = Field()
