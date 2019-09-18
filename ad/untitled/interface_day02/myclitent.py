import socket


#创建套接字
sk = socket.socket()

#连接服务器
sk.connect(("127.0.0.1",8080))


input1 =input("输入esc取消")
while True:

    sk1 = sk.send(input1.encode("utf8"))

    da = sk.recv(1024).decode("utf8")
    print(da)

sk.close()