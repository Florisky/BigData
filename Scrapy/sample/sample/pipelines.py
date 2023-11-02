# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class SamplePipeline:
    fp = None
    def open_spider(self, spider):
        print("开始爬虫......")
        self.fp = open('豆瓣电影.txt', 'w',encoding='utf-8')

    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_title = item['movie_title']
        movie_ranking = item['movie_ranking']
        movie_score = item['movie_score']
        movie_number = item['movie_number']
        movie_actor = item['movie_actor']
        movie_dire = item['movie_dire']
        movie_reladate = item['movie_reladate']
        movie_country = item['movie_country']
        movie_type = item['movie_type']

        self.fp.write(movie_ranking + '\t' + movie_name + '\t' + movie_title + '\t' + movie_score + '\t' + movie_number + '\t' + movie_actor + '\t' + movie_dire + '\t' + movie_reladate + '\t' + movie_country + '\t' + movie_type + '\n')

        return item

    def close_spider(self, spider):
        print("结束爬虫")
        self.fp.close()

class mysqlPipeline:
    conn = None
    coursor = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='Walnut111',
            database='douban_movie',
            port=3306,
            charset='utf8'
        )

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(
                'insert into douban_movie values("%d","%s","%f","%d","%s","%s","%s","%s","%s","%s")' % (
                int(item['movie_ranking']), item["movie_name"], float(item['movie_score']),
                int(item['movie_number']), item['movie_title'], item['movie_dire'], item['movie_actor'],
                item['movie_reladate'], item['movie_country'], item['movie_type']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        print("数据导入到数据库！！！")
        self.conn.close()
        self.cursor.close()