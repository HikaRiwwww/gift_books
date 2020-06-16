import json

import requests

from .common import CommonUtil

"""
处理api调用相关的工具类
"""


class Api:
    base_url = "https://book.feelyou.top/{}/{}"

    @staticmethod
    def get(q: str):
        """
        调用接口获取书籍信息
        :param q: 查询参数
        :return:
        """
        query = CommonUtil.name_or_isbn(q)
        if query == 'isbn':
            full_api = Api.base_url.format('isbn', q)
        else:
            full_api = Api.base_url.format('search', q)
        r = requests.get(full_api)
        result = json.loads(r.text)
        return result
