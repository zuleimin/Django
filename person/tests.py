import requests
r=requests.get("http://www.baidu.com")
r.encoding='utf-8'
print(r.text)