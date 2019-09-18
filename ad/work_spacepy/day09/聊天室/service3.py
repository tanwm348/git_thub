# 聊天室 服务端功能


# 1. socket/套接字 的作用:
#     可以实现多台电脑之间通过网络的通信
# 电脑和电脑之间的通信: 需要对方的ip  和 端口号

import socket

# 1. 创建一个 套接字/socket 对象
sk = socket.socket()

# 2. 给服务器绑定一个ip 和端口号
sk.bind(('192.168.40.153',666))
# 3. 开启监听, 将套接字编程监听套接字
sk.listen(128)  # 参数: 链接排队的最大数
print("服务器开始运行,等待客户连接!")
# 4. 等待客户端链接  注意: 下面这句话会一直阻塞, 知道有人来链接
con,addr = sk.accept()  # 返回 值: 1:和客户端链接的套接字  2. 客户端的ip 和端口

con.send("aaaaaa".encode("utf8"))



print(addr)
print("有人来了,快跑啊!")

# 5. 关闭套接字
con.close()
sk.close()












































