'''

二进制：
规定了8个开关 组成了一个字节

0 0 0 0     0 0 0 0


'''
#1.输出
# print("这是向控制台输入的东西")

#2.输入
# input("请输入")

#3.变量
aa = 1

#使用变量接受页面的值，然后输出到控制台
# aa =input("请输入")
# print(aa)

#变量取名：可以使用 a-z  A-Z 0-9 _

import keyword

print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def'
#  'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
#  'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try'













age=int(input('请输入你的年龄'))
if age >= 18 and  age < 100:
    print('你成年了')
elif age<18:
    print('你还要等%a多后才成年'%(18-age))
else:
    print('输入错误')
