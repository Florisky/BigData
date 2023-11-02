# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SampleItem(scrapy.Item):
    # define the fields for your item here like:
    # Name = scrapy.Field()
    movie_name = scrapy.Field()
    movie_title = scrapy.Field()
    movie_ranking = scrapy.Field()
    movie_score = scrapy.Field()
    movie_number = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_dire = scrapy.Field()
    movie_reladate = scrapy.Field()
    movie_country = scrapy.Field()
    movie_type = scrapy.Field()

