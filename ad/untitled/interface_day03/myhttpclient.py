import  http.client
import random


class TestWoniu:
    def __init__(self):
        self.host = "localhost"
        self.port = 8080
        self.cookies = ""
        self.num = random.randint(200,10000000)

    def get_hone_page(self):
        #建立与服务器的连接(3次握手)
        con= http.client.HTTPConnection(self.host,self.port)

        #发起请求
        url = "/WoniuSales-20171128-V1.3-bin/"
        headers = {}
        con.request(method="GET",url = url)
        #获取响应
        res = con.getresponse()
        res = res.read().decode("utf8")
        print(res)
        if "米乐熊-进销存系统"in res:
            print("请求成功")
        else:
            print("请求失败")

        #四次挥手
        con.close()

    #登陆
    def logintrue(self):
        #post请求
        #三次握手--建立连接
        con= http.client.HTTPConnection(self.host,self.port)
        #发起请求
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        url1 = "/WoniuSales-20171128-V1.3-bin/user/login"
        body = 'username=admin&password=admin123&verifycode=0000'
        con.request(method="POST",url=url1,body=body,headers=headers)
        res = con.getresponse()
        cookies = res.getheader("Set-Cookie")#获取指定响应头的键值
        self.cookies = cookies.split(";")[0]

        # 获取响应正文
        res1 = res.read().decode("utf8")

        #断言
        if res1 == "login-pass":
            print("登陆测试成功")

        else:
            print("登陆测试失败")

        con.close()

    #输入错误用户名
    def loginfalse1(self):
        #post请求
        #三次握手--建立连接
        con= http.client.HTTPConnection(self.host,self.port)
        #发起请求
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        url1 = "/WoniuSales-20171128-V1.3-bin/user/login"
        body = "username=admin1&password=admin123&verifycode=0000"
        con.request(method="POST",url=url1,body=body,headers=headers)

        # 获取响应正文
        res1 = con.getresponse().read().decode("utf8")


        #断言
        if res1 == "login-fail":
            print("错误用户名测试成功")

        else:
            print("错误用户名测试失败")

        con.close()

    #输入错误密码
    def loginfalse2(self):
        #post请求
        #三次握手--建立连接
        con= http.client.HTTPConnection(self.host,self.port)
        #发起请求
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        url1 = "/WoniuSales-20171128-V1.3-bin/user/login"
        body = "username=admin&password=admin125&verifycode=0000"
        con.request(method="POST",url=url1,body=body,headers=headers)

        # 获取响应正文
        res1 = con.getresponse().read().decode("utf8")


        #断言
        if res1 == "login-fail":
            print("错误密码测试成功")

        else:
            print("错误密码测试失败")

        con.close()

    #用户名输入为空
    def loginfalse3(self):
        #post请求
        #三次握手--建立连接
        con= http.client.HTTPConnection(self.host,self.port)
        #发起请求
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        url1 = "/WoniuSales-20171128-V1.3-bin/user/login"
        body = "username=&password=admin123&verifycode=0000"
        con.request(method="POST",url=url1,body=body,headers=headers)

        # 获取响应正文
        res1 = con.getresponse().read().decode("utf8")


        #断言
        if res1 == "login-fail":
            print("用户名为空测试成功")

        else:
            print("用户名为空测试失败")

        con.close()

    #密码输入为空
    def loginfalse4(self):
        #post请求
        #三次握手--建立连接
        con= http.client.HTTPConnection(self.host,self.port)
        #发起请求
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        url1 = "/WoniuSales-20171128-V1.3-bin/user/login"
        body = "username=admin&password=&verifycode=0000"
        con.request(method="POST",url=url1,body=body,headers=headers)

        # 获取响应正文
        res1 = con.getresponse().read().decode("utf8")


        #断言
        if res1 == "login-fail":
            print("密码为空测试成功")

        else:
            print("密码为空测试失败")

        con.close()

    #新增
    def addtrue(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=张三&customerphone=%d&childsex=男&childdate=2019-07-10&creditkids=0&creditcloth=0"%(self.num)
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")
        if res=="add-successful":
            print("新增测试成功")
        else:
            print("新增测试失败")
        con.close()

    #输入存在的电话号码
    def addcase1(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=张三&customerphone=110&childsex=男&childdate=2019-07-10&creditkids=0&creditcloth=0"
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")
        if res=="already-added":
            print("输入存在号码测试成功")
        else:
            print("输入存在号码测试失败")
        con.close()

    #电话号码输入为空
    def addcase2(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=张三&customerphone=&childsex=男&childdate=2019-07-10&creditkids=0&creditcloth=0"
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")

        if res == "already-added":
            print("输入空号码测试成功")
        else:
            print("输入空号码测试失败")
        con.close()

    #电话号码输入21个1
    def addcase3(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=张三&customerphone=111111111111111111111&childsex=男&childdate=2019-07-10&creditkids=0&creditcloth=0"
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")

        if "500 Internal Server Error" in res:
            print("号码输入21个1测试成功")
        else:
            print("号码输入21个1测试失败")
        con.close()

    #会员昵称输入为空
    def addcase4(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=&customerphone=%d&childsex=男&childdate=2019-07-10&creditkids=0&creditcloth=0"%(self.num+1)
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")

        if res == "add-successful":
            print("会员昵称为空测试成功")
        else:
            print("会员昵称为空测试失败")
        con.close()

    #会员昵称输入11个哈
    def addcase5(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=哈哈哈哈哈哈哈哈哈哈哈&customerphone=%d&childsex=男&childdate=2019-07-10&creditkids=0&creditcloth=0"%(self.num+2)
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")

        if "500 Internal Server Error" in res:
            print("会员昵称输入11个哈测试成功")
        else:
            print("会员昵称输入11个哈测试失败")
        con.close()

    #母婴积分为空
    def addcase6(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=张三&customerphone=%d&childsex=男&childdate=2019-07-10&creditkids=&creditcloth=0"%(self.num+3)
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")

        if "500 Internal Server Error" in res:
            print("母婴积分为空测试成功")
        else:
            print("母婴积分为空测试失败")
        con.close()

    #母婴积分输入12个2
    def addcase7(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=张三&customerphone=%d&childsex=男&childdate=2019-07-10&creditkids=222222222222&creditcloth=0"%(self.num+4)
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")
        if "400" in res:
            print("母婴积分输入12个2测试成功")
        else:
            print("母婴积分为空测试失败")
        con.close()


     #童装积分为空
    def addcase8(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=张三&customerphone=%d&childsex=男&childdate=2019-07-10&creditkids=1&creditcloth="%(self.num+5)
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")

        if "500 Internal Server Error" in res:
            print("童装积分为空测试成功")
        else:
            print("童装积分为空测试失败")
        con.close()

    #童装积分输入12个2
    def addcase9(self):
        con= http.client.HTTPConnection(self.host,self.port)
        url2 = "/WoniuSales-20171128-V1.3-bin/customer/add"
        headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":self.cookies}
        body = "customername=张三&customerphone=%d&childsex=男&childdate=2019-07-10&creditkids=1&creditcloth=222222222222"%(self.num+6)
        con.request(method="POST",url=url2,body=body.encode(),headers=headers)
        res = con.getresponse().read().decode("utf8")
        if "400" in res:
            print("童装积分输入12个2测试成功")
        else:
            print("童装积分为空测试失败")
        con.close()


if __name__ == '__main__':
    tw = TestWoniu()
    tw.logintrue()#正确登陆
    tw.loginfalse1()#用户名错误
    tw.loginfalse2()#密码错误
    tw.loginfalse3()#用户名为空
    tw.loginfalse4()#密码为空

    tw.addtrue()#新增成功
    tw.addcase1()#输入已存在号码
    tw.addcase2()#输入空号码
    tw.addcase4()#会员昵称输入为空
    tw.addcase5()#会员昵称输入11个哈
    tw.addcase6() #母婴积分为空
    tw.addcase7()#母婴积分输入12个2
    tw.addcase8() #童装积分为空
    tw.addcase9()#童装积分输入12个2