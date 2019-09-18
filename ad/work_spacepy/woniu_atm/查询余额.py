from woniu_atm.mysql import *
def balance(log):
    print("当前余额为:")
    sql10 = "select money from woniu_atm where username = '%s'"%(log)
    a = select(sql10)
    print(a[0][0])
    # print(log)
# balance()
