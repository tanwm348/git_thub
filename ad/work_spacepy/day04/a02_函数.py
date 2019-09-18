'''
js中的函数
    1.如何 创建一个函数
    2.如何使用使用函数
    3.参数问题
    4.将函数写到其他函数中，然后调用
    5.返回值的问题
    6.全局变量和局部变量
    7.可变参数和不可变参数
    8.debug
    9.参数问题









'''
# 函数：函数是实现了一定功能的代码的集合
# 1.如何创建一个函数
# function  函数名（）{}

# def getsum():
#     print(2)

# 2.调用函数
#     语法：函数名
# print(1)
# getsum()
# print(3)

# 3.参数问题
# def getsum(aa,bb):
#     sum = 0
#     for i in range(aa,bb):
#             sum=sum+i
#     print(sum)
#
# getsum(50,100)

# 4.希望调用其他模块中已经写好的函数
# 需要引入文件
# from day04.a02_函数01 import * # = getSum,getSum1
#
# sum1 = getSum(1,101)
# sum2 = getSum(1,3)
#
# print(sum1)
# print(sum2)
#
# print(getSum1(1,4))


# 6.全局变量和局部变量
# li = [1,2]
# 全局变量:从定义之后，后面一直都可以使用

# 局部变量：定义在函数中的变量
# 在函数中使用全局变量，注意需要在前面使用 global（标记）声明（global  sum）
# sum = 1
# def getSum(aa,bb):
#     global sum
#     sum = 0
#     for i in range(aa,bb):
#         sum += i
#
#     print(sum)
#
# getSum(1,101)

# 7.可变参数和不可变参数
# 不可变类型：修改内容，必须创建一个新的内容重新赋值
# 不可变数据类型：数字 字符串 元组
# num = 5
# num = 6

# 可变数据类型：修改里面的内容，但是这个变量本身地址不变
# 可变数据类型：列表 字典 集合
# li[1,2,3,4]
# li.insert(4,"5")

# 可变数据类型和不可变数据类型作为函数的参数问题
# 注意:如果传入函数中的是一个可变数据类型，
#      那么函数中对这个数据进行操作会影响外面 的变量
# def getSum(aa,bb):
#    aa.insert(1,"2")
#    bb = 10
#    print(aa)
#    print(bb)
#
# num1 = [1,1,2]
# num2 = 20
#
# getSum(num1,num2)
# print(num1)
# print(num2)

# debug
# print(1)
# def getSum(aa,bb):
#     sum = 0
#     for i in range(aa,bb):
#         sum += i
#
#     return sum
#
# sum1 = getSum(1,101)
# print(sum1)


# 10.参数的问题
# 10.1 必须参数：
#     问题：必须按照顺序传参，不能多传，少传，或者不传
# def getSum(aa,bb):
#     sum = 0
#     for i in range(aa,bb):
#         sum += i
#
# getSum(1,3)


# 关键字参数：
# 解决了参数顺序不能变的问题
# 不能少传
# def getSum(aa,bb):
#     sum = 0
#     for i in range(aa,bb):
#         sum += i
#
# getSum(aa= 1,bb= 3)




# 默认值参数：
# 不设值则用默认值   能够少传 或者不传，能和关键字参数配合着换位置传
# def getSum(aa=1,bb=100):
#     sum = 0
#     for i in range(aa,bb):
#         sum += i
#     print(sum)

# getSum(bb=3)



# 不定长参数
# def getSum(aa,bb,*cc,**dd):#*cc一般取*args  dd = **kwargs
#     sum = 0
#     print(aa,bb,cc,dd)
#
# getSum(1,3,4,5,ff=2,ii=5)
# aa=1  bb=3 *cc={4,5} **dd={'ff:2','ii':5}



# 11.匿名函数
# 使用关键字 lambda:语法如下
# 完成一些简单的功能，只能返回一个值，将着多个值放在列表/元组中
lam = lambda x,y:[x**y,x*y]

print(lam(2,3))

# 12.迭代器
li = [1,2,3,4]

# 1.创建一个可以迭代的对象
li1 = iter(li)

# 2.输出可迭代对象中的内容
print(next(li1))
print(next(li1))
print(next(li1))
print(next(li1))
