import base64

import requests
from Crypto.Cipher import AES

# url = "http://192.168.40.164:8080/testdemo/user/admin/2f6DhqPBNoK3f2A7FFqAXA=="
# res = requests.request("GET",url=url)
# print(res.text)


def add_to_16(s):
    '''
    调用AES加密算法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理，让它成为16的整数倍
    '''
    while len(s) % 16 != 0:
        s += (16 - len(s) % 16) * chr(16 - len(s) % 16)
    # 返回处理后的明文
    return s



#使用python模拟接口加密的过程
#加密算法 AES-ECB算法
#加密密钥 abcdefgabcdefg12
#对字节流
key = "abcdefgabcdefg12"
text = "123"

#加密的过程
#字符串明文->字节流明文->字节流密文


def encrypt(text):
    #实例化AES加密器,指定key和使用的模块
    aes = AES.new(key.encode("utf-8"),AES.MODE_ECB)

    #将字符串明文->字节流明文
    bytes_text = add_to_16(text).encode("utf-8")#16的整数倍
    # print(bytes_text)

    #加密   字节流明文->字节流密文
    encry_bytes_text = aes.encrypt(bytes_text)
    # print(encry_bytes_text)

    #使用base64对加密字节流进行编码
    base64_encry_bytes_text=base64.encodebytes(encry_bytes_text)
    # print(base64_encry_bytes_text)

    ##将base64编码成utf-8(二进制装换成密文字符串)
    data =base64_encry_bytes_text.decode("utf-8").replace('\n','')
    # print(data)
    return data

#发起登陆请求
password = encrypt(text)#明文密码->
# print(password)
url = "http://192.168.40.164:8080/testdemo/user/admin/%s"%(password)
res = requests.get(url)
print(res.text)






encrypt(text)