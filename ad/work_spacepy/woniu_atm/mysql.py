import pymysql
# from woniu_atm.需求分析 import admin
def select(sql,database = "atm",num=-1):
     # a = admin()
     # print(a)

     con = pymysql.connect("localhost","root","123456")
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

def change_mysql(sql,database="atm"):
    con = pymysql.connect("localhost","root","123456")
    cur = con.cursor()
    cur.execute("use "+database)
    # cur.execute("use %s"%(database))
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()


def get_con_cur():
    con = pymysql.connect("localhost","root","123456")
    cur = con.cursor()
    return cur,con


def run_sql(sql,cur):
    cur.execute(sql)


def con_commit(cur,con):
    con.commit()
    cur.close()
    con.close()




