# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 下午3:30
# @Author  : Xieli Ruan
# @Site    : 命令
# @File    : manage.py
# @Software: PyCharm
# Manager: 写终端类似脚本的
# Migrate: 模型到表面迁移
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from zlktqa import app
from exts import db
from models import User,Question,Answer

manager=Manager(app)

# 使用Migrate绑定app和db
migrate=Migrate(app,db)

#添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()