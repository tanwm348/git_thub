'''
装饰器:

开放闭合原则
一段代码在写好后,如果增加这段代码的功能,不建议去直接修改源代码

开放:可以对功能进行拓展
闭合:不要去修改源代码

'''

# 有个函数:需要去测试这个函数的执行时间

# 1.装饰器


# import time
# def set_func(fun):
#     def func():
#         time.perf_counter()
#         fun()
#         print(time.perf_counter())
#         print(1)
#     return func
#
# @set_func
# def test():
#     num = 0
#     for i in range(100000):
#         num += i
#     print(num)
# if __name__ == '__main__':
#     test()


# 2.自己实现装饰器

# def set_func(fun):
#     def func():
#       print("验证一下权限")
#       fun()
#
#     return func
#
# def test():
#   print("我又来了")
#
# if __name__ == '__main__':
#     test = set_func(test)
#     test()

# 3.参数问题
def set_func(fun):
    def func(a,b):
      fun(a,b)

    return func


@set_func
def test(a,b):
  num = 0
  for i in range(a,b):
      num += i
  print("num",":",num)


if __name__ == '__main__':
    test(1,3)
#

# def set_func(fun):
#     def func(a,b):
#       # print("验证一下权限")
#       fun(a,b)
#
#     return func
#
# def test(a,b):
#     num = 0
#     for i in range(a,b):
#         num += i
#     print(num)
# if __name__ == '__main__':
#     test = set_func(test)
#     test(1,101)


# 3.参数问题:
#
# def set_func(fun):
#     def func(*args,**kwargs):
#       # print("验证一下权限")
#       fun(*args,**kwargs)
#
#     return func
#
# def test(a,b,*args,**kwargs):
#    print(a,b,args,kwargs)
#
# if __name__ == '__main__':
#     test = set_func(test)
#     test(1,101,22,33,44,aa=1,cc= 2)


# 4.返回值问题:  通用装饰器写法

# def set_func(fun):
#     def func(*args,**kwargs):
#       # print("验证一下权限")
#       return fun(*args,**kwargs)
#
#     return func
#
# def test(a,b,*args,**kwargs):
#    print(a,b,args,kwargs)
#    return 111111111
#
# if __name__ == '__main__':
#     test = set_func(test)
#
#     print(test(1,101,22,33,44,aa=1,cc= 2))

# 5.多个装饰器执行顺序
def set_func(fun):
    print(1)
    def func(*args,**kwargs):
      print(2)
      return fun()

    return func

def set_func1(fun):
    print(3)
    def func1(*args,**kwargs):
      print(4)
      return fun()

    return func1




@set_func
@set_func1

def test():
    print("aaaaaa")
if __name__ == '__main__':
    test()