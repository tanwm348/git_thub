# 求5的阶乘
# 5*4*3*2*1
def dg(num):
    if num != 1:
        num = num*dg(num-1)
        return num
    else:
        return 1

print(dg(5))



# 一个小球从
# c表示次数  n 表示最终的高度 k 每次下落的高度
def work(c,n,k):
    if(c<10):
        return (c+1,n+k*2,k/2)
    return n

print(work(1,20,10))




























