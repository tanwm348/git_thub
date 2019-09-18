import pymysql
# from woniu_atm.需求分析 import admin
def select(sql,database = "milor",num=-1):
     # a = admin()
     # print(a)

     con = pymysql.connect("127.0.0.1","root","123456",charset = "utf8")
     cur = con.cursor()
     cur.execute("use "+database)
     cur.execute(sql)
     if num == -1:
          a = cur.fetchall()
     else:
          a = cur.fetchmany(num)
     con.commit()
     cur.close()
     con.close()
     return a
