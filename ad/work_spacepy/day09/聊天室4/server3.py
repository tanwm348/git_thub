
# 群聊:

# 1. 要实现服务器和多个人聊天 (多线程)
# 将聊天记录写到某个文件中 名字: 时间: ip: 端口号:  聊天内容

# 查询聊天记录:  请问你要查询谁的聊天记录
#         去文件中读取所有类容到列表中, 然后判断某个元素是否以某个名字开头, 如果是 把他弄出来
#         添加到新的列表中,


import socket,time,threading

class Service():
    def __init__(self):
        self.sk = socket.socket()
        self.sk.bind(('127.0.0.1',666))
        self.sk.listen(128)  # 参数: 链接排队的最大数
        print("服务器开始运行,等待客户连接!")
        self.accept()

    def  accept(self):
        user=[]
        while True:
            con,addr=self.sk.accept()
            user.append(con)
            con.send(("欢迎加入群聊,请输入你的名字").encode("utf8"))
            username=con.recv(1024).decode("utf8")
            for i in user:
                i.send(("欢迎"+username+"加入群聊").encode("utf8"))
            # print(str(addr)+"欢迎"+username+"加入群聊")

            with open("date.txt","a",encoding="utf8") as f:  #写日志
                f.write(str(addr)+"欢迎"+username+"加入群聊"+"       "+time.asctime(time.localtime())+"\n")

            t1=threading.Thread(target=self.recv,args=(con,user,username))# 开启子线程执行发送消息
            t1.start()# 发送消息


    # 接收消息

    def recv(self,con,user,username):
        dic={}
        li=[]
        dic["姓名"]=username
        dic["内容"]=li
        while True:
            source = username+":"+con.recv(1024).decode("utf8")
            print(source)
            li.append(source)
            # print("服务器接收消息了")
            with open("date.txt","a",encoding="utf8") as f:  #写日志
                 f.write(source+"         "+time.asctime(time.localtime())+"\n")

            for i in user:
                i.send(source.encode("utf8"))#向其他人广播

    def __del__(self):
        self.sk.close()


if __name__ == '__main__':
    Service()






#
#
# class Service():
#     li = [] #保存所有人的con
#     def __init__(self):
#         self.sk = socket.socket()
#         self.sk.bind(('192.168.40.153',666))
#         self.sk.listen(128)  # 参数: 链接排队的最大数
#         print("服务器开始运行,等待客户连接!")
#
#     def accept(self):
#         pass
#         # 一直等待客户链接,
#         # 客户链接之后 创建一个子线程 去实现聊天
#         # li.append()
#         # 主线程继续等
#
#     # 子线程聊天
#     def recv(self,con):
#         while True:
#             source = self.con.recv(1024).decode("utf8")
#             # 将接受的信息转发给所有人:
#             #     获取所有人的 con 然后发信息
#             print(source)
#             print("服务器接收消息了")
# if __name__ == '__main__':
#     Service()
#
#











































