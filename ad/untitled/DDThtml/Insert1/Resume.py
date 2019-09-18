import requests
import random,json
import threading


class resume():
    def __init__(self):
        self.random=random.randint(1111,2222222222011123)
        # session=requests.session()
        self.url='http://localhost/job/uploads/index.php?m=register&c=regsave'
        self.data={"username":"name%s"%(self.random),"password":"admin123","usertype":"1","name":"0","codeid":"1"}
        self.headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        res=requests.post(url=self.url,data=self.data,headers=self.headers)
        self.cookie=res.cookies
        self.cookie1=""

    def add_resume(self):
        aa=random.randint(1,10000000000000)
        phone=random.randint(18200000000,18299999999)
        url="http://localhost/job/uploads/member/index.php?c=expect&act=add"
        data={"uname":"%s"%(aa),"sex":"2","birthday":"1990-01-01","living": "home", "edu": "12",
              "exp": "21", "telphone": "%s"%(phone),"email": "","hy": "35",
              "job_class": "197", "name": "name", "minsalary": "7000",
              "maxsalary": "8000", "provinceid": "32",
              "citysid": "394", "three_cityid": "3328", "type": "58",
              "report": "48", "jobstatus": "115", "submit": "%E4%BF%9D%E5%AD%98","save": ""}
        headers={"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
        res = requests.post(url=url,data=data,headers=headers,cookies=self.cookie)
        print(res.text)


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
            self.login()
            url = "http://localhost/job/uploads/member/index.php?c=jobadd&act=save"
            headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
            data = {"name":"测试","job_post":161,"provinceid":6,"cityid":77,"three_cityid":707,"days":30,"edate":"2019-09-12","minsalary":4,"maxsalary": 5,
                    "hy":35,"number":40,"exp":127,"report":54,"age":88,"sex":3,"edu":65,"marriage":72,"islink":1,"link_man":"","link_moblie":"","tblink":"",
                    "isemail":0,"email":"","submitBtn":"提交操作","jobcopy":"","state":"","save":"","description":" <p>啊啊啊</p>"}
            res =requests.request("POST",url=url,headers=headers,data=data,cookies= self.cookie1)



if __name__ == '__main__':

    # def start1():
    #     for i in range(1000):
            aa=resume()
            aa.add_resume()
            # aa.pos()

    #
    # for j in range(50):
    #     j=threading.Thread(target=start1)
    #     j.start()
    #


