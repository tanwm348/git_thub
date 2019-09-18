import unittest

class caculator():
    def divide(self,x,y):
        return  x/y



class TestCaculator(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("连接数据库")

    def test_divide_01(self):
        cal = caculator()
        # actural = cal.divide(10,5)
        # self.assertIsInstance(cal,caculator,"aaa")
        self.assertFalse(1==2,"aaaa")
        # self.assertEqual(actural,2,"断言失败的时候提示:测试失败")



    def test_divide_02(self):
        cal = caculator()
        actural = cal.divide(10,2.5)
        self.assertEqual(actural,2,"断言失败的时候提示:测试失败")


    def test_divide_03(self):
        cal = caculator()
        actural = cal.divide(10,0)
        self.assertEqual(actural,2,"断言失败的时候提示:测试失败")
    # @classmethod
    # def tearDownClass(cls):
    #     print("断开数据库")

if __name__ == '__main__':
    # unittest.main()
    # #实例化result类
    # r = unittest.TestResult()
    # TestCaculator("test_divide_01").run(result=r)
    #实例化runner
    runer = unittest.TextTestRunner()
    # 参数:测试用例或者测试用例集
    runer.run(TestCaculator("test_divide_01"))