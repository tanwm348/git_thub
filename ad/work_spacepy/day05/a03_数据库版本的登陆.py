from Work.day5 import select
# operation = -1
#
while True:
#     print("欢迎使用atm,请输入你的选择,1.登陆,2,注册")
# if operation==1:
    username = input("请输入账号")
    password = input("请输入密码")
    sql5 = "select * from stu where sname ='%s'"%(username)
    source = select(sql5)
    # print(source)
    if len(source) ==0:
        print("输入错误")
    else:
       if str(source[0][2])==password:
        # print(source[0][2])
        print("登陆成功")
        break
       else:
           print("登陆失败")

# if operation==2:
#     newname = input("请输入账户名")
#     if newname != username:
#         newpassword= input("请输入密码")
#         sql6 = "insert into stu values(7,newname,newpassword)"
#         print("注册成功")
        # break
def atm_login():
    while True:
        # 1. 从页面接受用户名和密码
        print('如果需要退出请求输入:quit')
        user = input("用户名:")
        if user == "quit":
            break
        passwd =  input("密码:")
        # 2. 根据用户名去数据库中查询出对应的密码
        sql = "select * from woniu_atm where username ='%s'"%(user)
        source = select(sql)
        print(source)
        if len(source) == 0:
            print("兄弟, 没有这个人,请重新输入")
        else:
            print(source[0][1])
            if str(source[0][1]) == passwd:
                print("登录成功")
                break
            else:
                print("密码错误,请重新输入")
    print("程序运行结束")