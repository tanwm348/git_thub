from woniu_atm.mysql import *
def vip(log):
    sql = "select vip from woniu_atm where username = '%s'"%(log)
    aa = select(sql)
    if aa[0][0]==1:

        print("当前vip等级为1")

    elif aa[0][0]==2:

        print("当前vip等级为2")

    elif aa[0][0]==3:

        print("当前vip等级为3")


    elif aa[0][0]==4:
        sql1 = "update woniu_atm set vip = %d where username = '%s'"%(4,log)
        change_mysql(sql1)
        print("当前vip等级为4")

    else:

        print("当前vip等级为5")