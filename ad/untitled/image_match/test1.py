from PIL import ImageGrab,Image


#大图截图
#screen目录---放截图
#source 目录---模板图片
#保存
# im = ImageGrab.grab().convert("RGBA").save("./screen/1.png")

#打开图片
im1 = Image.open("./screen/1.png")
im2 = Image.open("./screen/1.png")
#获取图片大小
print(im1.size)
w,h = im1.size

# #不保存
imb = ImageGrab.grab().convert("RGBA")
pixes = imb.load()
print(pixes[0,0])


#加载图片像素
#
screen_pixes = im1.load()
target_pixes =im2.load()
print(target_pixes[0,0],screen_pixes)