from appium import webdriver
import time

#配置信息
desired_caps={}
desired_caps['platformName'] = 'Android'#平台名称
desired_caps['platformVersion'] = '6.0.1'#平台版本
desired_caps['deviceName'] = 'Android'#设备名称
desired_caps['appPackage'] = 'com.mobivans.onestrokecharge'#记账包名
desired_caps['appActivity'] = 'com.mobivans.onestrokecharge.activitys.BootActivity'#启动记账activity

desired_caps['udid'] = '127.0.0.1:7555'#设备唯一标识
desired_caps['noReset'] = True #不重置APP状态



desired_caps['noReset'] = True #不重置APP状态

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)#APP启动实例化

#支出
def qiong():
    time.sleep(1)
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/alert_tv_cancel").click()#下次吧
    time.sleep(1)
    # driver.find_element_by_id("com.mobivans.onestrokecharge:id/account_btn_guide").click()
    driver.find_element_by_xpath('//*[@resource-id="com.mobivans.onestrokecharge:id/main_write1"]/android.widget.ImageView[1]').click()#记一笔
    time.sleep(1)
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/item_cate_image").click()#餐饮
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_1").click()#价钱1
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_5").click()#价钱2
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_finish").click()#完成

    driver.find_element_by_xpath('//*[@resource-id="com.mobivans.onestrokecharge:id/main_write1"]/android.widget.ImageView[1]').click()#记一笔
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/add_txt_In").click()#收入
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/item_cate_image").click()#工资
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_1").click()#价钱1
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_0").click()#价钱2
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_0").click()#价钱3
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_0").click()#价钱4
    driver.find_element_by_id("com.mobivans.onestrokecharge:id/keyb_btn_finish").click()#完成
    d1 = driver.find_element_by_id("com.mobivans.onestrokecharge:id/account_txt_pay").text#支出总数
    d2 = driver.find_element_by_id("com.mobivans.onestrokecharge:id/account_txt_income").text#收入总数
    d3 = driver.find_element_by_id("com.mobivans.onestrokecharge:id/account_txt_balance").text#结余
    # print(d1,d2,d3)
    if int(d2) - int(d1) == int(d3):
        print("测试成功")
    else:
        print("测试失败")


if __name__ == '__main__':
    qiong()