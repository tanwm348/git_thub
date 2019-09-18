import requests

url = "https://httpbin.org/get"
#verify = False  表示不验证TLS证书
url1 ="http://httpbin.org/post"
res = requests.get(url = url,verify = False)
res1 =requests.post(url = url1,verify = False)
print(res.text)
print(res1.text)