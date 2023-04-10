import logging

from bson import ObjectId
from datetime import datetime

from qcore.model.base import BaseModel


class Book(BaseModel):
    logger = logging.getLogger(__name__)

    __collection__ = "book"

    indexes = [
        # Book-indexes

        # Book-indexes_fields
    ]
    structure = {
        # Book-structure

        # _ID
        '_id': ObjectId,

        # 链接
        'href': str,

        # 标题
        'title': str,

        # 原始页面内容
        'raw_content': str,

        # 要爬取的文章列表
        'articles': list,

        # 状态(100:正常/-100:禁用)
        'state': int,

        # 创建时间
        'created_at': datetime,

        # 更新时间
        'updated_at': datetime,

        # Book-structure
    }

    embed_fields = {
        # Book-embed_fields

        # Book-embed_fields
    }

    lookup_fields = {
        # 'state_title': ['state', constants.Article.STATES],
    }
    has_fields = {
        # Book-has_fields

        # Book-has_fields
    }
    ref_fields = {
        # Book-ref_fields
        # Book-ref_fields
    }
    callback_fields = {

    }

    default_values = {
        # Book-default_values
        '_id': ObjectId,
        'created_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
        # Book-default_values
    }
    required_fields = ['_id', 'href', 'title']

    validators = {}


class Article(BaseModel):
    """文章
    """
    logger = logging.getLogger(__name__)

    __collection__ = "article"

    indexes = [
        # Article-indexes

        # Article-indexes_fields
    ]
    structure = {
        # Article-structure

        # _ID
        '_id': ObjectId,

        # 书籍ID
        'book_id': ObjectId,

        # 链接
        'href': str,

        # 标题
        'title': str,

        # 章节
        'chapter': int,

        # 文章内容
        'raw_content': str,

        # 文章处理后的内容
        'content': dict,

        # 状态(1:待处理, 10:处理中，100:处理完成)
        'state': int,

        # 创建时间
        'created_at': datetime,

        # 更新时间
        'updated_at': datetime,

        # Article-structure
    }

    embed_fields = {
        # Article-embed_fields

        # Article-embed_fields
    }

    lookup_fields = {
        # 'state_title': ['state', constants.Article.STATES],
    }
    has_fields = {
        # Article-has_fields

        # Article-has_fields
    }
    ref_fields = {
        # Article-ref_fields
        # Article-ref_fields
    }
    callback_fields = {

    }

    default_values = {
        # Article-default_values
        '_id': ObjectId,
        'state': 1,
        'created_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
        # Article-default_values
    }
    required_fields = ['_id', 'href', 'title']

    validators = {}
