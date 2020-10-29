# -*- coding : utf-8 -*-
# @Time      : 2020/10/29 1:20 AM
# @Auther    : zhuangniu
# @File      : test.py

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power

"""
import random

#执行的函数
def game_numone(enemy_hp,enemy_power):
    my_hp = 1000
    my_power = 200

    while True:
#循环减少血量
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
#判断是否结束
        if my_hp<= 0 or enemy_hp <= 0:
            print("游戏结束")
            if my_hp < enemy_hp :
                print("敌人获胜")
                break
            elif my_hp == enemy_hp :
                print("平局")
                break
            else:
                print("我获胜")
                break

if __name__ == '__main__':
#使用三目运算符以及列表构造几个随机数，作为敌人血量的备选
    enemy_hpp = [i for i in range(900,910)]
#随机获取列表中的一个数字作为敌人的血量
    enemy_hp = random.choice(enemy_hpp)

#创建一个随机整数作为敌人的攻击力
    ememy_power = random.randint(188,201)

#调用函数，并传入参数（敌人血量，敌人攻击力）
    game_numone(enemy_hp,ememy_power)