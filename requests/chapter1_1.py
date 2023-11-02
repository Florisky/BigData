import requests

url = 'https://www.baidu.com/s'
resp = requests.get(url = url)

page = resp.text

print(page)

