# -*- coding: utf-8 -*-
# @TIME : 2020/12/17 21:07
# @AUTHOR : Xu Bai
# @FILE : __init__
# @DESCRIPTION :
print('you have imported mypackage!')
# from subpackage1 import test11
# #在我们执行import时，当前目录是不会变的（就算是执行子目录的文件），还是需要完整的包名。
from mypackage.subpackage1 import test11
__all__ = ['subpackage1','subpackage2']