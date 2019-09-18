from bs4 import BeautifulSoup
import lxml,requests,xlwt
import re


#请求并解析
res=requests.get("http://www.woniuxy.com/train/teacher.html")
content=res.content
# print(content)

def report():
    #实例化对象
    soup=BeautifulSoup(content,"lxml")
    # print(soup.prettify())
    #获取内容
    matches=soup.find_all("div",class_="teacher-info")
    # len=len(matches)
    print(matches)

    for i in matches:
         w1 = i.h2.text.lstrip().rstrip()
         w2=  i.span.text.lstrip().rstrip()
         with open("report.txt","a",encoding="utf8") as f:
            f.write(w1+w2+"\n")
            f.write("\n")


def excel():
    pass




if __name__ == '__main__':
    report()
