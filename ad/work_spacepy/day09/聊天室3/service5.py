# 聊天室 服务端功能


# 1. socket/套接字 的作用:
#     可以实现多台电脑之间通过网络的通信
# 电脑和电脑之间的通信: 需要对方的ip  和 端口号

import socket,time,threading

class Service():
    def __init__(self):
        self.sk = socket.socket()
        self.sk.bind(('192.168.40.153',666))
        self.sk.listen(128)  # 参数: 链接排队的最大数
        print("服务器开始运行,等待客户连接!")
        self.con,self.addr = self.sk.accept()  # 返回 值: 1:和客户端链接的套接字  2. 客户端的ip 和端口
        t1 = threading.Thread(target=self.recv)  # 开启子线程执行发送消息
        t1.start()
        self.send()
        # 发送消息
    def send(self):
        while True:
            str1 = input("请输入:")
            self.con.send(str1.encode("utf8"))
            print("服务器发送消息")

    # 接收消息
    def recv(self):
        while True:
            source = self.con.recv(1024).decode("utf8")
            print(source)
            print("服务器接收消息了")
if __name__ == '__main__':
    Service()






# 群聊:

# 1. 要实现服务器和多个人聊天 (多线程)
# 将聊天记录写到某个文件中 名字: 时间: ip: 端口号:  聊天类容

# 查询聊天记录:  请问你要查询谁的聊天记录
#         去文件中读取所有类容到列表中, 然后判断某个元素是否以某个名字开头, 如果是 把他弄出来
#         添加到新的列表中,




# 私聊:  判断有哪些人在线:  要哦谁聊   思考别入如何给你回消息



class Service():
    li = [] #保存所有人的con
    def __init__(self):
        self.sk = socket.socket()
        self.sk.bind(('192.168.40.153',666))
        self.sk.listen(128)  # 参数: 链接排队的最大数
        print("服务器开始运行,等待客户连接!")

    def accept(self):
        pass
        # 一直等待客户链接,
        # 客户链接之后 创建一个子线程 去实现聊天
        # li.append()
        # 主线程继续等

    # 子线程聊天
    def recv(self,con):
        while True:
            source = self.con.recv(1024).decode("utf8")
            # 将接受的信息转发给所有人:
            #     获取所有人的 con 然后发信息
            print(source)
            print("服务器接收消息了")
if __name__ == '__main__':
    Service()




















































