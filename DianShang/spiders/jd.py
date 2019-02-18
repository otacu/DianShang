# -*- coding: utf-8 -*-
import scrapy
import re

from DianShang.items import JdItem

url_prefix = "https://search.jd.com/Search?keyword=dr.martens&enc=utf-8&qrst=1&rt=1&stop=1&spm=2.1.0&vt=2&page={}"

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    # 因为页码都是奇数，总数24页
    start_urls = [url_prefix.format(2*i-1) for i in range(1,24)]

    def parse(self, response):
        for itemSelector in response.xpath('//div[@id="J_goodsList"]/ul/li/div'):
            # 虽然是extract()[0]取第一个元素，但是每次yield之后就会自动取下一个元素
            nameHtml = itemSelector.xpath('div[@class="p-name p-name-type-2"]/a/em').extract()[0]
            dr = re.compile(r'<[^>]+>', re.S)
            name = dr.sub('', nameHtml)
            # print(name)
            item = JdItem()
            item['name'] = name
            item['img'] = itemSelector.xpath('div[@class="p-img"]/a/img/@source-data-lazy-img').extract()[0]
            item['price'] = itemSelector.xpath('div[@class="p-price"]/strong/i/text()').extract()[0]
            item['shop'] = itemSelector.xpath('div[@class="p-shop"]/span/a/text()').extract()[0]
            yield item




