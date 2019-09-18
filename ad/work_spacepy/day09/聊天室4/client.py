import socket,threading

outstring = ""
name = ""
instring = ""

#发送信息
def client_send(sk):
    while True:#死循环   一直监听输入  如果有输入  就会发送到服务端
        global outstring,name
        outstring = input("请输入")#接受输入
        outstring = name +':'+outstring
        sk.send(outstring)#发送


#接收信息
def client_accept(sk):
    global instring
    while True:
        try:
            instring = sk.recv(1024) #接收数据
            if not instring:
                break

            if outstring != instring: #接收和发送不一致时
                print(instring)

        except:
            break


name = input("请输入你的名字")
ip = input("请输入ip地址")

port = 8888 #端口号

sk = socket.socket()#创建套接字

sk.connect((ip,port)) #连接

sk.send(name.encode("utf8"))  #把用户名发送给服务端






while True:
    con,addr = sk.accept()
    th_send = threading.Thread(target=client_send,args = (sk,))#发送消息的线程
    th_send.start()
    th_accept = threading.Thread(target=client_accept(),args = (sk,))#接收消息的线程
    th_accept.start()