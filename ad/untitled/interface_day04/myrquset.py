import json
from interface_day04.mysql_select import *

import requests

class Aglieone():
    def __init__(self):
       self.cookies = ""

    def get_hone_page(self):
        # get请求
        res = requests.request(method="GET",url = "http://localhost/Agileone/Agileone_1.2/index.php" )

        #响应正文
        result = res.content.decode("utf8")


        #断言
        if "AgileOne - Welcome to Login" in result:
            print("访问首页成功")
        else:
            print("访问首页失败")


    def login(self):
        #post请求
        url = "http://localhost/Agileone/Agileone_1.2/index.php/common/login"
        body = {"username":"admin","password":"admin","savalogin":"true"}
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        res = requests.request(method="POST",url = url,data = body,headers = headers)
        self.cookies = res.cookies
        print(self.cookies)
        #获取响应正文
        # result1 = res.content.decode("utf8")
        result1 = res.text



        if result1 == "successful":
           print("登陆成功")
        else:
           print("登陆失败")


    def add(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/add"
       body = {"headline":"aa","content":"adsa","scope":"1","expireddate":"2019-10-09"}
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)

       if res.text.isalnum():
           print("新增成功")
       else:
           print("新增失败")


    #全为空
    def select1(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/query"
       body = {"content":"","noticeid":"","headline":"","creator":"","scope":"","expireddate":"" }
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)
       #获得查询内容
       str = res.text
       #数据库查询编号

       #把字符串转换成字典
       pystr = json.loads(str)
       return pystr

    #编号
    def select_notice(self):
       pystr = ao.select1()
       sql = "select max(noticeid) from notice"
       a = select(sql)
       pystr1 = int(pystr[0]["noticeid"])
       if pystr1 == a[0][0]:
           print("查询编号测试成功")
       else:
           print("查询编号测试失败")


    #标题
    def select_headline(self):
        pystr = ao.select1()

        sql = "select headline from notice  order by noticeid desc limit 0,1"
        a = select(sql)

        if pystr[0]["headline"] == a[0][0]:
            print("标题测试成功")
        else:
            print("标题测试失败")

    #内容
    def select_content(self):
        pystr = ao.select1()

        sql = "select content from notice  order by noticeid desc limit 0,1"
        a = select(sql)

        if pystr[0]["content"] == a[0][0]:
            print("内容测试成功")
        else:
            print("内容测试失败")


    #创建者
    def select_creator(self):
        pystr = ao.select1()

        sql = "select creator from notice  order by noticeid desc limit 0,1"
        a = select(sql)
        # print(a[0][0])
        if pystr[0]["creator"] == a[0][0]:
            print("创建者测试成功")
        else:
            print("创建者测试失败")


    #下拉列表
    def select_scope(self):
        pystr = ao.select1()

        sql = "select scope from notice  order by noticeid desc limit 0,1"
        a = select(sql)

        pystr1 = int(pystr[0]["scope"])

        if pystr1 == a[0][0]:
            print("下拉列表测试成功")
        else:
            print("下拉列表测试失败")



    #编号为空
    def notice_null(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/query"
       body = {"content":"aa","noticeid":"","headline":"aa","creator":"admin","scope":"1","expireddate":"2019-10-9" }
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)
       #获得查询内容
       str = res.text
       #数据库查询编号

       #把字符串转换成字典
       pystr = json.loads(str)
       return pystr

    #编号
    def select_notice1(self):
       pystr = ao.notice_null()
       sql =  "select*from notice where content = 'aa'"
       a = select(sql)
       print(a)
       pystr1 = int(pystr[0]["noticeid"])
       print(pystr1)
       if pystr1 == a[0][0]:
           print("查询编号为空编号测试成功")
       else:
           print("查询编号为空编号测试失败")


    #标题
    def select_headline1(self):
        pystr = ao.notice_null()

        sql = "select*from notice where content = 'aa'"
        a = select(sql)

        if pystr[0]["headline"] == a[0][1]:
            print("查询编号为空标题测试成功")
        else:
            print("查询编号为空标题测试失败")

    #内容
    def select_content1(self):
        pystr = ao.notice_null()

        sql =  "select*from notice where content = 'aa'"
        a = select(sql)

        if pystr[0]["content"] == a[0][2]:
            print("查询编号为空内容测试成功")
        else:
            print("查询编号为空内容测试失败")

     #标题为空
    def headline_null(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/query"
       body = {"content":"333","noticeid":"125","headline":"","creator":"admin","scope":"1","expireddate":"2019-10-9" }
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)
       #获得查询内容
       str = res.text
       #数据库查询编号

       #把字符串转换成字典
       pystr = json.loads(str)
       return pystr

    #编号
    def select_notice2(self):
       pystr = ao.headline_null()
       sql = "select*from notice where noticeid = '125'"
       a = select(sql)
       print(a)
       pystr1 = int(pystr[0]["noticeid"])
       print(pystr1)
       if pystr1 == a[0][0]:
           print("查询标题为空编号测试成功")
       else:
           print("查询标题为空编号测试失败")


    #标题
    def select_headline2(self):
        pystr = ao.headline_null()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["headline"]
        if pystr1 == a[0][1]:
            print("查询标题为空标题测试成功")
        else:
            print("查询标题为空标题测试失败")

    #内容
    def select_content2(self):
        pystr = ao.headline_null()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["content"]
        if pystr1 == a[0][2]:
            print("查询标题为空内容测试成功")
        else:
            print("查询标题为空内容测试失败")



     #内容为空
    def content_null(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/query"
       body = {"content":"","noticeid":"125","headline":"333","creator":"admin","scope":"1","expireddate":"2019-10-9" }
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)
       #获得查询内容
       str = res.text
       #数据库查询编号

       #把字符串转换成字典
       pystr = json.loads(str)
       return pystr

    #编号
    def select_notice3(self):
       pystr = ao.content_null()
       sql = "select*from notice where noticeid = '125'"
       a = select(sql)
       pystr1 = int(pystr[0]["noticeid"])
       if pystr1 == a[0][0]:
           print("查询内容为空编号测试成功")
       else:
           print("查询内容为空编号测试失败")


    #标题
    def select_headline3(self):
        pystr = ao.content_null()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["headline"]
        if pystr1 == a[0][1]:
            print("查询内容为空标题测试成功")
        else:
            print("查询内容为空标题测试失败")

    #内容
    def select_content3(self):
        pystr = ao.content_null()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["content"]
        if pystr1 == a[0][2]:
            print("查询内容为空内容测试成功")
        else:
            print("查询内容为空内容测试失败")


     #创建者为空
    def creator_null(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/query"
       body = {"content":"333","noticeid":"125","headline":"333","creator":"","scope":"1","expireddate":"2019-10-9" }
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)
       #获得查询内容
       str = res.text
       #数据库查询编号

       #把字符串转换成字典
       pystr = json.loads(str)
       return pystr

    #编号
    def select_notice4(self):
       pystr = ao.creator_null()
       sql = "select*from notice where noticeid = '125'"
       a = select(sql)

       pystr1 = int(pystr[0]["noticeid"])

       if pystr1 == a[0][0]:
           print("查询内容为空编号测试成功")
       else:
           print("查询内容为空编号测试失败")


    #标题
    def select_headline4(self):
        pystr = ao.creator_null()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["headline"]
        if pystr1 == a[0][1]:
            print("查询内容为空标题测试成功")
        else:
            print("查询内容为空标题测试失败")

    #内容
    def select_content4(self):
        pystr = ao.creator_null()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["content"]
        if pystr1 == a[0][2]:
            print("查询内容为空内容测试成功")
        else:
            print("查询内容为空内容测试失败")



     #过期日期为空
    def expireddate_null(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/query"
       body = {"content":"333","noticeid":"125","headline":"333","creator":"admin","scope":"1","expireddate":"" }
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)
       #获得查询内容
       str = res.text
       #数据库查询编号

       #把字符串转换成字典
       pystr = json.loads(str)
       return pystr

    #编号
    def select_notice5(self):
       pystr = ao.expireddate_null()
       sql = "select*from notice where noticeid = '125'"
       a = select(sql)
       pystr1 = int(pystr[0]["noticeid"])
       if pystr1 == a[0][0]:
           print("查询过期日期为空编号测试成功")
       else:
           print("查询过期日期为空编号测试失败")


    #标题
    def select_headline5(self):
        pystr = ao.expireddate_null()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["headline"]
        if pystr1 == a[0][1]:
            print("查询过期日期为空标题测试成功")
        else:
            print("查询过期日期为空标题测试失败")

    #内容
    def select_content5(self):
        pystr = ao.expireddate_null()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["content"]
        if pystr1 == a[0][2]:
            print("查询过期日期为空内容测试成功")
        else:
            print("查询过期日期为空内容测试失败")



      #范围为空
    def scope_null(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/query"
       body = {"content":"adsa","noticeid":"131","headline":"aa","creator":"admin","scope":"0","expireddate":"2019-10-9" }
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)
       #获得查询内容
       str = res.text
       #数据库查询编号

       #把字符串转换成字典
       pystr = json.loads(str)
       return pystr

    #编号
    def select_notice6(self):
       pystr = ao.scope_null()
       sql = "select*from notice where noticeid = '131'"
       a = select(sql)
       print(a[0][5])
       pystr = int(pystr[0]["totalRecord"])

       if pystr < a[0][5]:
           print("查询范围为空编号测试成功")
       else:
           print("查询范围为空编号测试失败")




    #多参
    def dc(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/query"
       body = {"content":"333","noticeid":"125","headline":"333","creator":"admin","scope":"1","expireddate":"2019-10-9","aum":"1"}
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)
       #获得查询内容
       str = res.text
       #数据库查询编号

       #把字符串转换成字典
       pystr = json.loads(str)
       return pystr

    #编号
    def select_notice7(self):
       pystr = ao.dc()
       # print(pystr)
       sql = "select*from notice where noticeid = '125'"
       a = select(sql)
       pystr1 = int(pystr[0]["noticeid"])
       if pystr1 == a[0][0]:
           print("查询多参编号测试成功")
       else:
           print("查询多参编号测试失败")


    #标题
    def select_headline7(self):
        pystr = ao.dc()
        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["headline"]
        if pystr1 == a[0][1]:
            print("查询多参标题测试成功")
        else:
            print("查询多参标题测试失败")

    #内容
    def select_content7(self):
        pystr = ao.dc()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["content"]
        if pystr1 == a[0][2]:
            print("查询多参内容测试成功")
        else:
            print("查询多参内容测试失败")

    #少参
    def sc(self):
       url = "http://localhost/Agileone/Agileone_1.2/index.php/notice/query"
       body = {"content":"333","noticeid":"125","headline":"333","creator":"admin","scope":"1"}
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       res = requests.request(method="POST",url = url,headers = headers,data = body,cookies = self.cookies)
       #获得查询内容
       str = res.text
       #数据库查询编号

       #把字符串转换成字典
       pystr = json.loads(str)
       return pystr

    #编号
    def select_notice8(self):
       pystr = ao.sc()
       # print(pystr)
       sql = "select*from notice where noticeid = '125'"
       a = select(sql)
       pystr1 = int(pystr[0]["noticeid"])
       if pystr1 == a[0][0]:
           print("查询少参参编号测试成功")
       else:
           print("查询少参编号测试失败")


    #标题
    def select_headline8(self):
        pystr = ao.sc()
        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["headline"]
        if pystr1 == a[0][1]:
            print("查询少参标题测试成功")
        else:
            print("查询少参标题测试失败")

    #内容
    def select_content8(self):
        pystr = ao.sc()

        sql = "select*from notice where noticeid = '125'"
        a = select(sql)
        pystr1 = pystr[0]["content"]
        if pystr1 == a[0][2]:
            print("查询少参内容测试成功")
        else:
            print("查询少参内容测试失败")





if __name__ == '__main__':
    ao = Aglieone()
    ao.login()#登陆

    ao.add()#新增
    # ao.select_notice()#标题
    # ao.select_headline()#标题
    # ao.select_content()#内容
    # ao.select_creator()#创建者
    # ao.select_scope()#下拉列表
    #
    # #编号为空
    # ao.select_notice1()#查询编号为空编号
    # ao.select_headline1()#查询编号为空标题
    # ao.select_content1()#查询编号为空
    #
    # #标题为空
    # ao.select_notice2()#查询标题为空编号
    # ao.select_headline2()#查询标题为空标题
    # ao.select_content2()#查询标题为空内容
    #
    # #内容为空
    # ao.select_notice3()#查询内容为空编号
    # ao.select_headline3()#查询内容为空标题
    # ao.select_content3()#查询内容为空内容
    #
    # #创建者为空
    # ao.select_notice4()#查询创建者为空编号
    # ao.select_headline4()#查询创建者为空标题
    # ao.select_content4()#查询创建者为空内容
    #
    # #过期日期为空
    # ao.select_notice5()#查询过期为空编号
    # ao.select_headline5()#查询过期为空标题
    # ao.select_content5()#查询过期日期为空内容

    #范围为空
    # ao.select_notice6()#查询过期为空


    #多参
    # ao.select_notice7()#查询多参编号
    # ao.select_headline7()#查询多参标题
    # ao.select_content7()#查询多参内容
    #
    # #少参
    # ao.select_notice8()#查询少参编号
    # ao.select_headline8()#查询少参标题
    # ao.select_content8()#查询少参内容
    #
    #