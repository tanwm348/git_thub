'''
数据类型：
number: int  float
string:str
list:列表
tuple:原组
set:集合
dsctionary: dict 字典
bool:布尔

'''
# 1.list 和js的数组差不多
# 1.1 创建一个列表
# arr = [1,2,3,4,5,6,7,8,9]
# 学习存储结构的顺序：增 删 改 查
# 列表的特点：有序可重复

# 2.1如何使用列表，根据下标可以取出里面的元素
# print(arr[1])

# 3.列表的切片
# print(arr[:])#所有
# print(arr[::-1])#倒序
# print(arr[1::2])#2468
# print(arr[::-2])#97531

# 4.常用函数
# arr = [1,2,3,4,5,6,7,8,9]
#
# print(max(arr))
# print(min(arr))
# str1 = "12345"
# print(str1)
# print(list(str1))
# print(int(str1))

# 5.常用的方法
# 5.1 增 append()
# arr = [1,2,3,4]
# arr.append("555")#在末尾增加数据
# print(len(arr))
#
# # 在中间添加数据 根据下标
# arr.insert(2,"666")#中间
# arr.insert(0,"sds")#开头
# arr.insert(len(arr),"ds")#末尾
# print(arr)

# arr = [1,2,3,4]
# arr2 = [1,2,3,9]

# 将一个列表更新到另一个列表中
# arr.extend(arr2)# arr = 12341239
# print(arr)
# print(arr2)
#得到两个列表的和，不会修改列表本身
# print(arr+arr2)


# 5.2 删
#1. 根据下标删除某个元素  del
# arr = [1,2,3,4]
# del arr[0]
# # del arr
# print(arr)

# 2.清空列表: clear()
# arr.clear()
# print(arr)

# 3.根据匹配的元素删除 ,移除第一个匹配上的元素 remove()

# arr = [1,"2",3,4]
# fccccccccccf
# print(arr)
# 4.根据下标删除某个元素并返回该元素   pop(num) 有返回值
# arr = [1,2,3,4,5,6]
# print(arr.pop(0))
# print(arr)



# 5.3 改
# arr = [1,2,3,4,5,6]
# arr[1] = 3
# print(arr)

# 5.4 查
# 1.查询这个列表里面是否包含某个子元素,返回这个子元素的下标
# 注意:是第一次匹配到的位置 和前面的用法一样,没有找到会报错
# arr = [1,2,3,4,6,4]
# a = arr.index(4)
# print(a)

# 2.统计 和前面一样
# print(arr.count(4))

# 3.遍历列表
# arr = ["张三","李四","王五","老刘","张三",]
# for i in range(len(arr)):
#     if arr[i]=="张三":
#        arr[i] = "三儿"
#
# print(arr)


# arr = ["张三","李四","王五","老刘","张三",]
# num = arr.count("张三")
# for i in range(num):
#     arr.remove(arr[i])
#
# print(arr)


# arr = ["张三","李四","王五","老刘","张三",]
# for i in range(len(str)):
#     if arr[i]=="张三":
#         arr.remove(arr[i])
#
# print(arr)



# 6.排序 sort()默认升序   reverse()将顺序反转
# arr = [1,3,2,4,5]
# arr.sort()
# print(arr)

# arr.reverse()
# print(arr)

# arr.sort(reverse = True)
# print(arr)
arr = [1,9,3,7,5,3]
arr.sort(reverse=True)
print(arr)
#
# print(arr)
# num = 0
# for i in range(len(arr)-1):#循环次数
#     for j in range(len(arr)-1-i):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j];
#
#
#
#
# print(arr)
# arr1 =set(arr)
# print(arr1)
# def sum(aa,bb,cc):
#     print(aa,bb,cc)
#
# sum(aa =1,bb=2,cc=2)