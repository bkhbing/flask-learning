class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY='123456',

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False