#字典特点:每个元素都是由一个键值对(,为界)组成的
# key:数据类型只能是不可变类型(字符串/数字/元组)
# 一般使用字符串 key不能重复(姓名)
# value:可以是任意数据类型
# 1.创建一个字典
# dic = {"姓名":"张三","age":18,"sex":"男","爱好":["打球","看书","唱歌"]}
# print(type(dic))

# 2.创建一个空字典
# xx = {}

# 如何使用字典

# 1.像字典中添加数据
dic = {"姓名":"张三","age":18,"sex":"男","爱好":["打球","看书","唱歌"]}
#
# dic["体重"] = 120
#
# print(dic)

# 2,修改
# dic["姓名"] = "三儿"
# print(dic)

# 3.删除数据
# del dic["体重"]
# print(dic)


# print(dic.pop("sex"))#按照某个键 删除对应的值

# print(dic.popitem())#随机删除一个元素,会将整个元素以元组的形式返回

# 4.查询
# 取出里面的内容
# print(dic["age"])
# print(dic.get("age"))

# 遍历字典
# for i in dic:
#     print(i)
#     print(dic[i])

print(dic.keys(sw))  #输出键
for i in dic.keys():
    print(dic[i])

# print(dic.items)#拿出全部内容
# for i,j in dic.items():
#     print(i,j)


# dic = {"姓名":"张三","age":18,"sex":"男","爱好":["打球","看书","唱歌"]}
# print(dic["爱好"][1])

# li = [[1,2,3],[4,5,6],[7,8,9]]
#
# print(li[0][1])
# 人类：
# li = [
# {"姓名":"张三","age":18},
# {"姓名":"李四","age":19},
# {"姓名":"李四","age":19},
# {"姓名":"李四","age":19},
# {"姓名":"李四","age":19}
# ]
# # 找到名字为 张三 将他的年龄修改成50
# for i in li:
#     print(i)
#     # print(li)
#     # if i["姓名"] == "张三":
#     #     i["age"] = 20
#
# print(li)


# 队列：先进先出


# 栈：先进后出


# 使用列表来做一个队列和栈

# li = []
#
# li.extend("ad")
# li.pop(1)
# print(li)

# username = ["aa","bb","cc"]用户名
# userpwd = ["123","456","789"]
# 从页面接受一个用户和密码
# 判断 用户名和密码是否正确
#  如果正确提示登录成功
#  如何错误：提示错误的原因，继续输入
# 用户名和密码错误次数 总共可以错3次


# 使用*在控制台打印直角三角形和等腰三角形

