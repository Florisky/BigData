import requests

url = 'https://www.wjut.edu.cn/'

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

resp = requests.get(url = url, headers = headers)

resp.encoding = "utf-8"

page = resp.text

with open('皖江工学院官网.html', 'w', encoding ='utf-8') as fp:
    fp.write(page);