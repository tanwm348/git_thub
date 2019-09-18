'''
1.函数：
    函数是一些实现了一定功能的代码的集合

2.作用：
    提高代码的复用性，

3.语法：
    del 函数名（）：
        函数体

4.使用函数
    就是函数名（）

5.参数：
    可以通过参数去控制函数中的执行逻辑

6.调用其他文件中的函数
    from

7.返回值的问题

8.可变参数和不可变参数

9.全局变量和局部变量

10.必须参数   关键字参数   默认值参数   不定长参数

11.匿名函数：
  lambda a,b(a*b,b*2)

12.迭代器
    1.创建一个可迭代器
    2.读取里面的值
    每次读取都可以记住读取的位置，下一次读接着上一次的位置读

13.递归：自己调用自己 要有返回值

14.输出：sep   end

15.占位符：%s   %d    %f
'''

import pymysql

con = pymysql.connect("localhost","root","123456")

cur = con.cursor()

sql = "use z_woniu23_day06"

cur.execute(sql)

con.commit()
con.close()
cur.close()



















