#字符串

# 1.字符串的类型 str

# 2.切片 根据下标来获取里面的字串

# st = "abcdefg"
# print(st[0])= a
# print(st[3])= d
# print(st[3:5]) = de
#print(st[3:]) = defg

# st = "0123456789"
# print(st[0:10:2]) # =0 2 4 6 8  参数：1：开始下标 2.结束下标 3.步长（几个数开始取）
                                #左闭右开
# 求02468
# print(st[::2])
#求6543
# print(st[6:2:-1])
# 求86420
# print(st[8::-2])

# string = "张三，李四，王五"
# print(string[0:2:1])

# 字符串的常用函数和方法

# 常用函数：

# 1.获取字符串的长度:len()
# string = "abcde"
# print(len(string))
#
# print(max(string))#比较的是ASCII码
# print(min(string))

# 2.常用的方法：
# st = "123456789"
# str1 = "89"
 # 2.1.查找某个字串在另一个字符串的第一次出现的位置
 # find()
#print(st.find(str1,6,10)) = 7 切片  从下标为6开始，到下标为10 查找str1的下标
# 参数1：被查找的字串  参数2：从哪里开始查  参数3：到哪里结束
# 如果没有查到返回-1
# 地址 输出重庆市
# aaa = "重庆市红旗河沟"
# num = aaa.find("市")
# print(aaa[:num+1])

# 2.查询 index 和find用法一样，区别：如果没有查询到 会报错
# index()
# st = "123456789"
# str1 = "89"
# print(st.find("2"))
# print(st.index(str1,6,10))

# 3.输出一个固定长度的字符串，并且让内容居中。如果长度不够 用其他填充
# center()
# 参数1：表示要输出字符串的长度
# 参数2：表示多余的长度用什么来填充
# str1 = "aaabbb"
# str2 = str1.center(30,"o")
# print(str2)

# 4。统计某个子串在另一个串中出现的次数:count()
# 参数和find一样 有3个
# str1 = "adsacavabadsabadsa"
# str2 = "ab"
# print(str1.count(str2,2,9))

# 5.切割字符串：split()
# 参数1 ：按照某个元素来切  参数2：最多切割的次数
# str1 = "aa,bb,cc,1,2"
# str2 = str1.split(",",4)
# print(str2)
# print(type(str2))

# 6.替换字符串：replace()
# 参数1：被替换的子串
# 参数2：替换之后的内容
# 参数3：最多替换的次数

# str1 = "aa/bb/cc/dd/ee"
# str2 = str1.replace("/","||||",3)
# print(str2)

# 7.判断某个串是否全是字母，或者全身数字 或者 数字和字母的组合
# str1.isnumeric()数字  str1.isalpha()字母   str1.isalnum()组合
# str1 = "222"
# str2 = str1.isnumeric()#数字
# str3 = str1.isalpha()#字母
# str4 = str1.isalnum()#组合
# print(str2)
# print(str3)
# print(str4)

# 8. 判断这个串的字母是否全身大写或小写
# str1.isupper()#大写  str1.islower()#小写
# str1 = "abcd"
# a = str1.isupper()#大写
# b = str1.islower()#小写
# print(a)
# print(b)

# 9.将某个串中的所有字母变成大写或者小写
# str1.upper() 大写  str1.lower()#小写
# str1 = "asdFSAFsffvs"
# a = str1.upper()#大写
# b = str1.lower()#小写
# print(a)
# print(b)

# 10.判断某个串是否以某个字符开头或者结尾
# 参数：和fine一样
# str1 = "asdFSAFsffvs"
#
# a = str1.startswith("a",0,10)
# b = str1.endswith("s",0,2)
#
# print(a)
# print(b)

# 11.截掉字符串左边的空格或指定字符
# str1 = "   dasdad"
#
# b = str1.lstrip()
# print(str1)
# print(b)

# 12.删除字符串末尾的空格
# str1 = "sdas"
# str2 = "aadaasaa"
# a = str2.strip("a")
# # print(str1)
# print(a)


# 4.字符串的拼接：
# aa = "aaa"
# bb = "bbb"
# cc = "ccc"
# 如果在字符串中需要输出一些特殊的字符，需要使用\：转义字符
# print("这是aa的值:"+aa+"这是bb的值：" +bb+"这是cc的值："+cc)
#
# print("这是\"aa\"的值:"+aa+"这是bb的\\值：" +bb+"这是cc的值："+cc)

# print("a"*5) #复制5个a
#
# print(r"a" "b")


a  = "2222333444"

print(a.find("2",0,len(a)))