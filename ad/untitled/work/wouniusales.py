import requests

class woniu():
    def __init__(self):
       url = "http://192.168.40.115:8080/WoniuSales-20171128-V1.3-bin/user/login"
       body = {"username":"admin","password":"admin123","verifycode":"0000"}
       headers = {"Content-Type":"application/x-www-form-urlencoded"}
       session = requests.session()
       res = session.post(url = url,data = body,headers = headers)
       print(res.text)

    def test_batch_improm(self):

        upload = {"batchfile":("GB20190715.xls",open("D:/销售出库单-201901-Test1.xls","rb"))}
        url1 = "http://192.168.40.115:8080/WoniuSales-20171128-V1.3-bin/goods/upload?batchname=GB20190715"
        name1 = {"batchname":"GB20190715"}
        cookie = {"Cookie":"JSESSIONID=3A1E5FC22150FEF5A9B9612106E55E1F"}
        session = requests.session()
        res1 = session.post(url=url1,data=name1,files =upload)
        print(res1.text)
        if res1.text == "already-imported":
            print("测试成功")

        else:
            print("测试失败")

if __name__ == '__main__':

    wo = woniu()
    wo.test_batch_improm()