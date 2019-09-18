from appium import webdriver
import time

#配置信息
desired_caps={}
desired_caps['platformName'] = 'Android'#平台名称
desired_caps['platformVersion'] = '6.0.1'#平台版本
desired_caps['deviceName'] = 'Android'#设备名称
# desired_caps['appPackage'] = 'com.person.voice'#表态包名
# desired_caps['appActivity'] = 'com.person.voice.ui.splash.SplashActivity'#启动表态activity
desired_caps['appPackage'] = 'com.miui.calculator'#计算机包名
desired_caps['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity'#启动计算机activity

desired_caps['udid'] = '127.0.0.1:7555'#设备唯一标识
desired_caps['noReset'] = True #不重置APP状态



desired_caps['noReset'] = True #不重置APP状态

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)#APP启动实例化



driver.find_element_by_id("com.miui.calculator:id/btn_8_s").click()
driver.find_element_by_id("com.miui.calculator:id/btn_mul_s").click()
driver.find_element_by_id("com.miui.calculator:id/btn_6_s").click()

driver.find_element_by_id("com.miui.calculator:id/btn_equal_s").click()
time.sleep(1)
a = driver.find_element_by_xpath("//*[@text='48']").text
print(a)
if a == "48":
    print("成功")
else:
    print("失败")

