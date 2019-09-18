import unittest


class Jenins(unittest.TestCase):

    def test1(self):
        result=[1,2,3]
        self.assertIn(1,result,"test1测试失败")
    def test2(self):
        result=1
        self.assertEqual(result,1,"test2失败")
    def test3(self):
        result=1
        self.assertIs(result,1,"test3测试失败")

if __name__ == '__main__':
    loder=unittest.TestLoader()
    suite01=loder.loadTestsFromTestCase(Jenins)
    runner=unittest.TextTestRunner()
    runner.run(suite01)




