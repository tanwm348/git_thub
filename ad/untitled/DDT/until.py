import datetime
import pymysql
import xlrd

from DDT.cintrol import *

class ExcelOperaten():
    def __init__(self,filename):
        self.fiename=filename


    #读取sheet表
    def read_excel(self,sheetname):
        book=xlrd.open_workbook(filename=self.fiename)
        # book.sheet_names()
        sheet=book.sheet_by_name(sheetname)
        return sheet

    #获取一行数据
    def get_excel_data(self,sheetname,row):
        sheet=self.read_excel(sheetname)
        row=sheet.row_values(row)
        return row

    #获取行数
    def get_nrows(self,sheetname):
        sheetname=self.read_excel(sheetname)
        return sheetname.nrows

    #获取所有页数
    def get_all_sheetnames(self):
        book=xlrd.open_workbook(self.fiename)
        return book.sheet_names()



    #请求正文切割
    def myDict(self,str):
        newlist = str.split("\n")
        mydic = {}
        for lis in newlist:
            newlist2 = lis.split("=")
            mydic[newlist2[0]] = newlist2[1]

        return mydic



    def select1(sql,database="milor",num=-1):
         # a = admin()
         # print(a)

         con = pymysql.connect("127.0.0.1","root","123456",charset = "utf8")
         cur = con.cursor()
         cur.execute("use"+database)
         cur.execute(sql)
         if num == -1:
              a = cur.fetchall()
         else:
              a = cur.fetchmany(num)
         con.commit()
         cur.close()
         con.close()
         return a





class Report():
    def __init__(self,report):
        self.report_path = report



    def add_report(self,info):

        with open(self.report_path,"a",encoding="utf8") as f:
            f.write(info)
            f.write("\n")









if __name__ == '__main__':
    pass
    eo = ExcelOperaten("woniu.xlsx")
    # re = Report("report1.txt")
    # re.add_report("aa")
    # n = eo.get_nrows("login")
    # print(n)
    book=xlrd.open_workbook("woniu.xlsx")