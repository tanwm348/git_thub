# def mysql1(a,sqll,database = "z_woniu23_day06"):
#      import pymysql
#      con = pymysql.connect("localhost","root","123456")
#      cur = con.cursor()
#      cur.execute("use %s"%database)
#      cur.execute(a)
#
#      cur.execute(sqll)
#      con.commit()
#      cur.close()
#      con.close()
#
#
# sql = "insert into stu values(4,'张三',1),(5,'李四',1),(6,'王五',1)"
# sql2 = ("update stu set sname ='张' where sname ='李四'")
# sql3 = ("delete from stu where sname = '李四'")
#
# xx= mysql1( sql,"select*from stu")
# print(xx)
#


def select(sql,database = "atm",num=-1):
     import pymysql
     con = pymysql.connect("localhost","root","123456")
     cur = con.cursor()
     cur.execute("use "+database)
     cur.execute(sql)
     if num == -1:
          a = cur.fetchall()
     else:
          a = cur.fetchmany(num)
     # source = cur.fetchmany(3)
     #
     # source2 = cur.fetchall()
     con.commit()
     cur.close()
     con.close()
     return a

sql = "select*from stu"
aa = select(sql,"woniu_atm",num = -1)
