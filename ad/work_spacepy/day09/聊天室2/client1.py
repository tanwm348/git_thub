# 客户端
import socket


# 1.创建套接字
sk = socket.socket()

# 2.去连接服务器
sk.connect(("192.168.40.166",666))


while True:
   lt = input("你要说什么")
   print(sk.recv(1024).decode("utf8"))

#关闭套接字
sk.close()
