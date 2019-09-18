
# 题目：
# 警察局抓了a,b,c,d四名偷窃嫌疑犯，当中只有1个是小偷，审问结果如下：
# a说：“我不是小偷。”    a == 0
# b说：“c是小偷。”       c ==1
# d说：“c在冤枉人。”       d==0
# c说：“小偷肯定是d。”     d == 1
# 现在已经知道4个人中3人说的是真话，一个说的是假话，那么谁是小偷？

# 示：设4个变量a,b,c,d，为0时表示不是小偷，为1时表示是小偷，
# 用四重循环穷举a,b,c,d可能的取值的组合，对每一种组合判断其是否符合题目中给出的约束。



# a = 1
# b =5

# True 表示 1
# False 表示 0

# if ((a==1 ) + (b ==5)) == 2:
#     print(111)








for a in range(0, 2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                if   ((a == 0) + (b == 0 ) + (c == 0) + (d == 0) == 3) and  ((a == 0) + (c == 1)+ (d == 0)+(d == 1)) == 3:
                     print(a,b,c,d)


# 猜拳游戏
# 定义 1 剪刀  2 : 石头  3 : 布
# 电脑生成一个 1 2 3 中的随机数
# 人输入拳头,  对比 谁输谁赢,   每次猜 5次 每次记录比分并且输出
# 封装到一个对象中


# class 对象():
#     def __init__(self):
#         pass
#         # 调用猜拳的方法
#
#     def  猜拳方法(self):
#         # 请输入要猜次数
#         for i in range(num):
#             #电脑随机出拳
#             # 人出拳
#             # 对比输赢  记录比分 记录到对象属性中
#
#             # 每次猜拳之后都输出一下当前比分
#         pass

# 功能可以保存比分
# 可以比较分分数

# 1 剪刀     2 石头   3 布

# import random
# class Guess():
#     def __init__(self):
#         self.num = 0   #保存机器人的成绩
#         self.num1 = 0  #保存人的成绩
#         self.count = int(input("请问你要猜几次:"))
#         self.conGuess()
#     #猜拳
#     def conGuess(self):
#         for i in range(self.count):
#             print("第",i,"次猜拳开始:")
#             # 机器人出拳
#             rob = random.randint(1,3)
#             # 人出拳:
#             per = int(input("请出拳:"))
#             if (per == 1 and rob == 3)  or (per == 2 and rob == 1) or (per == 3 and rob == 2):
#                 print("恭喜恭喜")
#                 self.num1 = self.num1 + 1
#             elif per == rob:
#                 print("平局")
#             else:
#                 print("你输了")
#                 self.num = self.num + 1
#
#             print("机器人成绩:你的成绩")
#             print(self.num,"   :   ",self.num1)
#
# # print(random.randint(1,3))
#
#
#
# Guess()



# 多线程/单线程 分别写某个文件中  写入10万条数据, 然后计算各自所需要的时间




# 多线程/单线程写文件

# import threading,time
#
# def op(b,c):
#     for i in range(1000):
#         with open("a.txt","a",encoding="utf8") as f:
#             f.write(b+c+"\n")
#
# if __name__ == '__main__':
#     time.clock()
#     t = ""
#     for i in range(10):
#          t = threading.Thread(target=op,args=("这是第d%个线程",str(i)))
#          t.start()
#          # t.join() #不能写在这里, 后面的线程添加不了
#     t.join()
#     print(threading.currentThread())
#     print(time.clock())
#
#
# # def op1(b,c):
# #     for i in range(10000):
# #         with open("a.txt","a",encoding="utf8") as f:
# #             f.write(b+c+"\n")
# # time.clock()
# # op1("这是第d%个线程",str(1))
# # print(time.clock())
#
#


