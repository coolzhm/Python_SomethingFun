# -*- coding: utf-8 -*-
import random

'''
简单的剪刀、石头、布游戏
'''

print("您已经进入剪刀石头布游戏！")
print("【游戏提示】 1 [剪刀] 2 [石头] 3 [布]")
# 游戏运行结束标识
a = 1
# 存储用户出的拳头
u_text = ""
# 存储电脑出的拳头
c_text = ""


def getString_(value):
    if (value == 1):
        return "剪刀"
    if (value == 2):
        return "石头"
    if (value == 3):
        return "布"


while a == 1:
    computer = random.randint(1, 3)
    try:
        me = int(input("请输入你的操作(退出请输入‘0’)：\n"))
        if (me >= 0 and me <= 3):
            if me == 0:
                print("退出游戏！")
                a = 0
            else:
                if (me == 1 and computer == 3) or (me == 2 and computer == 1) or (me == 3 and computer == 2):
                    print("你【{0}】 电脑【{1}】".format(getString_(me), getString_(computer)))
                    print("恭喜！You Win！！")
                elif me == computer:
                    print("你【{0}】 电脑【{1}】".format(getString_(me), getString_(computer)))
                    print("有点遗憾！打平了")
                else:
                    print("你【{0}】 电脑【{1}】".format(getString_(me), getString_(computer)))
                    print("真菜！You Loss！！")
        else:
            print("请根据游戏提示输入有效数据！！")
    except:
        print("请根据游戏提示输入有效数据！！")
