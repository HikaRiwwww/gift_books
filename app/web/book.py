from flask import jsonify, request

from utils.api import Api
from .blueprint import web
from ..forms.book import SearchForm


@web.route('/book/search')
def search_book():
    """
    调用外部api查询书籍信息
    支持通过书名和isbn查询, 页码用于分页管理
    :return:json格式的书籍详细信息列表
    """
    # 根据查询参数拼接不同的api
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        result = Api.get(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
