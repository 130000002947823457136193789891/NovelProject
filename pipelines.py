# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymysql
from items import NovelprojectItem, NovelprojectItem2


class NovelprojectPipeline(object):
    def process_item(self, item, spider):

        # print(dict(item))

        # # ********** Begin **********#
        # # 1.和本地的数据库mydb建立连接
        # connection = pymysql.connect(
        #     host='localhost',
        #     port=3306,
        #     user='root',
        #     passwd='123123',
        #     db='mydb',
        #     charset='utf8',
        # )
        #
        if isinstance(item, NovelprojectItem):
            # print(dict(item))
            print('ok')
        # #2.处理来自NovelprojectItem的item（处理完成后return返回item）
        # name = item['name']
        # author = item['author']
        # state = item['state']
        # description = item['description']
        # try:
        #     with connection.cursor() as cursor:
        #         sql1 = 'Create Table If Not Exists novel(name varchar(20) CHARACTER SET utf8 NOT NULL,author varchar(10) CHARACTR SET utf8,state varchar(20) CHARACTER SET utf8 ,description text CHARACTER SET utf8,PRIMARY KEY(name))'
        #         sql2 = 'Insert into novel values(\'%s\',\'%s\',\'%s\',\'%s\')' % (name, author, state, description)
        #         cursor.excute(sql1)
        #         cursor.excute(sql2)
        #     connection.commit()
        # finally:
        #     connection.close()
            return item
        #
        elif isinstance(item, NovelprojectItem2):
            # print(dict(item))
            print('ok2')
        # # 3.处理来自NovelprojectItem2的item（处理完成后return返回item）
        # tablename = item['tablename']
        # title = ['title']
        # try:
        #     with connection.cursor() as cursor:
        #         sql3 = 'create table if not exists %s(title varchar(20) CHARACTER SET utf8 NOT NULL,PRIMARY KEY(title)' % tablename))'
        #         sql4 = 'insert into %s values(\'%s\')' % (tablename, title)
        #         cursor.excute(sql3)
        #         cursor.excute(sql4)
        #         connection.commit()
        # finally:
        #     connection.close()
        return item

    # ********** End **********#
