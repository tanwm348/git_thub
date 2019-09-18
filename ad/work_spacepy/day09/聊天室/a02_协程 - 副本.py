'''
# 应用场景:

切换时间: 进程 > 线程 > 协程

进程:

线程:

协程:

程序分为:

cpu 密集型  : 要使用多核计算能力  使用多进程  线程:
io密集型  :  协程:  线程:

'''










# 协程: 一个线程中有多个任务,如果某个任务遇到了耗时操作就去执行其他任务
#   如果没有遇到耗时操作, 不会跳转 直接按照顺序执行完

# 以个进程中有 3个线程


# import gevent
#
# from gevent import monkey
# monkey.patch_all()   # 打补丁, 将以前的耗时操作 转换成 gevent模块中的耗时操作
#
# import time
#
# def sing():
#     for i in range(5):
#         print("来啊, 快活啊..........")
#         # time.sleep(1)
#         gevent.sleep(1)
# def dance():
#     for i in range(5):
#         print("谈恋爱不如跳舞.........")
#         # time.sleep(1)
#         gevent.sleep(1)
# g1 = gevent.spawn(sing)
# g2 = gevent.spawn(dance)
#
# g1.join()
# g2.join()
#
# print("线程执行结束")

# 老杨开厂: 电脑组装厂

# 工作台, 工具 cpu 显卡 内存 还有wi这个人 可以开始生产 等等    进程
#  老杨在组装,老杨就是一个                                 线程

# 生意太好: 去找了几个学生 一起来组装电脑,  把组装电脑 分为几个步骤, 每个人去做一个   多线程
#     多个人: 共用工具:  理解为 共享全局变量

# 小云来订单: 业务太好  , 我将我的流水线 按照第一条 全部复制几条在旁边  : 多进程

# 流水线上 有的员工 动作太快,做完了之后会在哪里等着, 那么这个时候 可以给他安排其他任务, 将空闲时间利用起来




import  urllib.request
import gevent
from gevent import monkey
monkey.patch_all()  # 打补丁

def downloader(img_name, img_url):
    print(111,gevent.getcurrent())
    req = urllib.request.urlopen(img_url) #传入需要下载文件的路径
    print(222,gevent.getcurrent())
    img_countent = req.read()
    print(333,gevent.getcurrent())
    with open(img_name,"wb") as f:
        print(444,gevent.getcurrent())
        f.write(img_countent)

def main():
    gevent.joinall([
        gevent.spawn(downloader,"1.jpg","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548240597482&di=5d9e289fdceea8f560e2677bd16b425f&imgtype=0&src=http%3A%2F%2Fimg.besoo.com%2Ffile%2F201807%2F16%2F3wph4pihzes.jpg"),
        gevent.spawn(downloader,"2.jpg","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548240711253&di=e7573f190ee4a7637d54f2f17bc77cd0&imgtype=0&src=http%3A%2F%2Fpic.feizl.com%2Fupload%2Fallimg%2F180126%2Ftdtghtf0crb.jpg"),
        gevent.spawn(downloader,"3.jpg","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548240711253&di=e7573f190ee4a7637d54f2f17bc77cd0&imgtype=0&src=http%3A%2F%2Fpic.feizl.com%2Fupload%2Fallimg%2F180126%2Ftdtghtf0crb.jpg"),
        gevent.spawn(downloader,"4.jpg","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548240711253&di=e7573f190ee4a7637d54f2f17bc77cd0&imgtype=0&src=http%3A%2F%2Fpic.feizl.com%2Fupload%2Fallimg%2F180126%2Ftdtghtf0crb.jpg")
    ])



if __name__ == '__main__':
    main()
    # img_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548240711253&di=e7573f190ee4a7637d54f2f17bc77cd0&imgtype=0&src=http%3A%2F%2Fpic.feizl.com%2Fupload%2Fallimg%2F180126%2Ftdtghtf0crb.jpg"

    # img_url = "http://k.zol-img.com.cn/sjbbs/7692/a7691515_s.jpg"
    #
    # downloader("aa.jpg", img_url)





















































