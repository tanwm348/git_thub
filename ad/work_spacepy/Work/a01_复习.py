# 文件操作:
# 读写文件
# w:
# a:
# r:
# rb:
# wb:

'''
# 多任务
并行:
并发:

进程:
线程:


多进程:
多线程:

1. 创建多线程
2. join 主线程等待子线程结束后结束
3. 子线程跟随主线程的结束而结束
4. 常用的方法
5. 共享全局变量的问题
6. 使用锁解决共享全局变量问题
7. 使用 多进程解决上面的问题

8. 多进程的通信:  队列 (字句去封装一个队列 )













'''


# class dx():
#     def __init__(self):
#
#             self.r = 0
#             self.p = 0
#             self.count = int(input("请输入要猜的次数"))
#             self.cqff()
#
#
#     def  cqff(self):
#             for i in range(self.count):
#              print("这是第",i+1,"次")
#              rob = random.randint(0,3)
#              per = int(input("请输入拳头"))
#              if (rob==2 and per == 1) or (rob==3 and per == 2) or (rob==1 and per == 3):
#                 print("你输了")
#                 self.r = self.r+1
#              elif rob == per:
#                  print("平局")
#
#              else:
#                  print("你赢了")
#                  self.p = self.p+1
#
#              print("当前比分为 机器人:你")
#              print(self.r  ,":",  self.p)
#
#
#
# dx()











# 猜拳游戏
# 定义 1 剪刀  2 : 石头  3 : 布
# 电脑生成一个 1 2 3 中的随机数
# 人输入拳头,  对比 谁输谁赢,   每次猜 5次 每次记录比分并且输出
# 封装到一个对象中

# import random
# class cq():
#  def __init__(self):
#      self.r = 0
#      self.p = 0
#      self.count = int(input("请输入要猜的次数"))
#      self.cq1()
#
#  def cq1(self):
#     for i in range(self.count):
#         print("第",i+1,"次猜拳开始")
#         rob = random.randint(1,3)
#         print(rob)
#         per =int(input("请出手"))
#         if (rob==2 and per == 1) or (rob==3 and per == 2) or (rob==1 and per == 3):
#             print("你输了")
#             self.r+=1
#         elif per == rob:
#             print("平局")
#         else:
#             print("你赢了")
#             self.p+=1
#
#         print("当前比分为:机器人    :      你")
#         print(            self.r , ":"   ,self.p)

# cq()
# 题目：
# 警察局抓了a,b,c,d四名偷窃嫌疑犯，当中只有1个是小偷，审问结果如下：
# a说：“我不是小偷。”    a == 0
# b说：“c是小偷。”       c ==1
# d说：“c在冤枉人。”       d==0
# c说：“小偷肯定是d。”     d == 1
# 现在已经知道4个人中3人说的是真话，一个说的是假话，那么谁是小偷？

# 示：设4个变量a,b,c,d，为0时表示不是小偷，为1时表示是小偷，
# 用四重循环穷举a,b,c,d可能的取值的组合，对每一种组合判断其是否符合题目中给出的约束。


for a in range(0, 2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                if   ((a == 0) + (b == 0 ) + (c == 0) + (d == 0) == 3) and  ((a == 0) + (c == 1)+ (d == 0)+(d == 1)) == 3:
                     print(a,b,c,d)



# # 多线程/单线程 分别写某个文件中 写入10万条数据

# import threading,time
#
# def op(b):
#     for i in range(1000):
#         with open("a.txt","a",encoding="utf8") as f:
#             f.write(b+"\n")
#
# if __name__ == '__main__':
#     time.clock()
#
#     for i in range(10):
#          t = threading.Thread(target=op,args=("这是第"+str(i)+"个线程",))
#          t.start()
#          # t.join() #不能写在这里, 后面的线程添加不了
#     t.join()
#     print(time.clock())


#
#     print(threading.currentThread())
# def op1(b,c):
#     for i in range(10000):
#         with open("a.txt","a",encoding="utf8") as f:
#             f.write(b+c+"\n")
# time.clock()
# op1("这是第d%个线程",str(1))
# print(time.clock())



# def op1(num):
#     print("开始")
#     for i in range(num):
#         with open("ab.txt","a",encoding = "utf8") as f:
#             f.write("第"+str(i)+"条记录""\n")
#     time.clock()
#     print("结束")
# op1(num=10000)
# print(time.clock())
#





# import threading,time






# def op(num):
#     print("子线程开始")
#     for i in range(num):
#         with open("ad.txt","a",encoding = "utf8") as f:
#             f.write("这是第"+str(i)+"条记录"+"\n")
#     print("子线程结束")
#
# if __name__ == '__main__':
#     print("主线程开始")
#     time.clock()
#     t1 = threading.Thread(target =op,args = (10000,))
#     t1.start()
#     t1.join()
#     print("主线程结束")
#     print(time.clock())










import threading,time



# def op(a):
#     # print("子线程开始")
#     for i in range(1000):
#         with open("a.txt","a",encoding = "utf8") as f:
#             f.write(a+"\n")
#
#     # print("子线程结束")
#
#
# if __name__=='__main__':
#     time.clock()
#     # print("主线程开始")
#     for i in range(10):
#         t1 = threading.Thread(target=op,args=("这是第"+str(i)+"条记录",))
#         t1.start()
#     t1.join()
#     # print("主线程结束")
#     print(time.clock())

