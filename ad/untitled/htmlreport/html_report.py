import time

import pymysql

class HtmlReport():

    def __init__(self):
        pass




    def write_data_to_db(self,version,casetype,module,caseid,casename,result,error,screen,runtime):
        runtime = self.get_now_time()
        sql = 'insert into htmlreport.html_report VALUES (default,"%s","%s","%s","%s","%s","%s","%s","%s",%s)'%(version,casetype,module,caseid,casename,result,error,screen,runtime)

        #建立连接
        con = pymysql.connect("localhost","root","123456",charset= "utf8")

        #创建游标
        cur = con.cursor()

        #执行sql

        cur.execute(sql)

        cur.close()
        con.close()


    #读取数据库
    def generate_report(self,version):
        con = pymysql.connect("127.0.0.1","root","123456",charset= "utf8")

        #创建游标
        cur = con.cursor()


        #获取对应版本号全部测试结果数据
        alldata_sql ="select*from htmlreport.html_report where version = '%s'"%(version)
        cur.execute(alldata_sql)
        all_data = cur.fetchall()
        # print(all_data)

        if len(all_data)>0:

            #执行时间
            runtime_sql = "select runtime from htmlreport.html_report where version = '%s' order by runtime desc limit 1"%(version)
            cur.execute(runtime_sql)
            runtime = cur.fetchone()[0]




            #执行用例总条数
            totalcase_sql = "select count(*) from htmlreport.html_report where version = '%s'"%(version)
            cur.execute(totalcase_sql)
            totalcase = str(cur.fetchone()[0])

             #执行成功数
            sucesscase_sql = "select count(*) from htmlreport.html_report where version = '%s' and result = '成功'"%(version)
            cur.execute(sucesscase_sql)
            sucesscase = str(cur.fetchone()[0])



            #执行失败数
            failcase_sql = "select count(*) from htmlreport.html_report where version = '%s' and result = '错误'"%(version)
            cur.execute(failcase_sql)
            failcase = str(cur.fetchone()[0])


            with open("./js_html/html2.html","r",encoding="utf8") as f:
                content = f.read()
                #执行时间
                content = content.replace("$time",runtime)
                # print(content)
                #总条数
                content = content.replace("$countTotal",totalcase)
                # print(content1)
                #执行成功数
                content = content.replace("$sucesscase",sucesscase)
                # print(content2)
                #执行成功数
                content = content.replace("$countFail",failcase)
                # print(content)


            #替换用例集结果
            case_content = '<tr height="30">\n'
                # print(content)
            # print(all_data)
            #data是每一行数据
            for data in all_data:
                #写入用例编号
                case_content = case_content+'<td width="10%">'+str(data[0])+'</td>\n'

                #写入版本号
                case_content = case_content+'<td width="10%">'+str(data[1])+'</td>\n'

                #写入登录模块

                case_content = case_content+'<td width="10%">'+str(data[2])+'</td>\n'


                #写入模块
                case_content = case_content+'<td width="10%">'+str(data[3])+'</td>\n'

                #写入用例id
                case_content = case_content+'<td width="10%">'+str(data[4])+'</td>\n'

                #写入用例名称
                case_content = case_content+'<td width="10%">'+str(data[5])+'</td>\n'

                #写入执行结果
                case_content = case_content+'<td width="10%">'+str(data[6])+'</td>\n'

                #写入错误结果

                case_content = case_content+'<td width="10%">'+str(data[7])+'</td>\n'

                #截图
                if  str(data[7]) == "无":

                     case_content = case_content+'<td width="10%">'+str(data[8])+'</td>\n'
                else:
                    case_content = case_content+'<td width="10%">'+"<a heaf = %s>"%("./js_html/1.png")+"</a>"+"点这里"+'</td>\n'

                #时间
                case_content = case_content+'<td width="10%">'+str(data[9])+'</td>\n'

                case_content = case_content+'</tr>'
            content1 = content.replace("$result",case_content)
            # print(content1)

            with open("./js_html/html3.html","w",encoding="utf8") as f:

                f.write(content1)


        cur.close()
        con.close()





    # 获取当前时间
    def get_now_time(self,format = "%Y%m%d %H:%M%:S"):
        now_time = time.strftime(format,time.localtime(time.time()))
        return now_time

if __name__ == '__main__':
    ht = HtmlReport()
    # ht.write_data_to_db()
    ht.generate_report("v1.0")