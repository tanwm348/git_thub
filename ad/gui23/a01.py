# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()  #对浏览器实例化
# driver.get("http://www.baidu.com")   #输入网址
# driver.find_element_by_id("kw").send_keys("陈奕迅")#对搜索输入要搜索的内容
# time.sleep(2)
# # driver.find_element_by_id("kw").clear() #清空输入内容
# driver.find_element_by_id("su").click() #点击
# time.sleep(2)
# s1 = driver.find_element_by_class_name("nums_text").text #获取该元素的文本
# if s1 == "百度为您找到相关结果约33,000,000个":
#     print("测试成功")
# else:
#     print("测试失败")
# #
# driver.close()#关闭所有
# driver.quit()#关闭当前

#对元素的操作:get  send_keys click  clear text close quit










from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get("http://localhost/Agileone/Agileone_1.2/index.php/")
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("admin")
driver.find_element_by_id("login").click()
time.sleep(2)
l1=driver.find_element_by_link_text("英文版").text
if l1 == "英文版":
    print("登陆测试成功")
else:
    print("登陆测试失败")



def fuser():
    driver.find_element_by_link_text("注销").click()
    driver.find_element_by_id("username").send_keys("aaa")
    driver.find_element_by_id("password").send_keys("admin")
    driver.find_element_by_id("login").click()
    l2 = driver.find_element_by_class_name("login-message").text
    time.sleep(2)
    if l2 == "出错啦: 找不到该用户名 ...":
        print("账户输入错误测试成功")
    else:
        print("账户输入错误测试失败")


def fpwd():
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("123")
    driver.find_element_by_id("login").click()
    l2 = driver.find_element_by_class_name("login-message").text
    time.sleep(2)
    if l2 == "出错啦: 密码输入错误 ...":
        print("密码输入错误测试成功")
    else:
        print("密码输入错误测试失败")


def ggg():
    time.sleep(2)
    driver.find_element_by_partial_link_text("公告管理").click()
    l3 = driver.find_element_by_partial_link_text("公告管理").text
    if l3 == "※ 公告管理 ※":
        print("跳转公告管理测试成功")
        driver.find_element_by_id("headline").send_keys("你是谁")
        driver.find_element_by_xpath("//*[@id='add]").click()
        l4 = driver.find_element_by_css_selector("#msg").text
        print(l4)



    else:
        print("跳转公告管理测试成功失败")


ggg()
#
# fuser()
# fpwd()



from selenium import webdriver
# import time


# driver = webdriver.Firefox()
# driver.get("http://localhost/Agileone/Agileone_1.2/index.php/")
# # driver.find_element_by_tag_name("input").send_keys("admin")
# # driver.find_elements_by_tag_name("input")[2].send_keys("admin") #在第3个input输入
#
# #id name  class_name  tag_name xpath css_selector  partial_link_text  link_text
# #id --> name --> xpath --> partial_link.text / css_selector
# driver.find_element("id","username").send_keys("admin")
#
#
#
# driver = webdriver.Firefox()
# driver.get("http://localhost/Agileone/Agileone_1.2/index.php/")
# driver.find_element_by_css_selector("#username").send_keys("admin")
# driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
