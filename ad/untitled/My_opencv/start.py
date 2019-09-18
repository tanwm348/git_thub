import os
import random
from My_opencv.image_frame import *


def start():
        execute = ("start /b D:\woniu\Software\firefox.exe https://www.woniuxy.com")

        # 启动应用程序  start/b-不阻塞当前线程 不影响其他操作
        os.system("start/b %s"%(execute))

        st = Image_Frame1()
        st.sele()
        st.open()

        # for i in range(count):
        #     num = random.randint(0,5)
        #     num1 = random.randint(10,100)
        #     if num == 1:
        #         lc = st.left_click()
        #         self.report("id:%d,坐标:%s,鼠标操作:左键单击"%(num1,lc))
        #
        #     elif num == 2:
        #         dc = st.left_double_click()
        #         self.report("id=%d,坐标=%s,操作=左键双击"%(num1,dc))
        #
        #     elif num == 3:
        #         rc = st.left_click()
        #         self.report("id=%d,坐标=%s,操作=右键点击"%(num1,rc))
        #
        #     elif num == 4:
        #         ek = self.enter_key()
        #         ek1 = ek[0]
        #         ek2 = ek[1]
        #         self.report("id=%d,坐标=%s,操作:键盘按了%s键"%(num1,ek1,ek2))
        #
        #     elif num == 5:
        #         ist = self.input_string()
        #         ist1 = ist[0]
        #         ist2 = ist[1]
        #         self.report("id=%d,坐标=%s,操作=键盘输入%s"%(num1,ist1,ist2))


if __name__ == '__main__':
    start()