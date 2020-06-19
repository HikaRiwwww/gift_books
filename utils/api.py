import json

import requests

from app.view_models.book import BookBrief
from .common import CommonUtil

"""
处理api调用相关的工具类
"""


class Api:
    base_url = "https://book.feelyou.top/{}/{}"

    @classmethod
    def get(cls, q: str):
        """
        调用接口获取书籍信息
        :param q: 查询参数
        :return:
        """
        query = CommonUtil.name_or_isbn(q)
        full_api = Api.base_url.format('isbn', q) if query == 'isbn' else Api.base_url.format('search', q)
        r = requests.get(full_api)
        results = json.loads(r.text)
        return cls.pack_brief_by_isbn(results)

    @classmethod
    def pack_brief_by_isbn(cls, results):
        brief_list = []
        if type(results) == dict:
            results = [results]
        for res in results:
            brief_list.append(BookBrief(res).__dict__)
        return {'total': len(brief_list), 'results': brief_list}
