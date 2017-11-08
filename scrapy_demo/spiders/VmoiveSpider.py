#!/usr/bin/env python
# coding=utf-8

import scrapy

from scrapy_demo.items import ScrapyDemoItem


class VmoiveSpider(scrapy.Spider):
    # name是spider最重要的属性, 它必须被定义。同时它也必须保持唯一
    name = 'vmoive'

    # 可选定义。包含了spider允许爬取的域名(domain)列表(list)
    allowed_domains = ['vmovier.com']

    start_urls = [
        'http://www.vmovier.com/'
    ]

    def parse(self, response):
        self.log('item page url is ==== ' + response.url)

        moivelist = response.xpath("//li[@class='clearfix']")

        for m in moivelist:
            item = ScrapyDemoItem()
            item['cover'] = m.xpath('./a/img/@src')[0].extract()
            item['title'] = m.xpath('./a/@title')[0].extract()
            item['dec'] = m.xpath("./div/div[@class='index-intro']/a/text()")[0].extract()
            # print(item)

            urlitem = m.xpath('./a/@href')[0].extract()
            url = response.urljoin(urlitem)
            # 如果你想将上面的 item 字段传递给 parse_moive, 使用 meta 参数
            yield scrapy.Request(url, callback=self.parse_moive, meta={
                'cover':item['cover'],
                'title': item['title'],
                'dec': item['dec'],
            })

    def parse_moive(self, response):

        item = ScrapyDemoItem()
        item['cover'] = response.meta['cover']
        item['title'] = response.meta['title']
        item['dec'] = response.meta['dec']
        item['playUrl'] = response.xpath("//div[@class='p00b204e980']/p/iframe/@src")[0].extract()
        yield item