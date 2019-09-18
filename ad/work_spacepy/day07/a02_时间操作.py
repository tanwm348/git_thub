'''
时间操作
'''
import time
# print(time.time())
# 1.时间戳 1970年1月1号到现在的秒数,
# time.sleep(1)#停止1秒
# print(time.time())

# print(time.time())
#
#
# # 2.时间元组
# print(time.localtime())#有个默认参数  当前时间戳
# print(time.localtime(time.time()))
# print(time.localtime(1559614599.1402633))#将时间戳转换成一个时间元组
#
# # 3.获取一个可视化时间(美式日期)
# print(time.asctime())
# print(time.asctime(time.localtime()))
# print(time.asctime(time.localtime(time.time())))
# print(time.asctime((time.localtime(1559614599.1402633))))
#
# print(time.asctime(time.localtime(1550503710)))

# 4.获取一个我们习惯的可视化时间
# 可以将时间戳转换成可视化时间
# print(time.strftime("%Y--%m--%d %H:%M:%S"))
# print(time.strftime("%Y--%m--%d %H:%M:%S",time.localtime()))
# print(time.strftime("%Y--%m--%d %H:%M:%S",time.localtime(559616148.9967458)))#输出时间戳的时间

# 5.将一个可视化时间转换成时间元组\
# now = "2019-6-3 10:49:50"
# 参数1  需要将字符串转换成时间元组
# 参数2   这个时间的格式
# nowtime = time.strptime(now,"%Y-%m-%d %H:%M:%S")
# print(nowtime)

# 6.将时间元组转换成时间戳
# print(time.mktime(time.localtime()))

# 7.将字符串转换成时间戳

# print(time.mktime(time.strptime(now,"%Y-%m-%d %H:%M:%S")))

# 1.将时间戳转换成时间元组
# 2.将时间元组转换成可视化时间

# 3.将可视化时间转换成时间元组
# 4.将时间元组转换成时间戳

# 练习:淘宝7天无理由退款,输出 现在下单最后退款时间
now = "2019-6-4 11:07:20"
# now1 = "2019-6-5 11:07:20"
num1 = time.mktime(time.strptime(now,"%Y-%m-%d %H:%M:%S"))
# num2 = time.mktime(time.strptime(now1,"%Y-%m-%d %H:%M:%S"))
# num3 = num2 - num1
# num4 = num1+num3*7
num2 = num1+(60*60*24*7)
print(num2)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(num2)))

# 输出2006年11月11号 11;11;11像前180的日期
# now2 = "2006-11-11 11:11:11"
# num5 = time.mktime(time.strptime(now2,"%Y-%m-%d %H:%M:%S"))
# num6 = num5-num3*180
# print(time.strftime("%Y--%m--%d %H:%M:%S",time.localtime(num6)))
# 计算你活了多少天,多少小时,
# now3 = "1994-12-26 0:0:0"
# num7 = time.mktime(time.strptime(now3,"%Y-%m-%d %H:%M:%S"))
# num8 = time.mktime(time.localtime())
# num9 = num8 - num7
# print(num9/60/60/24)

# num9 = num8-num7
# num10 =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(num9))
# print(num10)
# print(time.strptime(num10,"%Y-%m-%d %H:%M:%S"))


# 7.计算机程序运行时间
# time.clock()
# aa = time.time()
# for i in range(1000000):
#     a= 1+i
#
# print(2)
# bb = time.time()
# print(bb-aa)
# print(time.clock())

# 程序运行时间=cpu执行时间+程序阻塞时间
# time.perf_counter()#运行系统时间
# # time.process_time()#返回进程运行时间 不用做标记
# for i in range(1000000):
#     a= 1+i
#
# print(time.perf_counter())
# print(time.process_time())