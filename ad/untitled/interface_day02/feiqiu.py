import socket
import time



#飞秋的报文格式
# [版本号:包编号:发送者姓名:发送者主机名:命令字:附加信息]
#协议版本号:1
#包编号:不可重复的数字---时间戳
# 命令字:32--发消息
# 附加信息:消息内容


#初始化套接字
# socket.SOCK_DGRAM 表示UDP协议
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sk.connect(("192.168.40.185",2425))
ban = "1.0"
time1 = str(time.time())
name = "我是刘露"
zjname = "李四"
ml1 = "32"
xiaoxi = "我是王财"
messagelist = [ban,time1,name,zjname,ml1,xiaoxi]

message = ":".join(messagelist)
for i in range(100000):
 sk.send(message.encode("GBK"))
