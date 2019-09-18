'''
编程可以分为面向对象 和面向过程
高级语言中都是面向对象编程
高级语言中:万物皆对象

面向对象三大特征: 封装  继承  多态

封装:就是将属性和函数封装到一个抽象的类中,
     对外界隐藏功能实现的细节


'''

# 1.如何去创建一个对象
# 人类:
# 属性:名字 年龄  性别  (程序中属性:变量)
# 功能:吃饭 走路  睡觉  (函数)
# class Persion():
#     name = "人"
#     age = 0
#     sex = "男"
#
#     def eat(self):
#         print("吃饭")
#
#     def walk(self):
#         print("走路")
#
#     def self_interduce(self):
#         print("你好!我叫%s,我今年%d岁"%(self.name,self.age))

# 通过类创建一个人出来(相当于通过模具去创建产品)
# 创建对象:也叫实例化对象
# persion = Persion()
# persion1 = Persion()
# 2.对象来访问自己的属性
# persion.name
# persion.age

# 3.对象访问自己的方法
# persion.self_interduce()
# persion.eat()

# 4.查看对象的类型
# print(type(persion))#是 Persion

# 5.修改属性值 获取这个属性的值 然后重新赋值
# persion.name = "张三"
# print(persion.name)

# 5.初始化方法
# 实例化对象就会执行__init__方法
# class Persion():
    # name = "人"
    # age = 0
    # sex = "男"
#     def __init__(self,sname,sage,ssex):
#         self.name = sname
#         print(sname)
#         self.age = sage
#         print(sage)
#         self.sex = ssex
#         print(ssex)
#
#         print("初始化方法执行,注意他的执行时机")
#
#     def eat(self):
#         print("%s在吃饭"%(self.name))
#
#     def walk(self):
#         print("%s在走路"%(self.name))
#
#     def self_interduce(self):
#         print("你好!我叫%s,我今年%d岁 是个%s的"%(self.name,self.age,self.sex))
#
# per1 = Persion("张三",12,"男")
# per2 = Persion("李四",12,"女")
# # print(per1.name)
# print(per2.sex)
# per1.self_interduce()
# per2.self_interduce()
# per1.eat()
# per1.walk()
# per2.eat()
# per2.walk()

# 6.类属性和对象属性
# class Persion():
#     name = "人"
#     age = 0
#     sex = "男"
#     def __init__(self,sname):
#         self.name = sname
#         print("初始化方法执行,注意他的执行时机")
#
#     def eat(self):
#         print("%s在吃饭"%(self.name))
#
#     def walk(self):
#         print("%s在走路"%(self.name))
#
#     def self_interduce(self):
#         print("你好!我叫%s,我今年%d岁 是个%s的"%(self.name))
# # 访问类型属性
# print(Persion.name)
#
# per = Persion("张三")
# print(per.name)
# #如果对象有这个属性就去访问对象属性,如果对象没有就去类中找
# print(per.age)#age = 0
# print(Persion.name)
#

# 7.访问类方法
# class Persion():
#     name = "人"
#     age = 0
#     sex = "男"
#     def __init__(self,sname):
#         self.name = sname
#         print("初始化方法执行,注意他的执行时机")
#
#     def eat(self):
#         print("%s在吃饭"%(self.name))
#
#     def walk(self):
#         print("%s在走路"%(self.name))
#
#     def self_interduce(self):
#         print("你好!我叫%s,我今年%d岁 "%(self.name,self.age))
# per = Persion("张三")
# per1 = Persion("张四")
# per.self_interduce()
# per1.self_interduce()


# 8.私有化属性
# 私有化之后,属性就不可以通过对象.属性名的方法去访问和修改值
# ,但是在函数内部是可以访问的 一般在内修改
# 如果需要获取或者修改值,可以在来中定义一个取值的函数:getName()
#                         和一个设置值的函数:setName()

# class Persion():
#     def __init__(self,sname,age):
#         self.name = sname
#         self.__age = age
#         print("初始化方法执行,注意他的执行时机")
#     #获取年龄的值
#     def getAge(self):
#         return self.__age
#     #修改年龄的值
#     def setAge(self,age):
#         if age>0 and age<120:
#             self.__age = age
#         else:
#             self.__age = 0
#
#
#     def self_interduce(self):
#         print("你好!我叫%s,我今年%d岁 "%(self.name,self.__age))
#
# per = Persion("张三",10)
# print(per.getAge())
# per.setAge(140)
# print(per.getAge())
# per.self_interduce()


#9.继承 单继承
# class Animal():
#     def __init__(self,name):
#         print("动物类初始化开始")
#         self.name = name
#         print("动物类初始化结束")
#
#
# class Persion(Animal):
#     def __init__(self,name,age):
#         print("人类类初始化开始")
#         self.age = age
#         Animal.__init__(self,name)
#         print("人类类初始化结束")
#
# per = Persion("张三",18)
# print(per.name,per.age)

# 10.多继承
# 注意: 如果父类有相同的属性 属性中的值会执行后面那个父类中属性的值
#         因为后执行会覆盖前面的值
# class Animal():
#     def __init__(self,name):
#         print("动物类初始化开始")
#         self.name = "动物"
#         print("动物类初始化结束")
#
# class Animal1():
#     def __init__(self,name):
#         print("动物1类初始化开始")
#         self.name = "动物1"
#         print("动物1类初始化结束")
#
# class Persion(Animal,Animal1):
#     def __init__(self,name,age):
#         print("人类类初始化开始")
#         self.age = age
#         Animal.__init__(self,name)
#         Animal1.__init__(self,name)
#         print("人类类初始化结束")
#
# per = Persion("张三",18)
# print(per.name,per.age)

# 10.1多继承
# class Animal():
#     def __init__(self,name,*args,**kwargs):
#         print("动物类初始化开始")
#         self.name = "动物"
#         print("动物类初始化结束")
#
# class Animal1(Animal):
#     def __init__(self,name,*args,**kwargs):
#         print("动物1类初始化开始")
#         self.name = "动物1"
#         super().__init__(self,name,*args,**kwargs)
#         print("动物1类初始化结束")
#
# class Animal2(Animal):
#     def __init__(self,name,*args,**kwargs):
#         print("动物2类初始化开始")
#         self.name = "动物2"
#         super().__init__(self,name,*args,**kwargs)
#         print("动物2类初始化结束")
#
# class Persion(Animal1,Animal2):
#     def __init__(self,name,age):
#         print("人类类初始化开始")
#         self.age = age
#         super().__init__(self,name,age)
#         print("人类类初始化结束")
#
# per = Persion("张三",18)
# print(per.name,per.age)
# print(Persion.mro())

# [<class '__main__.Persion'>, <class '__main__.Animal1'>,
# <class '__main__.Animal2'>, <class '__main__.Animal'>,
# <class 'object'>]

# 11.继承中调用父类方法:
# 注意:调用属性 后面的会覆盖前面的
# 但是:调用方法,调了一个就不会去找了 覆盖不了

# class Animal():
#     def __init__(self,name):
#         print("动物类初始化开始")
#         self.name = name
#         print("动物类初始化结束")
#     def eat(self):
#         print("吃饭")
#
# class Animal1():
#     def __init__(self,name):
#         print("动物1类初始化开始")
#         self.name = name
#         print("动物1类初始化结束")
#     def eat(self):
#         print("吃1")
#
# class Persion(Animal,Animal1):
#     def __init__(self,name,age):
#         print("人类类初始化开始")
#         self.age = age
#         Animal.__init__(self,name)
#         print("人类类初始化结束")
#
# per = Persion("老王",1)
# print(per.name)
# per.eat()


# 12.方法重写:如果父类方法不能满足之类的需求,在子类中可以对父类的方法进行重写

# class Animal():
#     def __init__(self,name):
#         print("动物1类初始化开始")
#         self.name = name
#         print("动物1类初始化结束")
#     def eat(self):
#         print("吃")
#
#
# class Persion(Animal):
#     def __init__(self,name,age):
#         print("人类类初始化开始")
#         self.age = age
#         Animal.__init__(self,name)
#
#         print("人类类初始化结束")
#     def eat(self):
#         print("斯文的吃")
#
# per = Persion("张三",18)
# print(per.name,per.age)

# 13.调用父类的方法
# super(Persion,per).eat()


# 14.多态 :多态的条件 封装 继承 重写
# class Animal():
#     def __init__(self,name):
#         print("动物类初始化开始")
#         self.name=name
#         print("动物初始化方法结束")
#     def eat(self):
#         print("吃")
# class Person(Animal):
#     def __init__(self,age,name):
#         print("人类初始化开始")
#         self.age=age
#         Animal.__init__(self,name)
#         print("人类初始化方法结束")
#     def feed(self):
#         print("斯文的吃")
#
# class Cat(Animal):
#     def eat(self):
#         print("舔猫")
#
# class Dog(Animal):
#     def eat(self):
#         print("舔狗")



# cat=Cat("老谭")
# dog=Dog("老王")
# cat.eat()
# dog.eat()

#15.python是一种动态语言
# class Persion():
#     def __init__(self,age):
#         print("人类类=初始化开始")
#         self.age = age
#     def eat(self):
#         print("斯文的吃")
# per = Persion
# per.name = "老刘"#可以动态的给对象添加属性
# print(per.name)

# 作业:先做大纲  复习   练习使用面向对象思想重构atm

