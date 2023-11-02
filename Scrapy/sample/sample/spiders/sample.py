import scrapy
from lxml import etree
from ..items import SampleItem
import re
# class SampleSpider:
#     name = 'sample'
#     start_urls = ["https://movie.douban.com/top250"]

class FirstSpider(scrapy.Spider):
    name = "sample"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        page = response.text
        tree = etree.HTML(page)
        li_list = tree.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in li_list:
            # 获取电影排名
            movie_ranking = li.xpath('./div/div[1]/em/text()')[0]
            # 获取电影的名称
            movie_name = li.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
            # 获取电影的主题
            movie_title = li.xpath('./div/div[2]/div[2]/p[2]/span/text()')
            # 判断电影的主题是否为空
            if len(movie_title) == 0:
                movie_title = ''
            else:
                movie_title = movie_title[0]
            # 获取电影评分
            movie_score = li.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]

            # 获取电影的评价人数
            movie_number = li.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0]
            movie_number = re.sub('\D', '', movie_number)

            # 获取导演和主演
            movie_message = li.xpath('./div/div[2]/div[2]/p[1]/text()[1]')[0]
            movie_message = re.sub('\s', '', movie_message)
            movie_splits = movie_message.split(':')
            # print(movie_splits)
            # 获取电影主演
            movie_actor = movie_splits[-1]
            # print(movie_actor)

            # 获取导演
            movie_dire = movie_splits[1]
            movie_dire = movie_dire.split("主演")
            movie_dire = movie_dire[0]
            # print(movie_dire)

            # 获取电影详情信息
            movie_details = li.xpath('./div/div[2]/div[2]/p[1]/text()[2]')[0]
            movie_details = re.sub('\s', '', movie_details)

            # 按照/进行切分获取电影相关信息
            movie_details = movie_details.split('/')

            # 获取电影发行时间
            movie_reladate = movie_details[0]

            # 获取电影发行国家
            movie_country = movie_details[1]
            # 获取电影的类型
            movie_type = movie_details[-1]

            # 实例化一个item对象
            item = SampleItem()

            # 将解析的数据封装到实例化对象
            item['movie_ranking'] = movie_ranking
            item['movie_name'] = movie_name
            item['movie_title'] = movie_title
            item['movie_score'] = movie_score
            item['movie_number'] = movie_number
            item['movie_actor'] = movie_actor
            item['movie_dire'] = movie_dire
            item['movie_reladate'] = movie_reladate
            item['movie_country'] = movie_country
            item['movie_type'] = movie_type


            yield item

            for i in range(25, 256, 25):
                url = f'http://movie.douban.com/top250?start={i}&filter='.format(i)
                yield scrapy.Request(url=url, callback=self.parse)

