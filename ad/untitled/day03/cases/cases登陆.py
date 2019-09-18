from day03.common.loginmodel import *

login1 = login()
driver = login1.driver1()

#登陆
def lon():
    login1.username_name("admin")
    login1.password_pwd("admin")
    time.sleep(2)
    l1 = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[2]/a[5]").text
    if l1 == "注销":
        print("登陆测试成功")
    else:
        print("登陆测试失败")

#输入错账户名
def fusname():
    login1.username_name("aaa")
    login1.password_pwd("admin")
    time.sleep(2)
    l2 = driver.find_element_by_id("msg").text
    if l2 == "出错啦: 找不到该用户名 ...":
        print("输入错误用户名测试成功")

    else:
        print("输入错误用户名测试失败")

#输入错误密码
def fpwd():
    login1.username_name("admin")
    login1.password_pwd("123")
    time.sleep(2)
    l3 = driver.find_element_by_id("msg").text
    if l3 == "出错啦: 密码输入错误 ...":
        print("输入错误密码测试成功")

    else:
        print("输入错误密码测试失败")

#输入空账户名
def kusername():
    login1.username_name("")
    login1.password_pwd("admin")
    time.sleep(2)
    l4 = driver.find_element_by_id("msg").text
    if l4 == "出错啦: 用户名不能为空 ...":
        print("输入空用户名测试成功")

    else:
        print("输入空用户名测试失败")

#输入空密码
def kpwd():
    login1.username_name("admin")
    login1.password_pwd("")
    time.sleep(2)
    l5 = driver.find_element_by_id("msg").text
    if l5 == "出错啦: 密码输入为空 ...":
        print("输入空密码测试成功")

    else:
        print("输入空密码应提示密码输入为空")

#注销
def zx():
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[2]/a[5]").click()
    time.sleep(1)
    l6 = driver.find_element_by_id("username").text
    if l6 == "":
        print("注销测试成功")

    else:
        print("注销测试失败")


if __name__ == '__main__':
    fusname()
    fpwd()
    kusername()
    kpwd()
    lon()
    zx()
    #