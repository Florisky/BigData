from lxml import etree
import requests

url = "http://www.aqistudy.cn/historydata/"
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

resp = requests.get(url = url, headers = headers)
page = resp.text

tree = etree.HTML(page)
city_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')

for city in city_list:
    print(city)



