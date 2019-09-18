
# 今天的安排:
# 1.文件操作
# 2.模块和包
# 3. 多任务 线程 进程 协程

# W: 向文件中插入数据
#   特点:
#     1. 只能插入字符串, 如果需要插入其他类型的请强制转换
#     2. 多次插入不会自动换行 如果需要换行 添加 \n
#     3. 他会覆盖文件中的内容
#     4. 文件如果不存在自己创建一个, 如果存在直接打开

# a: 向文件中追加内容
#     特点:
#         如果文件没有也会创建
#         不会覆盖以前的内容
#         也只能插入字符串

# 1. 向某个文件中写入类容
# li = ["张三","李四",222]
# li = ["张三","李四",222,{"aa":"aaaa","bb":"bbbbb"}]
# with open("aa.txt","w",encoding="utf8") as f:
    # f.write("你好啊, 吃饭了没啊!\n")
    # f.write("下雨了")
    # f.write("现在几点了?")
    # f.write("5")
    # for i in li:
    #     if type(i)== dict:
    #         print(i)
    #         for k,v in i.items():
    #             f.write(str(k)+":"+str(v)+"\n")
    #     else:
    #         f.write(str(i)+"\n")

# 张三
# 李四
# 222
# aa:aaaa
# bb:bbbbb

# 2. 向文件中最加内容
# with open("aaa.txt","a",encoding="utf-8") as f:
#     f.write("这是追加的内容")


# 3. 读文件

with open("aa.txt","r",encoding="utf8",newline="") as f:
    # souce = f.read() # 读取全部内容
    # print(souce)
    # print(f.readline(5))
    print(f.readline().strip())  #strip() 不传参 默认消除空格和换行
    print(f.readline())
    # print(f.readlines())
    # print(f.read().splitlines())

# 将 aa.txt 文件复制到 aaaa文件夹下面
#    复制图片

# 封装数据库中:  用户名 密码  数据库名














