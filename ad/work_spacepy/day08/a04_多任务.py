'''
线程 进程 协程
cpu:4核8核心

每个核 在同一时刻只能做一件事情

并行:多个任务在同一时刻同时被执行
并发:假多任务,由于cpu执行速度非常快,不断循环去执行多个任务,
    我们感觉这多个任务是在一起执行

时间片轮转:cpu随机给每个任务分配时间,
          然后让这些任务按照一定的顺序执行

进程:一个运行起来的程序就是一个进程(进程包括 源代码 内存 摄像头 声卡 显示器)
    ,代码和资源的集合,进程是分配资源的基本单位

线程:一个程序运行起来一定有一个东西去执行代码,
    线程是系统执行操作的最小单位
    一个进程至少有一个线程

多进程:多进程 多个程序同时运行

多线程:一个进程中有多个线程

线程中只有很少的数据,大部分数据都是存储在进程中,
那么多线程有很多数据就会共享




'''
# def sing():
#     for i in range(5):
#         print("让我们一起摇摆")
#
# def dance():
#     for i in range(5):
#         print("恰恰恰")
#
# if __name__ == '__main__':
#     sing()
#     dance()



# # 让唱歌跳舞一起执行
# import threading,time#主线程
# def sing():
#     for i in range(5):
#         time.sleep(1)
#         print("让我们一起摇摆")
#
# def dance():
#     for i in range(5):
#         time.sleep(1)
#         print("恰恰恰")
#
# if __name__ == '__main__':
#     #创建一个子线程,参数是这个子线程需要执行的任务
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()#启动子线程
#     t2.start()
#
#
#     for i in range(5):
#         time.sleep(1)
#         print("主线程执行")
#

# 1.让主线程等子线程执行完再结束
# 让唱歌跳舞一起执行
# import threading,time#主线程
# def sing():
#     for i in range(5):
#         time.sleep(1)
#         print("唱歌")
#
# def dance():
#     for i in range(5):
#         time.sleep(2)
#         print("跳舞")
#
# if __name__ == '__main__':
#     #创建一个子线程,参数是这个子线程需要执行的任务
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()#启动子线程
#     t2.start()
#
#     t1.join()#等待t1子线程结束后 主线程在结束
#     # t2.join()
#     t2.join(5)#参数是最大等待的秒数,如果等了这么多秒,不管线程是否结束,
#              # 主线程都会继续往下走
#
#     print("主线程执行")

# 3.守护线程 子线程随着主线程的结束而结束
# import threading,time#主线程
# def sing():
#     for i in range(5):
#         time.sleep(1)
#         print("唱歌")
#
# def dance():
#     for i in range(5):
#         time.sleep(1)
#         print("跳舞")
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.setDaemon(True)
#     t2.setDaemon(True)
#
#     t1.start()
#     t2.start()
#     print("主线程结束")

# 4.线程常用方法
# import threading,time#主线程
# def sing():
#     # 获取当前所有的线程变量
#
#     for i in range(5):
#         time.sleep(1)
#         print("唱歌")
#     print(threading.enumerate())
#     threading.enumerate()[0].setName("主线程")
#     print(threading.enumerate())
# def dance():
#     for i in range(5):
#         time.sleep(1)
#         print("跳舞")

# if __name__ == '__main__':
#     t1 = threading.Thread(target=sing)
    # t2 = threading.Thread(target=dance)

    # print(t1.getName())
    # t1.setName("线程1")

    # t1.setDaemon(True)
    # t2.setDaemon(True)
    #
    # t1.start()
    # t2.start()

#     # 获取当前线程变量
#     thr = threading.currentThread()
#     print(thr)
#     print(t1)
#     print(id(t1))


    # print("主线程结束")


# 5.多线程共享全局变量的
# import threading
# num = 0
# def getsum(a):
#     global num
#
#     for i in range(100000):
#         num+=a
#         num-=a
#
# if __name__ == '__main__':
#     for i in range(10):
#         t1 = threading.Thread(target=getsum,args=(5,))
#         t2 = threading.Thread(target=getsum,args=(5,))
#
#         t1.start()
#         t2.start()
#         t1.join()
#         t2.join()
#         print(num)
#         num = 0

# 6.使用同步锁解决多线程共享全局变量的问题
import threading
num = 0
def getsum(a):
    global num

    lock.acquire() #  使用锁对象
    for i in range(100000):
        num+=a
        num-=a
    lock.release()#解锁

if __name__ == '__main__':
    lock = threading.Lock()#创建锁对象
    for i in range(10):
        t1 = threading.Thread(target=getsum,args=(5,))
        t2 = threading.Thread(target=getsum,args=(5,))

        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(num)
        num = 0

# cpu密集型程序
# io密集型




