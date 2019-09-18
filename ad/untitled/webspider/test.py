import re

import requests
from bs4 import BeautifulSoup




#发起请求并解析响应内容
res = requests.post("http://woniuxy.com/train")
countent = res.text
# print(countent)
#实例化BeautifulSoup对象
soup = BeautifulSoup(countent,"lxml")

# print(soup.prettify())


div_data = soup.find_all("div", class_="info")
div_data1 = soup.find_all("div",class_ = "title")
div_data2 = soup.find_all("a",href = "/note/342")

# #发起请求并解析响应内容
# res = requests.get("http://woniuxy.com/note")
# countent = res.text
#
#
#
# #实例化BeautifulSoup对象
# soup = BeautifulSoup(countent,"lxml")
# # print(soup.prettify())
# matches = soup.find_all(name =["img","a"] )#匹配 图片和a标签
# # matches = soup.find_all(re.compile("b") ) #匹配所有b相关
# matches = soup.find_all(class_ =["b","a"])
matches = soup.find_all("div",class_="teach-box text-center")
print(matches)

