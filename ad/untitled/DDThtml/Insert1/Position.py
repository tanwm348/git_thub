import requests
import json,random
import threading

class Position():
    def __init__(self):
        self.cookie1=""
        self.cookie2=""
        self.rand = random.randint(100,100000)


    #登陆
    def login(self):
        url = "http://localhost/job/uploads/login/index.php?c=loginsave"
        headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        data = {"act_login":0,"username":"腾讯","password":"123456","loginname":0,"authcode":"","geetest_challenge":"","geetest_validate":"" ,"geetest_seccode":""}
        res =requests.request("POST",url=url,headers=headers,data=data)
        self.cookie1 = res.cookies
        log=json.loads(res.text)
        # print(log)



    #发布职位
    def pos(self):
        for i in range(400):
            self.login()
            url = "http://localhost/job/uploads/member/index.php?c=jobadd&act=save"
            headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
            data = {"name":"测试","job_post":161,"provinceid":6,"cityid":77,"three_cityid":707,"days":30,"edate":"2019-09-12","minsalary":4,"maxsalary": 5,
                    "hy":35,"number":40,"exp":127,"report":54,"age":88,"sex":3,"edu":65,"marriage":72,"islink":1,"link_man":"","link_moblie":"","tblink":"",
                    "isemail":0,"email":"","submitBtn":"提交操作","jobcopy":"","state":"","save":"","description":" <p>啊啊啊</p>"}
            res =requests.request("POST",url=url,headers=headers,data=data,cookies= self.cookie1)


            # print(res.text)







     # 注册
    def register(self):
       url = "http://localhost/job/uploads/index.php?m=register&c=regsave"
       headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
       data = {"username":"阿"+"%s"%(self.rand),"password":"123456","usertype":"1","name":"0","codeid":"1"}
       res =requests.request("POST",url=url,headers=headers,data=data)
        # log=json.loads(res.text)
       self.cookie2=res.cookies

    #登陆
    def login1(self):

        url = "http://localhost/job/uploads/login/index.php?c=loginsave"
        headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        data = {"act_login":0,"username":"阿%s"%(self.rand),"password":"123456","loginname":0,"authcode":"","geetest_challenge":"","geetest_validate":"" ,"geetest_seccode":""}
        res =requests.request("POST",url=url,headers=headers,data=data)
        # self.cookie2 = res.cookies
        log=json.loads(res.text)
        # print(log)

    #发布简历
    def resume(self):
       # for i in range(100):


           rand = random.randint(10000000000,99999999999)#电话号码
           rand1 = random.choice([9,12,13,14,15,16,17,18,19])#学历
           rand2 = random.choice([18,19,20,21,100,22,101,23,24])#工作经验
           rand3 = random.choice([35,837,835,836,45,44,43,42,41,40,39,38,37,36,839])#行业
           # rand4 = random.choice([2,27,25,32,16,6,31,3,4,18,12,13,14,10,11,30,5,7,8,9,15,17,26,24,23,22,21,20,19,28,29,33,34,35])#省份
           rand5 = random.choice([57,58,59])#是否全职
           rand6 = random.choice([45,46,47,48,50,51])#到岗时间
           rand7 = random.choice([114,115,116])#求职状态

           rand9 = random.choice([1,2])#性别
       #
           data = {"uname":"小啊%s"%(self.rand),"sex":rand9,"birthday":"2019-08-12","living":"北京","edu":rand1,"exp":rand2,"telphone":"%s"%(rand),
                    "email":"","hy":"%s"%(rand3),"job_class":"108","name":"工程师","minsalary":"10000","maxsalary":"20000","provinceid":"2",
                    "citysid":"52","three_cityid":"","type":"%s"%(rand5),"report":"%s"%(rand6),"jobstatus":"%s"%(rand7),"submit":"保存","save":""}

           # print(data)
           url = "http://localhost/job/uploads/member/index.php?c=expect&act=add"
           headers = {"Content-Type": "application/x-www-form-urlencoded"}
           # data = {"uname":"小啊%s"%(self.rand),"sex":1,"birthday":"1990-01-01","living":"北京","edu":15,"exp":18,"telphone":"%s"%(rand),
           #          "email":"","hy":"35","job_class":"108","name":"工程师","minsalary":"10000","maxsalary":"20000","provinceid":"2",
           #          "citysid":"52","three_cityid":"","type":"57","report":"45","jobstatus":"116","submit":"保存","save":""}



           res =requests.post(url=url,headers=headers,data=data,cookies =self.cookie2)

           # print(res.text)

    def start(self):


        for i in range(1000):

             self.register()
             self.resume()
             self.pos()

if __name__ == '__main__':
    p=Position()
    # for i in range(50):
    #  t1 =threading.Thread(target=p.pos)
    #
    #  t1.start()
    #
    #  t1.join()







    for i in range(50):
            p = Position()

            t2 =threading.Thread(target=p.start)
            t2.start()
            t2.join()
