# 集合

# 1.集合的特点:无序且不可重复 可去重

# 2.创建一个集合  并且初始化
# set1 = {1,2,3,4,5}

# 创建一个空集合
# set1 = set()

set1 = {3,2,8,6,9}
# print(set1)

# 使用集合 增删改查
set1.add("2")
print(set1)

# 将一个集合添加到另一个集合中 update()
# set1 = {3,2,8,6,9}
# set2 = {32,23,81}
# list1 = [122]
# # set1.update(set2)
# str = "afdsafa"
# set1.update(str)
# print(set1)


# 4.删除
set1 = {1,2,3,4,6,9}

#del set1 删除整个集合

# set1.clear()#清空集合
# print(set1)

#删除集合中的某个元素
# set1.remove(11) #如果没有对应的元素会报错

set1.discard(44) #删除 和remove一样,如果没有匹配到不会报错

print(set1)


# print(set1.pop())#随机删除并且返回这个删除的对象

#修改:一般情况都是将集合装换成列表

#使用删除+添加

# li = [1,2,5]
# print(li)
# set(li)
# print(type(li))

# set1 = {1,3,4,25,5,6,7}
# for i in set1:
#     print(i)

# set1 = {1,4,2,7,8}
# set2 = {2,4,6}
# set1.union(set2)#并集
# print(set1)

# set1.intersection(set2)#交集
# print(set1)