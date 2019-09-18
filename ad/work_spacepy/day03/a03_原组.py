# 原组
# 1.原组的特点
#     和列表差不多,有序可以重复,原组是不可改变的

# 2.创建并且初始化一个原组
# tup = (1,2,3,5,4,8)
# print(tup)

# 3.使用原组,可以使用下标获取里面的元素
# print(tup)
#
# print(tup[3])

# 4.原组的切片
# print(tup[:])
# print(tup[::-1])

# 5.增 删 改 都是非法操作


# 6.查询:
# tup.index()
# tup.count()

# 7.遍历原组
tup = (1,2,3,5,4,8)
print(tup)
# for i in tup:
#     print(i)

# 8.类型转换
tup = (1,2,3,5,4,8)
arr = list(tup)
print(arr)


a= tuple(arr)#转换成 tuple


如果原组只有一个值,需要添加一个逗号
tup = (5,)