
# num = 5
#
# for i in range(num):
#     print(" "*(num-i-1),"*"*(i+i+1))



redball = 5
black = 8
white = 7
num = 0

for i in range(redball):
    for j in range(black):
        for k in range(white):
            if i+j+k == 10 & white>2 & black<3:
                num+=1

print(num)

# aa = 1987
# bb = 2
# cc = 25
# num = 0
# li = [31,29,31,30,31,30,31,31,30,31,30,31]
# li1 = [31,28,31,30,31,30,31,31,30,31,30,31]
#
# if aa%4==0:
#     print("是闰年")
#     for i in range(bb-1):
#         num = num+li[i]
#
# else:
#     print("不是")
#     for i in range(bb-1):
#         num = num + li1[i]
#
# num+=cc
# print(num)


