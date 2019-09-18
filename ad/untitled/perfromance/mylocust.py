import pymysql
import requests
from locust import HttpLocust,TaskSet,task


#用户行为类
class Userbehavior(TaskSet):




    @task
    def home(self):
         self.client.get("/")


    # 每个虚拟用户都会去执行
    def on_start(self):
        print("start")
        # # requests.get==
        # self.client.get("/get")
        data = {"username":"admin","password":"admin123","verifycode":"0000"}
        res = self.client.post("/WoniuSales-20171128-V1.3-bin/user/login",data,catch_response = True)
        print(res.text)
        #设置检查点catch_response = True
        if res.text == "login-pass":
            res.success()#检查点
        else:
            res .failure("测试失败") #检查点




    def on_stop(self):
        print("stop")






  #task 修饰的是以个用户操作,只有被task修饰了locust才会执行




    # @task
    # def add(self):
    #
    #     data = {"customerphone":"8888"}
    #     res = self.client.post("/WoniuSales-20171128-V1.3-bin/customer/search",data,catch_response = True)
    #     print(res.text)
    #     if res.text == "":
    #
    #         res .failure("测试失败")
    #     else:
    #         res.success()


    @task
    def barcode(self):
        sql = "select barcode from goods"
        barcode = self.select(sql)

        data = {"barcode":"%s"%(barcode[0][0])}
        res = self.client.post("/WoniuSales-20171128-V1.3-bin/sell/barcode",data,catch_response = True)
        print(res.text)
        if res.text == "":
           res.failure("测试失败")
        else:
           res.success()





    @task
    def summary(self):
        sql ="select barcode from goods"
        data = ""




    def select(self,sql,database = "milor",num=-1):
     # a = admin()
     # print(a)

     con = pymysql.connect("127.0.0.1","root","123456",charset = "utf8")
     cur = con.cursor()
     cur.execute("use "+database)
     cur.execute(sql)
     if num == -1:
          a = cur.fetchall()
     else:
          a = cur.fetchmany(num)
     con.commit()
     cur.close()
     con.close()
     return a



class website(HttpLocust):
    task_set = Userbehavior
    # 最大最小思考时间
    max_wait = 3000
    min_wait = 1000




if __name__ == '__main__':
    pass