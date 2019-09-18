from woniu_atm.mysql import *
def drawmoney(log):
    num1 = int(input("请输入你要取的金额"))
    sql11 = "select money from woniu_atm where username = '%s'"%(log)
    dra = select(sql11)
    if dra[0][0]>0:
        num2 = dra[0][0]-num1
        sql12 = "update woniu_atm set money = %d where username = '%s'"%(num2,log)
        change_mysql(sql12)
        print("'%s'当前余额为%d"%(log,num2))
    else:
        print("账户余额不足")