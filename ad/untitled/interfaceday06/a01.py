import requests


class aa():
    def __init__(self):
        pass




    def updata(self):
        cookie = {"Cookie":"JSESSIONID=F703FDB8A04854FA0D519197785690BA"}
        url1 = "http://192.168.40.164:8080/testdemo/user"
        data = {"id":36,"username":"蜗牛2","passwork":"123456"}
        res = requests.put(url=url1,data=data,cookies = cookie)
        print(res.text)
        if res.text == "success":
            print("测试成功")
        else:
            print("测试失败")


    def dele(self):
        cookie = {"Cookie":"JSESSIONID=F703FDB8A04854FA0D519197785690BA"}
        url1 = "http://192.168.40.164:8080/testdemo/user"
        data = {"id":43,"username":"蜗牛2","passwork":"123456"}
        res = requests.delete(url=url1)
        print(res.text)


    def getname(self):
        cookie = {"Cookie":"JSESSIONID=F703FDB8A04854FA0D519197785690BA"}
        url1 = "http://192.168.40.164:8080/testdemo/user"
        data = {"id":"","username":"","passwork":""}
        res = requests.get(url=url1,data=data,cookies = cookie)
        print(res.text)
        # print(type(res.text[3:5:1]))
        if res.text[3:5:1] == "id":
            print("测试成功")
        else:
            print("测试失败")



    def add(self):
        cookie = {"Cookie":"JSESSIONID=F703FDB8A04854FA0D519197785690BA"}
        headers = {"Content-Type":"application/json;charset=UTF-8"}
        url1 = "http://192.168.40.164:8080/testdemo/user"
        data = {"id":"","username":" bbbb","passwork":"1111"}
        res = requests.post(url=url1,data=data,headers = headers)
        print(res.text)



if __name__ == '__main__':
    a = aa()
    a.updata()
    a.dele() #
    # # a.getname()
    # a.add()