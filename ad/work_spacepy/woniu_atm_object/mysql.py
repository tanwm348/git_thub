import pymysql


def admin():
    # with open("aa.txt","a",encoding="utf-8") as f:
      with open("aa.txt","r",encoding="utf8")as f:
    #   f.write("localhost""\n")
    #   f.write("root""\n")
    #   f.write("123456")
        li =f.read().splitlines()
        return li



def select(sql,database = "atm",num=-1):
         li = admin()
         con = pymysql.connect(li[0],li[1],li[2])
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




