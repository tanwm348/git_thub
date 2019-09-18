import pymysql



# 1. 封装对数据库 增删改 的操作
def change_mysql(sql,database="z_woniu23_day06"):
    con = pymysql.connect("localhost","root","123456")
    cur = con.cursor()
    cur.execute("use "+database)
    # cur.execute("use %s"%(database))
    num = cur.execute(sql)
    print(num)
    con.commit()
    cur.close()
    con.close()

def select(sql,database="z_woniu23_day06",num=-1):
    con = pymysql.connect("localhost","root","123456")
    cur = con.cursor()
    cur.execute("use "+database)
    cur.execute(sql)

    if num == -1:
        source = cur.fetchall()
    else:
        source = cur.fetchmany(num)

    con.commit()
    cur.close()
    con.close()
    return source



if __name__ == '__main__':
    print(111)
    

# 1. 插入数据
# sql = "insert into stu values (1,'老王',23),(1,'老王',23),(1,'老王',23)"
# change_mysql(sql)


# 2. 删除
# sql =  "delete from stu where age = 23"
# change_mysql(sql)

# 3. 查询:
# sql = "select * from stu"
# xx = select(sql,"z_woniu23_day06")
# print(xx)
































