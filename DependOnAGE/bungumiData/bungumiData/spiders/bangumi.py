import scrapy
from lxml import etree
from ..items import SampleItem
import re

class BangumiSpider(scrapy.Spider):
    name = "bangumi"
    allowed_domains = ["www.agedm.org"]
    start_urls = ["https://www.agedm.org/rank"]

    def parse(self, response):
        page = response.text
        tree = etree.HTML(page)
        div_list = tree.xpath('//*[@id="rank_list_wrapper"]/div/div[2]/div/div[1]')
        for div in div_list:
             for child in div:
                 bangumiName =  child.xpath()

