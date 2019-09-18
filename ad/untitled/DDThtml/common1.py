import requests
from until1 import *
from html_report1 import *
import json


class common1():
    def __init__(self):
        self.countcg = 0
        self.countsb = 0
        self.ht = HtmlReport()






    def post(self,url1,body1,headers1,cookie):


        res=requests.request("POST",url=url1,data=body1,headers=headers1,cookies =cookie)
        result=[]

        text=res.text
        cod=res.status_code #状态码
        result.append(text)
        result.append(cod)
        self.cookie = res.cookies
        return result




    def get(self,url,body,headers):

        res=requests.request(method="POST",url=url,data=body,headers=headers)
        result=[]

        #返回响应状态码和响应正文的文本格式
        code = res.status_code
        result.append(code)
        result.append(res.text)
        return result

    # 登陆
    def logincase(self,result,data):

        # now_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        result1 =json.loads(result[0])
        data1 = json.loads(data[8])
        # print(data)
        # print(result1)

        if data1 == result1 and result[1] == 200:
                print("登陆测试成功")
                self.countcg += 1

                # # print(data[2],type(data[2]),str(data[0]),type(str(data[0])),data[1],type(data[1]),data[8],type(data[8]),)
                # self.ht.write_data_to_db("v2.0","接口测试",data[2],str(int(data[0])),data[1],"成功","无","无","2019")
                # self.ht.generate_report("v2.0")


        else:
               print("登陆测试失败")
               # self.ht.write_data_to_db("v2.0","接口测试",data[2],str(int(data[0])),data[1],"失败","无","无","2019")
               # self.ht.generate_report("v2.0")
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
        # report.add_report("预期结果:%s"%(data1))
        # report.add_report("实际结果:%s"%(result[0]))
        #
        #
        # report.add_report("执行次数为%s,成功%s,失败%s"%(self.countcg+self.countsb,self.countcg,self.countsb))
        # # ti = TestWoniu()
        # # time1 = ti.logintime()
        # # report.add_report(time1)
        # report.add_report("-------------------------------------------------------------------------")



    #简历编辑
    def compilecase(self,result,data):

        # print(result[0])
        # print(data[8])
        #

        if data[8] == result[0] and result[1] == 200:
                print("学历编辑测试成功")
                self.countcg += 1

        else:
               print("学历编辑测试失败")
               self.countsb += 1


        # nowtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        # report.add_report("=============================用例开始执行==================================")
        # report.add_report("\n")
        # report.add_report("下面开始执行用例:蜗牛进销存add")
        # report.add_report("测试时间:%s---接口:%s---%s----执行成功"%(nowtime,data[2],data[1]))
        # report.add_report("用例url:%s"%(data[3]))
        # report.add_report("参数为:")
        # report.add_report("请求正文为:%s"%(data[7]))
        # report.add_report("预期结果:%s"%(data1))
        # report.add_report("实际结果:%s"%(result[0]))
        #
        # report.add_report("执行次数为%s,成功%s,失败%s"%(self.countcg+self.countsb,self.countcg,self.countsb))
        # # ti = TestWoniu()
        # # time1 = ti.logintime()
        # # report.add_report(time1)
        # report.add_report("-------------------------------------------------------------------------")

    #订阅
    def subscribecase(self,result,data,email_ex, email_sql):
          # print(email_sql,type(email_sql))
          # print(email_ex,type(email_ex))

            if "订阅设置成功，请认证邮箱！" in result[0] and result[1] == 200 and email_ex == email_sql[0][0]:
                print("订阅测试成功")
                self.countcg += 1

            else:
               print("订阅测试失败")
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
            # report.add_report("预期结果:%s"%(data1))
            # report.add_report("实际结果:%s"%(result[0]))
            #
            #
            # report.add_report("执行次数为%s,成功%s,失败%s"%(self.countcg+self.countsb,self.countcg,self.countsb))
            # # ti = TestWoniu()
            # # time1 = ti.logintime()
            # # report.add_report(time1)
            # report.add_report("-------------------------------------------------------------------------")
            #

    #个人用户注册
    def registe_pucase(self,result,data):

        result1 =json.loads(result[0])
        data1 = json.loads(data[8])
        # print(result,data[8])

        if result1 == data1 and result[1] == 200:

            print("个人注册成功")

        else:
            print("个人注册失败")
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
        # report.add_report("预期结果:%s"%(data1))
        # report.add_report("实际结果:%s"%(result[0]))
        #
        #
        # report.add_report("执行次数为%s,成功%s,失败%s"%(self.countcg+self.countsb,self.countcg,self.countsb))
        # ti = TestWoniu()
        # time1 = ti.logintime()
        # report.add_report(time1)
        # report.add_report("-------------------------------------------------------------------------")



    #企业用户注册
    def registe_eucase(self,result,data):

        result1 =json.loads(result[0])
        data1 = json.loads(data[8])

        if result1 == data1 and result[1] == 200:

            print("企业注册成功")

        else:

            print("企业注册失败")

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
        # report.add_report("预期结果:%s"%(data1))
        # report.add_report("实际结果:%s"%(result[0]))
        #
        #
        # report.add_report("执行次数为%s,成功%s,失败%s"%(self.countcg+self.countsb,self.countcg,self.countsb))
        # # ti = TestWoniu()
        # # time1 = ti.logintime()
        # # report.add_report(time1)
        # report.add_report("-------------------------------------------------------------------------")




