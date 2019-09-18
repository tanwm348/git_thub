import json

import requests



class KEdaoyun():
    def __init__(self):
        pass


    def test01(self):
        url = "http://localhost/kodexplorer4.40/?systemMember/getByName"
        data = {"name":"demo"}
        res = requests.post(url = url,data=data)

        if "可道云.资源管理器" in res.text:
            print("test01测试成功")
        else:
            print("test01测试失败")




    def test02(self):
        url = "http://localhost/kodexplorer4.40/?systemMember/getByName"
        data = {"name":"demo"}
        headers = {"Cookie":"HOST=http%3A//localhost/; APP_HOST=http%3A//localhost/kodexplorer4.40/; kodUserLanguage=zh-CN; "
                   "kodUserID=100; kodVersionCheck=check-at-1563179230; username=admin; password=admin123; PHPSESSID=308eb7c60c605c6db6312ea1c1675b5f;"
                   " KOD_SESSION_SSO=54e563995537d6dacde23871a16ceecc; KOD_SESSION_ID_be020=5680bb2fe5042ac67fe1f069289c4769"}
        res= requests.post(url=url,data=data,headers= headers)
        res1 = res.text
        # print(res1[8:12:1])
        # print(res.text)
        if res1[8:12:1] == "true":
              print("test02测试成功")

        else:
            print("失败")

    def test03(self):
        url = "http://localhost/kodexplorer4.40/?systemMember/getByName"
        data = {"name":"demo"}
        headers = {"Cookie":"kodUserID=100; HOST=http%3A//localhost/; APP_HOST=http%3A//localhost/kodexplorer4.40/;"
                  " kodUserLanguage=zh-CN; kodVersionCheck=check-at-1563179660; KOD_SESSION_SSO=0f7d6b822e91a0461e2b0d32d5c859e0; "
                  "KOD_SESSION_ID_be020=deb8982478db5bb61aa7c48c19b7c538"}
        res= requests.post(url=url,data=data,headers = headers)
        res1 = res.text
        print(res.text)
        if res1[8:13:1] == "false":
              print("test03测试成功")
        else:
            print("失败")


    def test04(self):
        url = "http://localhost/kodexplorer4.40//?user/loginSubmit&isAjax=1&getToken=1&name=admin&password=admin"
        res = requests.get(url = url)
        print(res.text)
        #字符串转字典
        token = json.loads(res.text)["data"]
        print(token)

        #获取demo用户的信息
        url1 = "http://localhost/kodexplorer4.40/?systemMember/getByName"
        data = {"name":"admin"}
        #放在cookie里
        # headers = {"Cookie":"accessToken=%s"%(token)}
        # print(headers)
        # res1 = requests.post(url=url1,data=data,headers=headers)
        # print(res1.text)

        #放在url上
        url2 = url1+"&accessToken=%s"%(token)
        res2 = requests.post(url=url2,data=data)
        print(res2.text)
        res3 = json.loads(res2.text)["code"]
        res3 = str(res3)
        if res3 == "True":
            print("测试成功")

        else:
            print(2)






if __name__ == '__main__':

    ke = KEdaoyun()
    # ke.test01()
    # ke.test02()
    # ke.test03()
    ke.test04()
