# -*- coding : utf-8 -*-
# @Time      : 2020/11/1 9:07 PM
# @Auther    : zhuangniu
# @File      : oop.py

class House():
    # 类变量
    door = "red"
    floor = "white"

    # 构造方法
    def __init__(self):
        self.bed = "black"

    # 方法1
    def sleep(self):
        self.table = "green绿色"
        print("房间可以睡觉")
        print(f"房间可以在{self.table}桌子上吃饭")
        return "sleep end"
    # 方法2
    def cook(self):
        print(self.table)
        print(self.bed)
        print(self.floor)
        print("房子可以进行煮饭")

        return "cook end"


#   函数入口
if __name__ == "__main__":
    north_house = House()
    china_house = House()

    china_house.sleep()
    print("---------------------------我是挖煤的分割线---------------------------")
    north_house.sleep()
    print("---------------------------我是挖煤的分割线---------------------------")
    print(china_house.cook())
    print(china_house.sleep())
    print("---------------------------我是挖煤的分割线---------------------------")
    print(north_house.sleep())
    print(north_house.cook())