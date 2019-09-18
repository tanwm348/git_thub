'''
程序中如果出现了异常,整个程序会直接退出,这样不科学
我们需要对异常进行处理

'''
# 1.异常处理:哪里有异常就把他放到try中
# 执行顺序:从上到下,进入try语句中,如果try语句中没有出现异常,
#          程序不会走except,而是直接向下执行
#          如果程序在try中出现了异常,try中的语句不会再执行了
#          直接进入except字句(条件是 捕获了这类异常)
#          如果没有捕获这一类异常,会直接跳出程序
# print(0)
# try:
#     print(1)
#     1/0
#     # int("sdf")
#     print(2)
# except ZeroDivisionError as e:#可以捕获对应的异常,不能捕获其他类型的异常
#     print("捕获到异常了,你的除数为0了")
#     print(e)

# print(3)

# 2. 如何捕获多个异常
# print(0)
# try:
#     print(1)
#     # 1/0
#     int("sdf")
#     print(2)
# except (ZeroDivisionError,ValueError) as e:
#     print("捕获到异常了,你的除数为0了")
#     print(e)


# print(0)
# try:
#     print(1)
#     # 1/0
#     int("sdf")
#     print(2)
# except ZeroDivisionError as e:
#     print("捕获到异常了,你的除数为0了")
#     print(e)
# except ValueError as e:
#     print("参数异常")
#     print(e)

# 3.使用常见类型的基类,捕获一些常见的异常
# print(0)
# try:
#     print(1)
#     1/0
#     int("sdf")
#
# except Exception as e:
#     print(e)
#     print(3)
'''
python标准异常
异常名称 描述
BaseException 所有异常的基类
    SystemExit 解释器请求退出
    KeyboardInterrupt 用户中断执行(通常是输入^C)
    Exception 常规错误的基类
        GeneratorExit 生成器(generator)发生异常来通知退出
        OverflowError 数值运算超出最大限制
        ZeroDivisionError 除(或取模)零 (所有数据类型)
        AttributeError 对象没有这个属性
        EnvironmentError 操作系统错误的基类
        IOError 输入/输出操作失败
        OSError 操作系统错误
        ImportError 导入模块/对象失败
        IndexError 序列中没有此索引(index)
        KeyError 映射中没有这个键
        MemoryError 内存溢出错误(对于Python 解释器不是致命的)
        NameError 未声明/初始化对象 (没有属性)
        RuntimeError 一般的运行时错误
        NotImplementedError 尚未实现的方法
        IndentationError 缩进错误
        SystemError 一般的解释器系统错误
        TypeError 对类型无效的操作
        ValueError 传入无效的参数
        Warning 警告的基类

'''

# NameError 未声明/初始化对象 (没有属性)
# KeyError 映射中没有这个键
# ImportError 导入模块/对象失败
# ValueError 传入无效的参数
# StopAsyncIteration
# try:
#     # print(z)
# except NameError as e:
#     print(e)


# 4.语法 try except 后面可以跟else
# else执行的时机:如果没有走except就会走else
try:
    print(1)
    # 1/0
    # int("sda")
except Exception as e:
    print(e)
else:
    print("这里是else")


# 5.finally字句
# try:
#     print(1)

#   1.连接数据库
#   2.操作数据库
#   3.关闭连接
#     1/0
#     int("sda")

# except NameError as e:
#     print(e)
# else:
#     print("这里是else")
# finally:#注意:就算try语句的异常没有被捕获
#          # 也会继续执行
#     print("无论报不报错都会执行")
# print(3)