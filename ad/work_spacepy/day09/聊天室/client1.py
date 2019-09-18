# 客户端

import socket


# 1. 创建套接字
sk = socket.socket()
# 2. 去链接服务器
sk.connect(("192.168.40.168",666))

xx = sk.recv(1024).decode("utf8")
print(xx)
# 关闭 套接字
sk.close()
































