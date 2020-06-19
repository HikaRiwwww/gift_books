from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class Book(db.Model):
    """
    书籍模型
    """
    # 数据表主键id
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 书名
    title = Column(String(50), nullable=False)
    # 作者
    author = Column(String(30), default='佚名')
    # 出版社
    publisher = Column(String(50))
    # 价格
    price = Column(String(20))
    # 页数
    pages = Column(Integer)
    # 出版日期
    pubdate = Column(String(20))
    # isbn
    isbn = Column(String(15), nullable=False, unique=True)
    # 简介
    summary = Column(String(1000))
    # 图片地址
    image = Column(String(50))
