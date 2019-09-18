# from woniu_atm.mysql import*
# from woniu_atm.查询余额 import balance
#
# def transfer_accounts(username):
#
#
#     while True:
#         try:
#             print("转账")
#             name = input("请输入对方的账户名:")
#             sql = "select*from woniu_atm where username = '"+name+"'"
#             souce = select(sql)
#
#
#             if len(souce)>0:
#                 print("对方账户存在,开始转账")
#
#                 try:
#                     money = int(input("请输入转账金额:"))
#                 except ValueError as e:
#                     print("错了,写日志文件")
#
#
#
#
#                 #调用查询余额模块,判断余额是否大于等于转账的金额
#             sel_money = select(username)#自己的余额
#
#
#             if sel_money>= money:
#                 print("余额充足")
#
#                 #获取游标和连接
#                 con,cur = get_con_cur()
#                 try:
#                     sql1 = "use woniu_atm"
#                     sql2 = "update woniu_atm set money = money-%d"%()
#                     sql3 = "update woniu_atm set money = money+%d"%()
#
#                     run_sql(sql1,cur)
#                     run_sql(sql2,cur)
#                     run_sql(sql3,cur)
#
#                 except:
#                     #回滚
#                     con.rollback
#                     print("转账不成功")
#                 finally:
#                     #提交事务
#                     con.commit
#                     cur.close
#                     con.close
#
#                 print("提交事务")
#
#
#             else:
#                 print("余额不足,请充值")
#
#         else:
#             print("乱搞,重新输入")
#
#
#             except Exception as e:
#                 print(e)
#
# if__name__=='__main__':
#     transfer_accounts("老刘")
