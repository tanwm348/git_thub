
import socket
import threading

class Service():
    li =[]
    def __init__(self):
        self.sk = socket.socket()
        self.sk.bind(('127.0.0.1',777))
        self.sk.listen(128)  # 参数: 链接排队的最大数
        print("服务器开始运行,等待客户连接!")
        self.accept()

    def accept(self):
        # 一直等待客户链接,
        while True:
           con,addr = self.sk.accept()#阻塞等待  客户端连接
           # 客户链接之后 创建一个子线程 去实现聊天
           Service.li.append(con)#将连上的人的con保存到列表中
           t1 = threading.Thread(target=self.recv,args=(con,))
           t1.start()




    # 子线程聊天
    def recv(self,con):
        con.send("恭喜连上,请输入名字:".encode("utf8"))
        name = con.recv(1024).decode("utf8")


        while True:
            #接受某个人发送的消息
            source = con.recv(1024).decode("utf8")
            source = name+":"+ source
            print(source)
            # 将接受的信息转发给所有人:
            for i in Service.li:
                if i != con:
                    i.send(source.encode("utf8"))





if __name__ == '__main__':
    Service()