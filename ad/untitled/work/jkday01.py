import unittest
from HTMLTestRunner import HTMLTestRunner


class getsum:
    def __init__(self):
        self.list1 = [1, 2, 3]

    def myInsert(self, index1, num1):
        self.list2 = []
        self.list2.extend(self.list1)
        self.list2.insert(index1, num1)
        if len(self.list2)>index1:
            return self.list2
        else:
            return len(self.list2)



class TestCaculator(unittest.TestCase):
    def test_divide_01(self):
        ge = getsum()
        actural = ge.myInsert(0, 1)
        self.assertIn(1,actural, "断言失败的时候提示:测试失败")

    def test_divide_02(self):
        ge = getsum()
        actural = ge.myInsert(2, 3)
        self.assertIn(3,actural, "断言失败的时候提示:测试失败")

    def test_divide_03(self):
        ge = getsum()
        actural = ge.myInsert(3,4)
        print(actural)
        self.assertIn(3,actural, "断言失败的时候提示:测试失败")

    def test_divide_04(self):
        ge = getsum()
        actural = ge.myInsert(1, 2)
        self.assertIn(2,actural, "断言失败的时候提示:测试失败")

    def test_divide_05(self):
        ge = getsum()
        actural =ge.myInsert(4, 5)
        self.assertEqual(actural,4,"断言失败的时候提示:测试失败")


if __name__ == '__main__':
    # 测试用例加载器
    # loder = unittest.TestLoader()
    unittest.main()
    # 从测试类加载测试用例 参数:类名
    # suite01 = loder.loadTestsFromTestCase(TestCaculator)
    #
    # runner = unittest.TextTestRunner()
    #
    # # 实例化runner
    # with open("report.html","w",encoding="utf8") as f:
    #   runner=HTMLTestRunner(stream=f,verbosity=3,title="测试报告")
    #   runner.run(suite01)