import threading
import random
#
# with open("./aa.txt","r",encoding="utf8") as f:
#  with open ("./aaa/cc.txt","w",encoding="utf8")as e:
#     a = f.read()
#     e.write(a)


# def addd():
#     for i in range(100000):
#         with open("ee.txt","a",encoding="utf8")as f:
#             f.write("哈")
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=addd)
#     t1.start()


# 猜拳游戏
# 定义 1 剪刀  2 : 石头  3 : 布
# 电脑生成一个 1 2 3 中的随机数
# 人输入拳头,  对比 谁输谁赢,   每次猜 5次 每次记录比分并且输出
# 封装到一个对象中


class dx():
    def __init__(self):

            self.r = 0
            self.p = 0
            self.count = int(input("请输入要猜的次数"))
            self.cqff()


    def  cqff(self):
            for i in range(self.count):
             print("这是第",i+1,"次")
             rob = random.randint(0,3)
             per = int(input("请输入拳头"))
             if (rob==2 and per == 1) or (rob==3 and per == 2) or (rob==1 and per == 3):
                print("你输了")
                self.r = self.r+1
             elif rob == per:
                 print("平局")

             else:
                 print("你赢了")
                 self.p = self.p+1

             print("当前比分为 机器人:你")
             print(self.r  ,":",  self.p)


dx()
#  人出拳
#             # 对比输赢  记录比分 记录到对象属性中
#
#             # 每次猜拳之后都输出一下当前比分
#         pass


