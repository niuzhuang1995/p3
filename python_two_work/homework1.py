# -*- coding : utf-8 -*-
# @Time      : 2020/11/5 7:49 PM
# @Auther    : zhuangniu
# @File      : homework1.py

"""
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个

"""

class Person():
    #有参构造方法，需要传参
    """
    @name：姓名
    @sex ：性别类别标识
    @occupation：所属类别
    @age :年龄
    @dricks：饮品
    """
    def __init__(self,name,sex,age,occupation,dricks):
        self.name = name
        self.sex = sex
        self.age = age
        self.occupation = occupation
        self.dricks = dricks

    def eat(self):
        print(f"一个叫{self.name}的{self.occupation}要吃米饭")

    def drick(self):
        print(f"一个叫{self.name}的{self.occupation}要喝{self.dricks}")

if __name__ == '__main__':

    old_person = Person("老张头",'man',89,"老人","二锅头")
    old_person.eat()
    old_person.drick()
    print("----------------------我是完美的分割线------------------")
    smail_person = Person("小灰灰",'child',4,"小孩","牛奶")
    smail_person.eat()
    smail_person.drick()
    print("----------------------我是完美的分割线------------------")
    man_person = Person("张三",'man',24,'小伙子','啤酒')
    man_person.drick()
    man_person.eat()
    print("----------------------我是完美的分割线------------------")
    women_person = Person("张丽",'women',19,'女人','营养品')
    women_person.drick()
    women_person.eat()
    print("----------------------我是完美的分割线------------------")
    work_person = Person("打工人",'person',26,'人类','知识')
    work_person.drick()
    work_person.eat()



