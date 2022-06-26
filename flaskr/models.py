

import click
from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

# from flaskr import create_app

# print(current_app)

db = SQLAlchemy()

def init_db():
    from . import create_app
    # db = SQLAlchemy(create_app())
    db.create_all(app=create_app())
    
class User(db.Model):
    # 定义表名
    __tablename__ = 'user'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, comment='姓名')
    password = db.Column(db.String(200), unique=True, comment='密码')
    def __repr__(self):
        return 'user:%s'% self.username
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)

class Post(db.Model):
    # 定义表名
    __tablename__ = 'post'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), comment='用户id')
    created = db.Column(db.DateTime, comment='创建时间')
    title = db.Column(db.String(200), default="无定义", comment='标题')
    body = db.Column(db.String(200), default="没有内容", comment='文本')
    def __repr__(self):
        return 'post:%s'% self.title



@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')