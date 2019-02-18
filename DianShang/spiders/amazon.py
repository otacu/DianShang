# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request  # 导入模块


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # 自定义配置，在Spider中custom_settings设置的是None
    custom_settings = {
        'REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        }
    }

    def start_requests(self):
        r1 = Request(
            url="https://www.amazon.cn/s/ref=nb_sb_ss_i_3_6?field-keywords=iphonex",
            headers=self.settings.get('REQUEST_HEADERS'),
        )
        yield r1

    def parse(self, response):
        # 获取商品名
        # detail_urls = response.xpath('//*[@id="result_0"]/div/div[3]/div[1]/a/h2').extract()
        # 商品单个商品详情链接
        # detail_urls = response.xpath('//*[@id="result_0"]/div/div[3]/div[1]/a/@href').extract()
        # 获取整个页面商品详情链接
        # detail_urls = response.xpath('//li[contains(@id,"result_")]/div/div[3]/div[1]/a/@href').extract()
        detail_urls = response.xpath('//*[starts-with(@id,"result")]/div/div[3]/div[1]/a/@href').extract()

        print(detail_urls)
