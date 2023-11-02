import requests

url = 'https://www.baidu.com/s?wd='
data = {
 'wd':'lyr'
}

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

resp = requests.get(url = url + data['wd'], headers = headers)

page = resp.text
website =  'xxx.html'
with open(website, 'w', encoding="utf-8") as fp:
 fp.write(page)