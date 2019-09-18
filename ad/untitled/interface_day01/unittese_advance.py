import unittest


from interface_day01 import unittest_base
from HTMLTestRunner import HTMLTestRunner


class Teacher(unittest.TestCase):
    @unittest.skip("强制跳过")
    def test_teather(self):
        print("teather1")

    @unittest.skipIf(1>2,"满足条件则跳过")
    def test_teather1(self):
        print("teather2")

    @unittest.skipUnless(1>2,"不满足条件跳过")
    def test_teather2(self):
        print("teather3")



class Student(unittest.TestCase):
    def test_student(self):
        print("student1")


    def test_student1(self):
        print("student2")


    def test_student2(self):
        print("studnet3")


if __name__ == '__main__':
    #测试用例加载器
    loder = unittest.TestLoader()


    #从模块加载测试用例--参数:模块名称,不能是自己  必须是其他模块
    suite01 = loder.loadTestsFromModule(unittest_base)

    #通过路径加载测试用例,可以加载模块,类,某个具体测试方法 参数,包名,模块名称,类名,方法名
    suite02 = loder.loadTestsFromName("unittest_base.TestCaculator")


    # suite04 = loder.loadTestsFromNames(["interface_day01.unittest_base.TestCaculator','unittese_advance"])



    #从测试类加载测试用例 参数:类名
    suite03 = loder.loadTestsFromTestCase(Student)


    runner = unittest.TextTestRunner()
    # runner.run(suite02)

  #   实例化runner
    with open("report1.html","w",encoding="utf8") as f:
      runner=HTMLTestRunner(stream=f,verbosity=3,title="测试报告")
      runner.run(suite02)



    # unittest.main()

    # #实例化一个测试套件--装载测试用例容器
    # suite = unittest.TestSuite()
    #
    # #参数是测试用例和测试用例集--单数,只能跑一条测试用例
    # # suite.addTest(Teacher("test_teather1"))
    #
    # #参数元组或者列表
    # list = [Teacher("test_teather2"),Student("test_student1")]
    #
    # #添加测试用例
    # suite.addTests(list)
    #
    # #实例化runner
    # runner = unittest.TextTestRunner()
    #
    # #参数是单条测试用例或者多条测试用例(测试用例集)
    # runner.run(suite)

    # 需求 执行Teacher类的test02和student类里面的test01



    #装饰器:不改变原来的函数却能添加新的功能


    #报告--h5测试报告(html)



