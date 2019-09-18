import unittest
import requests


class login_html(unittest.TestCase):


    #正确登陆
    def test1(self):
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



    #用户名错误
    def test2(self):
        #post请求
        url = "http://localhost/Agileone/Agileone_1.2/index.php/common/login"
        body = {"username":"admin1","password":"admin","savalogin":"true"}
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        res = requests.request(method="POST",url = url,data = body,headers = headers)
        self.cookies = res.cookies
        print(self.cookies)
        #获取响应正文
        # result1 = res.content.decode("utf8")
        result1 = res.text


        if result1 == "user_invalid":
           print("登陆成功")
        else:
           print("登陆失败")


    #密码错误
    def test3(self):
        #post请求
        url = "http://localhost/Agileone/Agileone_1.2/index.php/common/login"
        body = {"username":"admin","password":"admin1","savalogin":"true"}
        headers = {"Content-Type":"application/x-www-form-urlencoded"}
        res = requests.request(method="POST",url = url,data = body,headers = headers)
        self.cookies = res.cookies
        print(self.cookies)
        #获取响应正文
        # result1 = res.content.decode("utf8")
        result1 = res.text

        if result1 == "password_invalid":
           print("登陆成功")
        else:
           print("登陆失败")





if __name__ == '__main__':
    pass