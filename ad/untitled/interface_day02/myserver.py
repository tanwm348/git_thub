import  socket
#实例化套接字
#socket.AF_INET---使用通信协议
#socket.SOCK_DGRAM --表示的是面向连接的连接协议  ICP
sk = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

sk.bind(("127.0.0.1",8080))


sk.listen(128)
print("服务器开始运行")

con,addr = sk.accept()
while True:
    date = con.recv(1024).decode("utf8")

    if date == "esc":
        break

    print(date)
    aa =con.send("你好,很高兴认识你".encode("utf8"))


con.close()
sk.close()