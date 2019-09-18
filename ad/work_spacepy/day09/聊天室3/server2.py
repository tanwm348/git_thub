'''
聊天室服务端功能

'''
import socket
import threading

# # 1.socket/套接字 的作用:
# #   可以实现多台电脑之间通过网络的通信
# # 电脑和电脑之间的通信:需要对方的 ip 和 端口号
#
# # 创建一个套接字/对象
# sk = socket.socket()
#
# # 2.给服务器绑定一个ip核端口号
# sk.bind(('192.168.40.166',777))
#
# #3.开始监听,将套接字编程监听套接字
# sk.listen(128) # 参数:连接排队的最大数
# print("服务器开始运行")
#
#
# # 4.等待客户端连接 注意这句话会一直阻塞,直到有人来连接
# con,addr = sk.accept() #返回值 con:和客户端连接的套接字  addr:客户端的ip和端口
# # lt = input("你要说什么")
# # for i in range(100):
# # while True:
# con.recv(1024).decode("utf8")
# # print(aa)
#
# #   lt = input("你要说什么")
# #   print(sk.recv(1024).decode("utf8"))
#
#
# # 5.关闭套接字
# con.close()
# sk.close()





class Server():

   def __init__(self):
      # 1.创建套接字
      self.sk = socket.socket()

      #2.给服务器绑定一个ip核端口号
      self.sk.bind(('127.0.0.1',666))

      # 3.开始监听,将套接字编程监听套接字
      self.sk.listen(128) # 参数:连接排队的最大数
      print("服务器开始运行")

      # 4.等待客户端连接 注意这句话会一直阻塞,直到有人来连接
      self.con,self.addr = self.sk.accept()
      t1 = threading.Thread(target=self.recv1)
      t2 = threading.Thread(target= self.send1)
      t1.start()
      t2.start()



      # 发送消息
   def send1(self):
         while True:
            f = str(input("服务器输入:\n"))
            print("服务器:"+f)
            print("如果需要退出,请输入1")
            if f == "1":
               self.close2()
            self.con.send(f.encode("utf8"))

      # 接受消息
   def recv1(self):
          while True:
            aa = self.con.recv(1024).decode("utf8")
            print("客户端:"+aa)



   def close2(self):
      self.con.close()
      self.sk.close

if __name__ == '__main__':
    Server()