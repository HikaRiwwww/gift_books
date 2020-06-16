from flask import Flask

from app.config import DevelopmentConfig
from app.models.book import db
from app.web.blueprint import web


def create_app():
    """
    初始化核心应用
    :return:
    """
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(DevelopmentConfig)
    # 数据库初始化
    db.init_app(app)
    db.create_all(app=app)
    # 注册蓝图
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(web)
