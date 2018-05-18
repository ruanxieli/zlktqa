# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 下午1:46
# @Author  : Xieli Ruan
# @Site    : 
# @File    : decorators.py
# @Software: PyCharm

from functools import wraps
from flask import redirect,url_for,session

# 登陆限制装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
