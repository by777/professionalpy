# -*- coding: utf-8 -*-
# @TIME : 2020/12/9 21:05
# @AUTHOR : Xu Bai
# @FILE : 1.1_理解装饰器
# @DESCRIPTION :
def decorated_by(func):
    func.__doc__ += '\n---------------Decorated by decorated_by 1.---------------'
    return func


def decorated_by2(func):
    func.__doc__ += '\n---------------Decorated by decorated_by 2.---------------'
    return func

def add(x, y):
    '''Return the sum of x and y.
    (docString是第一行指定的字符串，例如执行help()就能看到此字符串）'''
    return x + y


help(add)

add = decorated_by(add)
help(add)

@decorated_by2
@decorated_by
def div(x, y):
    '''解释器的执行是自底向上的'''
    return x / y


help(div)
