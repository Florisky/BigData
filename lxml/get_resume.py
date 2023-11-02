from lxml import etree
from os.path import exists
import requests
import os


if not exists('./rfiles'):
    os.mkdir('./rfiles')

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

for i in (2,4):
    url = f"https://sc.chinaz.com/jianli/free_{i}.html".format(i)
    resp = requests.get(url = url, headers = headers)
    # print(resp)
    page = resp.text
    # print(page)
    tree = etree.HTML(page)
    #
    list = tree.xpath('//div[@id="container"]/div[1]/a/@href')
    for j in list:
        resp1 = requests.get(url = j, headers = headers)
        resp1.encoding="utf-8"
        page1 = resp1.text
        tree1 = etree.HTML(page1)
        name = tree1.xpath('//div[@class="bgwhite"]/div[1]/h1/text()')[0]
        print(name)
        list1 = tree1.xpath('//div[@id="down"]/div[2]/ul/li/a/@href')[0]

        resp2 = requests.get(url = list1, headers = headers)
        content = resp2.content
        name += ".rar"
        path = "rfiles/" + name

        with open(path, 'wb') as fp:
            fp.write(content)

