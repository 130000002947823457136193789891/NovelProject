import scrapy
import re
from scrapy.http import Request
from items import NovelprojectItem
from items import NovelprojectItem2


class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['www.quanshuwang.com']
    offset=1
    adr = ".html"
    url="http://www.quanshuwang.com/list/1_"
    start_urls=[url+str(offset)+".html"]
    # start_urls = ['http://www.quanshuwang.com/list/1_1.html']  # 全书网玄幻魔法类第一页


    # ********** Begin **********#
    # 1.定义函数，通过'马上阅读'获取每一本书的 URL
    def parse(self, response):
        book_urls = response.xpath('//li/a[@class="l mr10"]/@href').extract()#
        three_book_urls = book_urls[0:32]
        for book_url in three_book_urls:
            yield Request(book_url, callback=self.parse_read)


        # #offset+=1,在函数的最后实现翻页功能# #offset+=1,在函数的最后实现翻页功能

        if self.offset< 10:
            self.offset+=1
            self.start_urls = [self.url + str(self.offset) + self.adr]
            yield Request(self.url + str(self.offset) + self.adr,callback=self.parse)

    # 2.定义函数，进入小说简介页面，获取信息，得到后yield返回给pipelines处理，并获取'开始阅读'的url，进入章节目录
    def parse_read(self, response):
        item = NovelprojectItem()
        name = response.xpath('//div[@class="b-info"]/h1/text()').extract_first()
        description = response.xpath('//div[@class="infoDetail"]/div/text()').extract_first()
        state = response.xpath('//div[@class="bookDetail"]/dl[1]/dd/text()').extract_first()
        author = response.xpath('//div[@class="bookDetail"]/dl[2]/dd/text()').extract_first()
        item['name'] = name
        item['description'] = description
        item['state'] = state
        item['author'] = author
        #随着需要导出哪个数据变化，有时不要注释这一句。
        # yield item
        read_url = response.xpath('//a[@class="reader"]/@href').extract()[0]
        #读取详细信息，章节。
        yield Request(read_url, callback=self.parse_info)
        # #offset+=1,在函数的最后实现翻页功能
        # if self.offset<100:
        #     self.offset+=1
        #     yield Request(self.start_urls+self.str(self.offset),callback=self.parse_read())
        # for self.offset in range(100):
        #     self.start_urls = [self.url + str(self.offset) + ".html"]
        #     yield Request(self.start_urls,callback=self.parse)
        # yield item

    # 3.定义函数，进入章节目录，获取小说章节名并yield返回
    def parse_info(self, response):
        item = NovelprojectItem2()
        # tablename=response.xpath('//div[@class="b-info"]/h1/text()').extract_first()
        # tablename = response.xpath('//div[@class="main-index"]/a3/text()').extract_first()
        titles = response.xpath('//div[@class="clearfix dirconone"]/li')
        tablename=response.xpath('//*[@id="chapter"]/div[3]/div[1]/strong/text()').extract_first()
        for each in titles:
            title = each.xpath('.//a/text()').extract_first()
            item['tablename'] = tablename
            item['title'] = title
            #有时要注释这一句
            yield item

    # ********** End **********#
