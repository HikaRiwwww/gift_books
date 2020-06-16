from secret import db_pwd


class BaseConfig:
    JSON_AS_ASCII = False
    PER_PAGE = 15
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@127.0.0.1:3306/fish?charset=UTF8MB4'.format(db_pwd)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    JSONIFY_PRETTYPRINT_REGULAR = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_POOL_SIZE = 5  # 默认连接池里的连接数量就是5


class ProductionConfig(BaseConfig):
    DEBUG = False
