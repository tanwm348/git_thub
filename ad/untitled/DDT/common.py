from DDThtml.until1 import *
import requests
import time





class common1():
    def __init__(self):
        self.countcg = 0
        self.countsb = 0



    def post(self,url1,body1,headers1):
        # url = "http://localhost:8080/WoniuSales-20171128-V1.3-bin/user/login"
        # body = {"username":"admin","password":"admin123","verifycode":"0000"}
        # headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        session = requests.session()
        # session.post(url=url,data=body,headers=headers)
        res=session.post(url=url1,data=body1,headers=headers1)
        result=[]
        text=res.text
        print(text)
        cod=res.status_code #状态码
        result.append(text)
        result.append(cod)

        # print(result)
        return result




    def get(self,url,body,headers):

        res=requests.request(method="POST",url=url,data=body,headers=headers)
        result=[]

        #返回响应状态码和响应正文的文本格式
        code = res.status_code
        result.append(code)
        result.append(res.text)
        return result


    def logincase(self,result,data):



        if result[1] == 200 and result[0] == data[8]:
                print("测试成功")
                self.countcg += 1

        else:
               print("测试失败")
               self.countsb += 1
        # report = Report("report1.txt")
        #
        # nowtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        # report.add_report("=============================用例开始执行==================================")
        # report.add_report("\n")
        # report.add_report("下面开始执行用例:蜗牛进销存login")
        # report.add_report("测试时间:%s---接口:%s---%s----执行成功"%(nowtime,data[2],data[1]))
        # report.add_report("用例url:%s"%(data[3]))
        # report.add_report("参数为:")
        # report.add_report("请求正文为:%s"%(data[7]))
        # report.add_report("预期结果:%s"%(data[8]))
        # report.add_report("实际结果:%s"%(result[0]))
        #
        #
        # report.add_report("执行次数为%s,成功%s,失败%s"%(self.countcg+self.countsb,self.countcg,self.countsb))
        # # ti = TestWoniu()
        # # time1 = ti.logintime()
        # # report.add_report(time1)
        # report.add_report("-------------------------------------------------------------------------")




    def addcase(self,result,data):
        report = Report("report1.txt")
        print(result[1],result[0])
        if result[1] == 200 and result[0] == data[8]:
                print("测试成功")
                self.countcg += 1

        else:
               print("测试失败")
               self.countsb += 1


        nowtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        report.add_report("=============================用例开始执行==================================")
        report.add_report("\n")
        report.add_report("下面开始执行用例:蜗牛进销存add")
        report.add_report("测试时间:%s---接口:%s---%s----执行成功"%(nowtime,data[2],data[1]))
        report.add_report("用例url:%s"%(data[3]))
        report.add_report("参数为:")
        report.add_report("请求正文为:%s"%(data[7]))
        report.add_report("预期结果:%s"%(data[8]))
        report.add_report("实际结果:%s"%(result[0]))

        report.add_report("执行次数为%s,成功%s,失败%s"%(self.countcg+self.countsb,self.countcg,self.countsb))
        # ti = TestWoniu()
        # time1 = ti.logintime()
        # report.add_report(time1)
        report.add_report("-------------------------------------------------------------------------")





if __name__ == '__main__':
    com = common1()





