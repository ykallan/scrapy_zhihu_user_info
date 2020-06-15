# -*- coding: utf-8 -*-
import scrapy
import json
# scrapy zhihu userinfo
from ..items import ZhihuUserItem


class ZhSpider(scrapy.Spider):
    name = 'zh'
    # allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/xpqiu/following']
    start_user = 'teng-xun-ke-ji'
    following = 'https://www.zhihu.com/api/v4/members/{}/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
    followers = 'https://www.zhihu.com/api/v4/members/{}/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'

    def start_requests(self):
        yield scrapy.Request(url=self.following.format(self.start_user), callback=self.parse_following)
        yield scrapy.Request(url=self.followers.format(self.start_user), callback=self.parse_following)

    def parse_following(self, response):
        resp_json = json.loads(response.text)
        next_page = resp_json['paging']['next']
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse_following)

        data = resp_json['data']
        for i in data:
            item = ZhihuUserItem()
            for k, v in i.items():
                item[k] = i[k]
            yield item
            yield scrapy.Request(url=self.following.format(i['url_token']), callback=self.parse_following)
