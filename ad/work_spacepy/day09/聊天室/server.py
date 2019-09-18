'''
聊天室服务端功能

'''
import socket

# 1.socket/套接字 的作用:
#   可以实现多台电脑之间通过网络的通信
# 电脑和电脑之间的通信:需要对方的 ip 和 端口号

# 创建一个套接字/对象
sk = socket.socket()

# 2.给服务器绑定一个ip和端口号
sk.bind(('127.0.0.1',777))

#3.开始监听,将套接字编程监听套接字
sk.listen(128) # 参数:连接排队的最大数
print("服务器开始运行")


# 4.等待客户端连接 注意这句话会一直阻塞,直到有人来连接
con,addr = sk.accept() #返回值 con:和客户端连接的套接字  addr:客户端的ip和端口
# lt = input("你要说什么")
# for i in range(100):
lt = input("你要说什么")
con.send(lt.encode("utf8"))


# 5.关闭套接字
con.close()
sk.close()

