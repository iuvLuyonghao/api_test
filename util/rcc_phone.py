#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def creat_phone():
    #第二位数
    second = [3,4,5,7,8][random.randint(0,4)]
    #第三位数
    third = {
        3:random.randint(0,9),
        4:[5,7][random.randint(0,1)],
        5:[i for i in range(0,10) if i != 4][random.randint(0,8)],
        7:[6, 7, 8][random.randint(0,2)],
        8:random.randint(0,9)
    }[second]
    #后八位数
    suffix = ''
    for j in range(0, 8):
        suffix = suffix + str(random.randint(0,9))

    return "1{}{}{}".format(second, third, suffix)

if __name__=='__main__':
    print(creat_phone())