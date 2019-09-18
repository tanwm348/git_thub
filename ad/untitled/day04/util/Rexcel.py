import xlrd


class rexcel:
    def read(self,path,index=0):
        #返回整个excel文件,其中包括多个sheet
        date = xlrd.open_workbook(path)
        #z获取整个sheet对象
        sheet = date.sheets()[index]
        return sheet
