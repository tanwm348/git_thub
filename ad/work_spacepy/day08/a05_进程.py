'''
使用多进程去解决 多线程中共享全局变量乱码的问题
'''
import multiprocessing


# 创建子进程后,子进程会将主进程的内容复制一份,
# 然后去执行相应的操作,进程和进程之间没有共享数据


# 消息队列:可与会实现进程和进程之间的通信
# 消息队列本质:存储数据的

# 队列: 先进先出
# 栈:   先进后出


import multiprocessing
num = 0
def getsum(a):
    global num
    for i in range(10000):
        num+=a
        num-=a


if __name__ == '__main__':
# 创建一个子进程
    t1 =multiprocessing.Process(target=getsum,args = (5,))
    t2 = multiprocessing.Process(target=getsum,args = (8,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    print(num)

#进程之间的通信
# 创建两个进程向消息队列中存数据
# 另一个去消息队列取数据

#
# def setVulue(que):
#     li = ["a","b","c"]
#     for i in li:
#         que.put(i)
#
#
# def getValue(que):
#     li1 = []
#     for i in range(que.qsize()):
#         aa = que.get()
#         li1.append(aa)
#     print(li1)
#
# if __name__ == '__main__':
#     que = multiprocessing.Queue()
#     p1 = multiprocessing.Process(target=setVulue,args=(que,))
#     p2 = multiprocessing.Process(target=getValue,args=(que,))
#
#     p1.start()
#     p2.start()
#     p1.join()
#     p1.join()



# 多线程/单线程 分别写某个文件中 写入10万条数据
