# 客户端
import socket


# 1.创建套接字
sk = socket.socket()

# 2.去连接服务器
sk.connect(("192.168.40.166",777))



xx = sk.recv(1024).decode("utf8")

print(xx)

#关闭套接字
sk.close()
