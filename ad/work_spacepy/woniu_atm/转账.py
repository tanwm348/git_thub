from woniu_atm.mysql import *
def getmoney(log):
    gname = input("请输入要转账的用户名:")
    sql17 = "select * from woniu_atm where username = '%s'"%(gname)
    bb = select(sql17)
    if len(bb)>0:
        gnum = int(input("请输入转账金额"))
        sql13 = "select money from woniu_atm where username = '%s'"%(log)
        aa = select(sql13)
        if aa[0][0] >= gnum:
            sql14 = "select money from woniu_atm where username = '%s'"%(gname)
            bb = select(sql14)
            gnum2 = aa[0][0] - gnum
            sql15 = "update woniu_atm set money = %d where username = '%s'"%(gnum2,log)
            change_mysql(sql15)
            gnum3 = bb[0][0] + gnum
            sql16 = "update woniu_atm set money = %d where username = '%s'"%(gnum3,gname)
            change_mysql(sql16)
            print("'%s'当前余额为%d"%(log,gnum2))
            return gnum

        else:
            print("账户余额不够")
    else:
        print("用户不存在")



