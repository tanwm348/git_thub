import pymysql
# 1.需要导入模块

# 2.创建一个连接 连接数据库
# con = pymysql.connect("localhost","root","123456")

# 3.通过这个连接创建一个游标，这个游标可以执行数据库操作的命令
# cur = con.cursor()

# 4.写sql 创建一个数据库
# sql = "create database z_woniu23_day06"

# 5.执行数据库操作代码
# cur.execute(sql)

# 6.关闭游标  断开连接
# cur.close()
# con.close()

# 去数据库创建一张学生表
# con = pymysql.connect("localhost","root","123456")
#
# cur = con.cursor()
#
# sql1 = "use z_woniu23_day06"
# tab = "create table stu(sid int,sname char(20),age int)"
# cur.execute(sql1)
# cur.execute(tab)
# cur.close()
# con.close()

# 在学生表中添加3个数据
# li=[
#     {"name":"张三","age":18 ,"sid":1},
#     {"name":"李四","age":18 ,"sid":2},
#     {"name":"王五","age":18 ,"sid":3}
# ]
# con = pymysql.connect("localhost","root","123456")
# cur = con.cursor()
# sql1 = "use z_woniu23_day06"
# cur.execute(sql1)
# for i in  li:
#     # tab1 = "insert into stu values(%d,'%s',%d)"%(i["sid"],i["sname"],i["age"])
#     tab1 = "remove('张三')"
#     cur.execute(tab1)
#
# # 提交事务
# con.commit()
# cur.close()
# con.close()

# # 修改 和删除数据
#
# # 将数据库操作，封装到函数中：
# # 通过调用函数 实现增删改
#
#

# 查询：
con = pymysql.connect("localhost","root","123456")
cur = con.cursor()
sql2 = "use z_woniu23_day06"
sql1 = "select*from stu"
cur.execute(sql2)
cur.execute(sql1)#查询会将返回的结果 保存到 cur 中

source = cur.fetchmany(7)#会将游标中所有的内容取出来
print(source)
cur.close()
con.close()



