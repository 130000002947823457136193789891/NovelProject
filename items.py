import scrapy


# 存放全部小说信息
class NovelprojectItem(scrapy.Item):
    # ********** Begin **********#
    name = scrapy.Field()
    author = scrapy.Field()
    state = scrapy.Field()
    description = scrapy.Field()

    # ********** End **********#


# 单独存放小说章节
class NovelprojectItem2(scrapy.Item):
    # ********** Begin **********#
    tablename = scrapy.Field()
    title = scrapy.Field()

    # ********** End **********#