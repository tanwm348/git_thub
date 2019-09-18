import os
#获取路径
path = os.path.abspath("../")+"\\cases\\"
# print(path)


#获取所有文件
file_list = os.listdir(path)
for file in file_list:
    if file !="_init_.py" and ".py" in file:
        os.system("python %s%s"%(path,file))