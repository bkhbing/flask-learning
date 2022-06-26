class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY='123456',

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.56.102:3306/flaskr'
    SQLALCHEMY_TRACK_MODIFICATIONS = False