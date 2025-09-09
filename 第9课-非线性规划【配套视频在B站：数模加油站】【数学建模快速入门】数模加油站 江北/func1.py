# -*- coding: utf-8 -*-
"""
    @author: 数模加油站
    @time  : 2025/8/23 15:18
    @file  : func1.py
"""

def fun1(x):
    # x 是一个 numpy 数组 [x1, x2]
    # 返回值是 -f(x)，用于最小化
    return -x[0]**2 - x[1]**2 + x[0]*x[1] + 2*x[0] + 5*x[1]

