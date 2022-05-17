import os

from flask import Flask

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # 默认配置
    app.config.from_mapping(
        SECRET_KEY='dev', # session会用到的密钥
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), # 数据库
    )
    
    if config is None:
        # 加载py文件中的配置
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 传入参数为配置
        app.config.from_mapping(config)
    
    # 创建数据库需要用到的目录
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # 测试
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    return app

 