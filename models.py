# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 下午3:29
# @Author  : Xieli Ruan
# @Site    : db模型
# @File    : models.py
# @Software: PyCharm

from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # now()获取等是服务器第一次运行等时间
    # now是每次创建一个模型等时候，都呼求当前等时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    author=db.relationship('User',backref=db.backref('questions'))

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    question_id=db.Column(db.Integer,db.ForeignKey('question.id'))
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    question=db.relationship('Question',backref=db.backref('answers',order_by=id.desc()))
    author=db.relationship('User',backref=db.backref('answers'))

