from woniu_atm.mysql import *
def savemaney(log):
   num = int(input("请输入要存的金额"))
   sm1 = "select money from woniu_atm where username = '%s'"%(log)
   sm2 = select(sm1)
   sm3 =(num) + sm2[0][0]
   if sm2[0][0]>1 and sm2[0][0]<1000:
         sm4 = "update woniu_atm set money = %d where username = '%s'"%(sm3,log)
         sql1 = "update woniu_atm set vip = %d where username = '%s'"%(1,log)
         change_mysql(sm4)
         change_mysql(sql1)
         print("'%s'当前余额为 %d"%(log,sm3))


   elif sm2[0][0]>1000 and sm2[0][0]<10000:
        sm4 = "update woniu_atm set money = %d where username = '%s'"%(sm3,log)
        sql1 = "update woniu_atm set vip = %d where username = '%s'"%(2,log)
        change_mysql(sql1)
        change_mysql(sm4)
        print("'%s'当前余额为 %d"%(log,sm3))


   elif sm2[0][0]>10000 and sm2[0][0]<100000:
        sm4 = "update woniu_atm set money = %d where username = '%s'"%(sm3,log)
        sql1 = "update woniu_atm set vip = %d where username = '%s'"%(3,log)
        change_mysql(sql1)
        change_mysql(sm4)
        print("'%s'当前余额为 %d"%(log,sm3))



   elif sm2[0][0]>100000 and sm2[0][0]<1000000:
       sm4 = "update woniu_atm set money = %d where username = '%s'"%(sm3,log)
       sql1 = "update woniu_atm set vip = %d where username = '%s'"%(4,log)
       change_mysql(sql1)
       change_mysql(sm4)
       print("'%s'当前余额为 %d"%(log,sm3))

   else:
       sm4 = "update woniu_atm set money = %d where username = '%s'"%(sm3,log)
       sql1 = "update woniu_atm set vip = %d where username = '%s'"%(5,log)
       change_mysql(sql1)
       change_mysql(sm4)
       print("'%s'当前余额为 %d"%(log,sm3))




