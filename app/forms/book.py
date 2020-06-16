from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    """
    用于搜索参数校验
    """
    # 查询字段： 书名，isbn等
    q = StringField(validators=[Length(min=1, max=30), DataRequired()])
    # 页码
    page = IntegerField(validators=[NumberRange(min=1, max=100)], default=1)
