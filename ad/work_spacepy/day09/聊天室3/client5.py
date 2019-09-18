# 客户端
import socket
import threading

class Clice():

   def __init__(self):
      # 1.创建套接字
      self.sk = socket.socket()

      # 2.去连接服务器
      self.sk.connect(("127.0.0.2",666))
      t1 = threading.Thread(target=self.recv)
      t1.start()
      self.send()


      # 发送消息
   def send(self):
         while True:
            s = str(input("客户端输入:\n"))
            print("客户端1:"+s)
            print("如果需要退出,请输入1")
            if s == "1":
               self.close1()
            self.sk.send(s.encode("utf8"))


      # 接受消息
   def recv(self):
          while True:
            aa = self.sk.recv(1024).decode("utf8")
            print("服务器:"+aa)

   def close1(self):
      self.sk.close

if __name__ == '__main__':
    Clice()





























