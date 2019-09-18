





# 1.使用普通函数

#
# def line(x,k,b):
#     print("y =",k*x+b)
#
#
# line(2,3,5)

# 缺点:每次都需要传入很多参数,比如同一条线上的多个点,k和是相同的
#      但是还是需要反复的传

# 2.使用默认值参数:
# def line(x,k = 2,b = 4):
#     print("y =",k*x+b)
#
#
# line(2)
#

# 3.使用对象:消耗资源比较多
# class line():
#     def __init__(self,k,b):
#         self.k = k
#         self.b = b
#
# #     #     调用对象的时候可以给这个方法传参
#     def __call__(self,x):# line1(x)
#         print("y = ",self.k*x+self.b)
#
#
# line1 = line(2,4)
# line1(1)
# line1(2)
# line1(3)
# print("  ")
#
#
# line2 = line(5,5)
# line2(1)
# line2(2)
# line2(3)



# 4.使用闭包  函数中返回个函数
# def set_func(aa,bb):
#     k = aa
#     b = bb
#     def line(x):
#         print("y = ",k*x+b)
#     return line
#
# cc = set_func(2,4) #此时cc中保存的是返回来的函数
#
# cc(1)
# cc(3)


# 匿名函数:可以完成一些非常简单的功能

# 函数:完成一些稍微复杂的功能

# 闭包:完成比较复杂的功能,介于函数和对象之间

# 对象:完成非常复杂的功能

# def sum(k,b):
#     # k = a
#     # b = c
#     def line(x):
#         print("y = ", k*x+b)
#     return line
#
#
# aa = sum(2,4)
# aa(2)
# aa(3)