from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/index.php?tn=monline_3_dg")
# driver.find_element_by_id("kw").click()
# driver.find_element_by_id("kw").send_keys("张学友")
# driver.find_element_by_id("su").click()
# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/h3/a").click()
# time.sleep(2)
# win = driver.current_window_handle #获取当前句柄(网站页面)
# wins = driver.window_handles #获取当前所有句柄(网站页面)
#
# # driver.switch_to.window(wins[-1]) #第一种方法
# time.sleep(2)
# for i in wins:#第二种方法
#     if i != win:
#         driver.switch_to.window(i)
#
# time.sleep(2)
# a1 = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/dl/dt/dl/dd[1]/h1").text
# print(a1)
#

time.sleep(2)
driver.find_element_by_id("kw").click()
driver.find_element_by_id("kw").send_keys("126")
# driver.find_element_by_id("su").click()
#
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/h3/a[1]").click()
# time.sleep(5)
# wins = driver.window_handles
# driver.switch_to.window(wins[-1])
# driver.find_element_by_id("switchAccountLogin").click()
#
# l = driver.find_element_by_xpath("//div/iframe")
# driver.switch_to.frame(l)
# time.sleep(2)
# driver.find_element_by_name("email").click()
# driver.find_element_by_name("email").send_keys("123")
# time.sleep(2)
# driver.find_element_by_name("password").click()
# driver.find_element_by_name("password").send_keys("234")




# time.sleep(2)
# driver.find_element_by_id("op_email3_username").click()
# driver.find_element_by_id("op_email3_username").send_keys("123")
# driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/div[1]/div/form/table/tbody/tr[2]/td[2]/span/input").click()
# driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/div[1]/div/form/table/tbody/tr[2]/td[2]/span/input").send_keys("456")
driver.find_element_by_id("su").send_keys(Keys.ENTER)