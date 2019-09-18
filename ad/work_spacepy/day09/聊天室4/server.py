import socket
import threading


def clientThreadIn(con,name):
    global date
    while True:
        try:
            temp = con,repr(1024)#客户端发送过来的消息
            if not temp:
                con.close()
                return
            else:
                NotifyAll(temp)
        except:
            NotifyAll(name+"离开房间")#出现问题就退出
            print(date)
            return


def clientThreadout():
    global date
    while True:
        if con.accept():
            con.wait()#放弃对资源占有  等待通知 然后运行后面的代码
            if date:
                try:
                    con.send(date)
                    con.release()
                except:
                    con.release()
                    return





def NotifyAll(a):
    global date
    if con.acquire():#获取锁
        date = a
        con.nottiAll()  #当前线程放弃对资源占有,通知所有等待线程从wait方法执行
        con.release()

conn = threading.Condition()#条件
sk = socket.socket()  #创建一个服务

host = input("请输入服务器ip")

port = 8888

date = ""

sk.bind((host,port))#绑定

sk.listen(128) #监听



while True:
    con,addr = sk.accept()

    print(addr[0]+":"+str(addr[1]))

    name = con.recv(1024)

    NotifyAll( "欢迎"+name+"进入房间")

    con.send(date)

t1 = threading.Thread(target=clientThreadIn(),args=(con,name))

t2 =  threading.Thread(target=clientThreadout(),args=(con,name))

t1.start()
t2.start()
