import os
import time
import uiautomation


def calc():
    os.system("start/b calc.exe")
    #找到计算器窗口
    # window = uiautomation.WindowControl(searchDepth=1,Name= "计算器")

    window = uiautomation.WindowControl(searchDepth=1,ClassName= "CalcFrame")

    # print(window)
    #判断窗口是否存在
    if window.Exists():
        print("找到计算器了")
        #置顶窗口
        window.SetTopmost(isTopmost=True)
        #
        # #最大化窗口
        # window.Maximize()

        #激活窗口(从任务栏点出来)
        window.SetActive()


        #输出应用当前坐标
        # print(window.BoundingRectangle)

        # rest = window.BoundingRectangle
        # x = [rest.left,rest.right]
        # y = [rest.bottom,rest.top]
        # print(x,y)



    time.sleep(1)
    botton7 = uiautomation.ButtonControl(searchDepth=4,Name = "7")
    botton7.Click()
    time.sleep(1)
    botton2 = uiautomation.ButtonControl(Name = "加")
    botton2.Click()
    time.sleep(1)
    botton4 = uiautomation.ButtonControl(Name = "4")
    botton4.Click()
    time.sleep(1)
    botton3 = uiautomation.ButtonControl(Name = "等于")
    botton3.Click()
    time.sleep(1)
    reslult = uiautomation.TextControl( AutomationId = "158")
    name = reslult.Name
    if int(name) == 11:
        print("测试成功")
        uiautomation.ButtonControl(Name = "关闭").Click()
    else:
        print("测试失败")


if __name__ == '__main__':
    calc()