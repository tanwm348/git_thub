import  psutil
#top
# psutil.test()


#CPU 每3秒钟采集一次cpu使用率
cpu_per = psutil.cpu_percent(interval=3)
print(cpu_per)

#cpu使用时间百分比
cpu_times= psutil.cpu_times_percent()
print(cpu_times)

#内存
men  = psutil.virtual_memory()
print(men)

#网络
net = psutil.net_io_counters()
print(net)

#进程
pids = psutil.pids()
print(pids)




