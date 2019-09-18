
# 客户端

# 收发 同时进行  把这个客户端做成一个类

import socket
import threading


class Client():
    def __init__(self):
        # 1. 创建套接字
        self.sk = socket.socket()
        # 2. 去链接服务器
        self.sk.connect(("127.0.0.1",666))

    # 发送消息
    def send(self):
        while True:
            str1 = input("")
            self.sk.send(str1.encode("utf8"))
            # print("发过去了")

    # 接收消息
    def recv(self):
        while True:
            source = self.sk.recv(1024).decode("utf8")
            print(source)
            # print("接收消息了")

    def thread(self):
         t1=threading.Thread(target=self.send)# 开启子线程执行发送消息
         t2=threading.Thread(target=self.recv)
         t1.start()
         t2.start()

    def close(self):
         self.sk.close()





if __name__ == '__main__':
    Client().thread()



























































