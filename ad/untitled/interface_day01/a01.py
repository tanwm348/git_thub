class caculator():
    def divide(self,x,y):
        return  x/y



class jdj():

    def test(self):
        cal = caculator()
        cal = cal.divide(10,5)
        yq = 2
        if cal == yq:
            print("测试成功")

        else:
            print("测试失败")



if __name__ == '__main__':
    a = jdj()
    a.test()