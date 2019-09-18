import socket
import threading

class Clice():

   def __init__(self):
      # 1.创建套接字
      self.sk = socket.socket()

      # 2.去连接服务器
      self.sk.connect(("127.0.0.1",777))
      t1 = threading.Thread(target=self.send)
      t2 = threading.Thread(target=self.recv)
      t1.start()
      t2.start()


      # 发送消息
   def send(self):
         while True:
            s = (input("请输入:\n"))
            self.sk.send(s.encode("utf8"))
            print("发过去了")


      # 接受消息
   def recv(self):
          while True:
            aa = self.sk.recv(1024).decode("utf8")
            print(aa)
            print("接收消息:")



if __name__ == '__main__':
    Clice()
   