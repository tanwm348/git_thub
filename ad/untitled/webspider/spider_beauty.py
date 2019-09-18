from bs4 import BeautifulSoup
import lxml,requests


#发起请求并解析响应内容
res = requests.get("http://woniuxy.com/note")
countent = res.text



#实例化BeautifulSoup对象
soup = BeautifulSoup(countent,"lxml")
# print(soup.prettify())

#匹配
#参数 name:标签名称 kwargs：属性(id,class)
div_data = soup.find_all("div", class_="info")
div_data1 = soup.find_all("div",class_ = "title")
div_data2 = soup.find_all("a",href = "/note/342")
# print(div_data)

# print(div_data2)
# print(div_data1)
# for data in div_data:
#     pass
    # print(data)
    # print(data.text)

#
#
url_list = []
for data1 in div_data1:
    # print(data1.a["href"])
    # print(data1.text)

    url =  "http://woniuxy.com"+data1.a["href"]
    url_list.append((url,data1.text))
    with open("result.txt","a",encoding="utf8") as f:
        f.write(url+","+data1.text+"\n")
print(url_list,"\n")




# for data2 in div_data2:
#
#     print(data2.text)
#     print(data2["href"])


