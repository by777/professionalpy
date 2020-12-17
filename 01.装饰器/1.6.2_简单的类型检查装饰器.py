# -*- coding: utf-8 -*-
# @TIME : 2020/12/17 20:14
# @AUTHOR : Xu Bai
# @FILE : 1.6.2_简单的类型检查装饰器
# @DESCRIPTION :
import functools
def requires_ints(decorated):
    '''确保接受的所有参数都是整型'''
    @functools.wraps(decorated) # 这样会显示foo的docstring
    def inner(*args, **kwargs):
        kwargs_values = [i for i in kwargs.values()]
        for arg in list(args) + kwargs_values:
            if not isinstance(arg, int):
                raise TypeError('%s only accepts integers as arguments.' % decorated.__name__)
        return decorated(*args, **kwargs)

    return inner


@requires_ints
def foo(x, y):
    ''':return x+y'''
    return x + y


help(foo) #
