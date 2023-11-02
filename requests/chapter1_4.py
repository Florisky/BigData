import requests

url = 'https://img2.baidu.com/it/u=3220182263,4248330525&fm=253&fmt=auto&app=120&f=JPEG?w=800&h=500'

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

resp = requests.get(url = url, headers = headers)

jpg = resp.content

with open('芙莉莲.jpg', 'wb') as fp:
    fp.write(jpg)