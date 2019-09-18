'''
Cookie操作的方式
1.静态.复制粘贴
2.动态, http.client:res.getHeader["Set-cookie"]----返回的String split()
       resquests:res.cookie----返回的cookie jar
3.requests.session()

requests.request()
requests.get()
requests.post()


'''
import json

import requests
#实例化session对象
session = requests.session()
# url = "http://localhost/Agileone/Agileone_1.2/index.php/common/login"
url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/add"
body = {""}
headers = {"Content-Type":"application/x-www-form-urlencoded"}
cookie = {"JSESSIONID=63C58ACD9156AA6AE8774E9660671112"}
res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = cookie)
# res =session.post(url = url,data = body,headers = headers)
print(res.text)
str = res.text
       #数据库查询编号

       #把字符串转换成字典
pystr = json.loads(str)
print(pystr)
