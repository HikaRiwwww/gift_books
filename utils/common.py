"""
处理一些通用逻辑的工具类
"""


class CommonUtil:
    @staticmethod
    def name_or_isbn(q: str):
        """
        判断入参是isbn还是书名
        如果不是isbn就是书名
        :param q: 查询参数
        :return: 'isbn' or 'name'
        """
        q = q.replace('-', '')
        if q.isdigit() and (len(q) == 13 or len(q) == 10):
            return 'isbn'
        else:
            return 'name'
