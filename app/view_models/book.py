class BookBrief:
    """
    模糊查询时的简单书籍模型
    """

    def __init__(self, json_res: dict):
        """
        接收接口传来的原始json数据，整合成简单书籍模型
        :param json_res: 原始json数据
        """
        self.abstract = json_res.get('abstract', "")
        self.title = json_res.get('title', "")
        self.douban_url = json_res.get('url', "")
        self.img_url = json_res.get('cover_url', "")


class BookDetail:
    pass
