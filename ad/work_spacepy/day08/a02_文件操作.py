'''
1.文件操作
2.模块和包
3.多任务 线程 进程  协程
'''
# w:像文件中插入数据
# 特点:
# 1.只能插入字符串  如果插入其他类型需强转
# 2.多次插入不会自动换行 如果需要换行 添加\n
# 3.会覆盖文件中的内容
# 4.文件如果不存在自己创建一个,如果存在直接打开

# a:像文件中追加内容
# 特点:1.不会覆盖以前的内容
#      2.如果文件没有也会创建
#      3.只能插入字符串

# 1.像某个文件中写入内容
# 覆盖
# with open("aa.txt","w",encoding="utf8")as f:
    # f.write("你好.\n")
    # f.write("并不好!\n")
    # f.write("为什么?\n")
    # f.write("5\n")
    #
    # li = ["张三","李四",222,{"aaa":"aaaa","bb":"bbbb"}]
    # for i in li:
    #   if type(i)==dict:
    #       for k,v in i.items():
    #           f.write(str(k)+":"+str(v)+"\n")
    #   else:
    #       f.write(str(i)+"\n")

# 2.像文件中追加内容
# with open("aa.txt","a",encoding="utf-8") as f:
#     f.write("localhost""\n")
#     f.write("root""\n")
#     f.write("123456")
with open("aa.txt","r",encoding="utf-8") as e:
    li = e.read().splitlines()
    print(li[1])

# 3.读文件
# with open("aa.txt","r",encoding="utf8",newline="")as f:
#     souce = f.read()#读取全部文件的内容
#     print(souce)
# print( f.readline())#读取1行
# print( f.readline(1))#读字符串 第一个
# print( f.readline(2))

    # li = f.readlines()#取出所有  并放在列表中
    # print(f.read().splitlines())
    # print(li)
    # for i in li:
    #     pass

#将aa.txt 文件复制到aaa中
# 复制照片

# 封装数据库中:用户名 密码  数据库名123456







