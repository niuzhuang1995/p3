# -*- coding : utf-8 -*-
# @Time      : 2020/11/5 7:49 PM
# @Auther    : zhuangniu
# @File      : homework2.py

class  TongLao():
    def __init__(self):
        print("我只是个在童姥中的简单构造函数")

    def see_people(self,name):
        if name == "WYZ":
            print("师弟")
        elif name == "李秋水":
            print("师弟是我的！")
        else:
            print("丁春秋”，打印“叛徒！我杀了你")
    def fight_zms(self,enemy_hp,enemy_power,my_hp,my_power):
        my_hp = my_hp - my_hp * 2
        my_power = my_power + my_power * 10

        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if my_hp > enemy_hp:
            print("我获胜了")
        else :
            print("敌人获胜")

class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")


if __name__ == "__main__":
    xuzu = XuZhu()
    xuzu.see_people("李秋水")
    xuzu.fight_zms(1000,190,1000,200)