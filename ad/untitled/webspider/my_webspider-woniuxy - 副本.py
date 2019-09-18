import os

import requests
import re
#发请求
res = requests.get("http://woniuxy.com/note")

content = res.text

# print(content)
#定义匹配规则
# regular ='<img src="(.+?)"'
# regular ='<img src="(.+?(png|jpg))"'
regular = '<img src="((.+?)png|jpg)"'
# regular ='<img src="(.+?)"'
url_list = []

#匹配
#参数pattern:正则表达式；string：要匹配的范围(res.text),网页html
matchs = re.findall(pattern=regular,string=content)
print(matchs)
for url in matchs:
    if url[0].startswith("http://"):
        url_list.append(url[0])
    else:
        print(url[0])
        newurl = "http://woniuxy.com"+url[0]
        url_list.append(newurl)

print(url_list)

#下载图片并保存



for url in url_list:
    print(url)
    #下载
    res =requests.get(url)
    #保存

    filename = url.split("/")[-1]
    print(filename)
    #判断文件是否已经存在
    if not os.path.exists("./img/"+filename):
        with open("./img/"+filename,"wb") as f:
            f.write(res.content)

    else:
        print("文件已存在")
