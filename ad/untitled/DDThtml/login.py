import requests
import json
import random

# url = "http://localhost/job/uploads/login/index.php?c=loginsave"
# body = {"act_login":"0","username":"liulu","password":"123456","loginname":"0","authcode":"","geetest_challenge":"","geetest_validate":""}
# headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
# session = requests.session()
# res = session.post(url = url,data = body,headers = headers)
# # cookie = res.cookies
# res1 =json.loads(res.text)
# # print(res1)
#
#
#
# url = "http://localhost/job/uploads/index.php?m=subscribe"
# body = {"type":1,"job1":"45","job1_son":"102","job_post":"809","provinceid":"2","cityid":"","three_cityid":"",
#         "minsalary":3,"maxsalary":4,"cycle_time":3,"email":"794513906@126.com","time":1,"sid":"","submit":"订阅"}
#
# headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
# # session = requests.session()
# res2 = session.post(url = url,data = body,headers = headers)
# print(res2.text)
# res2 =json.dumps(res1.text)
# li1 =res1.text
# print(li1)
# li2 = []
# for i in li1:
#     if u"\u4e00" <= i <= u'\u9fff':
#        li2.append(i)
#        # print(li2)
#
#
# print((li2),type((li2)))
# if "信息更新成功" in res1.text:
#     print(1)
#
#
#
#
# # print(type(res1.text),res1.text)
#
# print("哈"*100)
num = random.randint(0,100000)
# num = "???"
url = "http://localhost/job/uploads/index.php?m=register&c=regsave"
body = {"username":"","password":"123456","unit_name":"公司%s"%(num),"usertype":2,"linkman": "%s"%(num),"codeid":1}
headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
session = requests.session()
res = session.post(url = url,data = body,headers = headers)
# cookie = res.cookies
res1 =json.loads(res.text)
print(res1)