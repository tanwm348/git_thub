# 控制结构：分支 和 循环

# 1.分支：
#1.1 多个分支不互斥
# if:条件
#     执行的内容
# if:条件
#     执行的内容
# if:条件
#     执行的内容


# 1.2只有两个分支且这两个分支是互斥的，只会走一个分支
# if 5>6:
#     print("a")
# else:
#     print("b")
#
# 1.3 多个分支 且这多个分支是互斥的
# if 条件 ：
#     执行的内容
# elif 条件：
#     执行的内容
# else:
#     执行的内容

# 1.从页面接受一个内容 日期格式是 xxxx-xx-xx  年月日
# 判断是平年还是瑞年
# a = str(input("请输入"))
# b = int(a[0:4])
# if(b%4==0):
#     print("今年是闰年")
# else:
#     print("今年是平年")

# 2.从页面输入一个字符串 判断这个字符串是否是 数字 或者 数字和字母或者
# 数字和字母 或者其他
# str2 = str1.isnumeric()#数字
# str3 = str1.isalpha()#字母
# str4 = str1.isalnum()#组合
# str1 = str(input())
# if(str1.isnumeric()):
#     print("全是数字")
# elif(str1.isalpha()):
#     print("全是字母")
# elif(str1.isalnum()):
#     print("有字母和数字")
# else:
#     print("输入错误")
# 循环结构
#使用下标输出字符串的内容 range()
# range()函数 有3个参数
# 参数1：从哪里开始 默认0
# 参数2：到哪里结束  左闭右开
# 参数3;步长 默认为1


# str1 = "12345aaa"
# for i in range(0,len(str1)):
#     print(str1[i])



# for i in range(0,100,2):
#     print(i)


#
# str2 = "012345678"
# for i in str2:
#     x = int(i)
#     print(str2[x])

# a = 0
# for i in range(101):
#     a = a + i
#
# print(a)
#
# for i in range(10):
#     if i == 8:
#         continue

        # print(i)

# break:跳出当前循环，结束这个循环
# continue:结束本次循环，进入下一个循环

# while 循环：

# 1.打印99乘法表
for i in range(1,10):
    for j in range(1,10):
        if(i>=j):
                print(i , "*" , j , "=" , i*j,"" , end="")

    print()

 # 2.一个10000以内整数，它加上100和加上268后都是一个完全平方数，请问该数是多少
# for i in range(10000):
#          x = int((i + 100)**0.5)
#          y = int((i + 268)**0.5)
#          if(x * x == i + 100) and (y * y == i + 268):
#           print(i)



# 3.输入三个整数x,y,z 请把三个数由小到大输入
# x =int((input("请输入X:")))
# y =int((input("请输入Y:")))
# z =int((input("请输入Z:")))
# if x<y<z:
#     print(x,y,z)
# elif x<z<y:
#     print(x,z,y)
# elif y<z<x:
#     print(y,z,x)
# elif y<x<z:
#     print(y,x,z)
# elif z<x<y:
#     print(z,x,y)
# elif z<y<x:
#     print(z,y,x)





# 4.求1000以内的水仙花数
# for i in range(2,1000):
#     a = int(i / 100)
#     b = int(i / 10 % 10)
#     c = int(i % 10 % 10)
#     num = (a*a*a+b*b*b+c*c*c)
#     if(i==num):print(i)



# 5.对3 65 22 102 4 进行升序排序

a = ("3","65","22","102","4")
n = 0
for i in range(0,len(a)-1):
    for j in range(0,len(a)-1):
        if a[i] > a[j+1]:
            a[i+1],a[i] = a[j],a[j+1]
#             n = a[j]
#             a[i] = a[j+1]
#             a[j+1] = n
#
    print(a)

# 6猜数字游戏，系统随机生成一个1000以内的数字，用户输入一个数字，如果输入数字大于系统数字则提示”大了“
# 反之提示”小了“ 直到游戏结束，提示”通关“并输出猜测次数
# import random
#
# aa= random.randint(1,1000)
# print(aa)
# while True:
#     bb = int(input("请输入数字:"))
#     if aa==bb:
#         print("通关")
#         break
#     elif bb > aa:
#         print("大了")
#     else :
#         print("小了")
#
#         continue