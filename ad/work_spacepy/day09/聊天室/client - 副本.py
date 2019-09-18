# 客户端

import socket


# 1. 创建套接字
sk = socket.socket()
# 2. 去链接服务器
sk.connect(("192.168.40.153",666))

xx = sk.recv(1024).decode("utf8")  #接受来自服务器的消息,这里会阻塞
print(xx)

sk.send("我真的连上了嘛?".encode("utf8")) # 向服务器发送消息



# 关闭 套接字
sk.close()
































