import unittest
from HTMLTestRunner import HTMLTestRunner

def start():

    loder = unittest.TestLoader()
    suite02 = loder.loadTestsFromName("html.login_html")
    with open("report1.html","w",encoding="utf8") as f:
          runner=HTMLTestRunner(stream=f,verbosity=3,title="测试报告")
          runner.run(suite02)


if __name__ == '__main__':
    start()



