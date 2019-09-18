# a ="aAsmr3idd4bgs7Dlsf9eAF"
# arr = list(a)
# for i in range(len(arr)):
#     if arr[i].isupper():
#        arr[i].lower()
#     elif arr[i].islower():
#       arr[i].upper()
#
#
# print(arr)

# name = " aleX "
# print(name)
# a.移除name变量对应的值两边的空格，并输入移除有的内容
# print(name.lstrip())

# b.判断name变量对应的值是否以 "al"开头，并输出结果
# print(name.startswith("al"))

# c.判断name变量对应的值是否以 "X"结尾，并输出结果
# print(name.endswith("X"))

# d.将name变量对应的值中的 " l" 替换为 " p"，并输出结果
# print(name.replace("l","p"))

# e.将name变量对应的值根据 " l" 分割，并输出结果。
# print(name.split("l"))

# f.请问，上一题 e分割之后得到值是什么类型？
# print(type(name.split("l")))

# g.将name变量对应的值变大写，并输出结果
# print(name.upper())

# h.将name变量对应的值变小写，并输出结果
# print(name.lower())

# i.请输出name变量对应的值的第2个字符？
# print(name[:1])

# j.请输出name变量对应的值的前3个字符？
# print(name[0:2])

# k.请输出name变量对应的值的后2个字符？
# print(len(name))
# print(name[3:5])

# l.请输出name变量对应的值中 "e" 所在索引位置？
# print(name.index("e"))

li = ['alex','eric','rain']
# a.计算列表长度并输出
# print(len(li))

# b.列表中追加元素"seven"，并输出添加后的列表
# li.append("seven")
# print(li)

# c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
# li.insert(0,"Tony")
# print(li)

# d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
# li.insert(1,"Kelly")
# print(li)

# e.请删除列表中的元素"eric"，并输出修改后的列表
# li.remove("eric")
# print(li)

# f.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
# print(li.pop(1))
# print(li)

# g.请删除列表中的第3个元素，并输出删除元素后的列表
# print(li.pop(2))
# print(li)

# h.请删除列表中的第2至4个元素，并输出删除元素后的列表
# print(li.pop(1,2))
# print(li)

# i.请将列表所有的元素反转，并输出反转后的列表
# li.reverse()
# print(li)

# j.请使用for、len、range 输出列表的索引
# for i in range(len(li)):
#     print(i)

# k.请使用enumrate输出列表元素和序号（序号从 100 开始）
# for i,j in enumerate(li):
#     print(i,j)

# l.请使用for循环输出列表的所有元素
# for i in range(len(li)):
#     print(li[i])

# 3. 写代码，有如下列表，请按照功能要求实现每一个功能
li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
# a.请输出"Kelly"
# print(li[2][1][1])

# b.请使用索引找到 'all'元素并将其修改为"ALL"
# (li[2][2]) ="ALL"
# print(li)

u=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])

# a. 讲述元祖的特性
# 和列表差不多,有序可以重复,原组是不可改变的

# b. 请问 tu 变量中的第一个元素 "alex" 是否可被修改？可以
# li = list(u)
# li[0] = "a"
# print(li)

# c. 请问 tu 变量中的"k2"对应的值是什么类型？是否可以被修改？
# 如果可以，请在其中添加一个元素
# 字典
# li = list(u)
# print(li)
#
#
# li.insert()

# d. 请问 tu 变量中的"k3"对应的值是什么类型？是否可以被修改？
# 如果可以，请在其中添加一个元素 "Seven"
# key
li = list(u)


dic={'k1':"v1","k2":"v2","k3":[11,22,33]}

# a. 请循环输出所有的 key
# for i in dic:
#     print(i)

    # b. 请循环输出所有的 value
# for i in dic.keys():
#     print(dic[i])

    # c. 请循环输出所有的 key 和 value
# for i,j in dic.items():
#     print(i,j)

    # d. 请在字典中添加一个键值对， "k4":"v4"，输出添加后的字典
# dic["k4"] = "v4"
# print(dic)

# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic["k1"] = "alex"
# print(dic)

# f. 请在 k3 对应的值中追加一个元素 44，输出修改后的字典
# arr = list(dic["k3"])
# arr.append(44)
# dic["k3"] = arr
# print(dic)



# g. 请在 k3 对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# arr = list(dic["k3"])
# arr.insert(0,18)
# dic["k3"] = arr
# print(dic)



#1.使用while循环实现输出2-3+4-5+6.....+100的和
num = 0
while(True):
    for i in range(2,100):
       num = num+(i - (i+1))
    print(num)
    break



# 2.打印等腰三角形:  循环中使用一句话



