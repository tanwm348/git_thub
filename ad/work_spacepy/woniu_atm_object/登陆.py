from woniu_atm.mysql import*
from woniu_atm_object.person import Person


def login():

     while True:

         usname = input("请输入账号")
         password = input("请输入密码")
         sql5 = "select * from woniu_atm where username ='%s'"%(usname)
         # sql55 = "select num from woniu_atm where username ='%s'"%(usname)
         source = select(sql5)
         # num = select(sql55)
         if len(source) ==0:
            print("给用户不存在")

         elif str(source[0][1])==password:
                if source[0][4]>2:
                    print("你的账户已被锁定,请解锁后再来操作")
                    return False

                else:
                    print("登陆成功")
                    print("欢迎%s"%(usname))
                    per = Person(source[0][0],source[0][1],source[0][2])


                    return per

         else:
            print("登陆失败")
            num=source[0][4]+1
            sql555 = "update woniu_atm set num = '%d' where username = '%s'"%(num,usname)
            change_mysql(sql555)

