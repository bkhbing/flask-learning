import os

from flask import Flask
from flaskr import models
from flaskr.config import DevelopmentConfig
from flask_login import LoginManager

login_manager = LoginManager()

def init_app(app):
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    models.db.init_app(app)
    app.cli.add_command(models.init_db_command)

def init_blueprint(app):
    from flaskr import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # # 默认配置
    # app.config.from_mapping(
    #     # 密码
    #     SECRET_KEY='123456',
    #     # 数据库链接地址
    #     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask',
    #     # 动态追踪修改设置，如未设置只会提示警告
    #     SQLALCHEMY_TRACK_MODIFICATIONS = True,
    # )
    if config is None:
        # 加载py文件中的配置
        app.config.from_object(DevelopmentConfig)
    else:
        # 传入参数为配置
        app.config.from_mapping(config)
    
    # 创建数据库需要用到的目录
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    init_app(app)
    init_blueprint(app)
    # 测试
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    return app
