import logging

from bson import ObjectId
from datetime import datetime

from qcore.model.base import BaseModel


class App(BaseModel):
    """应用服务
    """
    logger = logging.getLogger(__name__)

    __collection__ = "app"

    indexes = [
        # App-indexes
        # App-indexes_fields
    ]
    structure = {
        # App-structure

        # id
        '_id': ObjectId,

        # 名称
        'name': str,

        # 描述
        'description': str,

        # 状态
        'state': int,

        # app 代码
        'app_code': str,

        # 创建时间
        'created_at': datetime,

        # 更新时间
        'updated_at': datetime,
        # App-structure
    }

    embed_fields = {
        # App-embed_fields

        # App-embed_fields
    }

    lookup_fields = {
        # 'state_title': ['state', constants.core.STATES],
    }
    has_fields = {
        # App-has_fields

        # App-has_fields
    }
    ref_fields = {
        # App-ref_fields

        # App-ref_fields
    }
    callback_fields = {

    }

    default_values = {
        # App-default_values
        '_id': ObjectId,
        'state': 100,
        'created_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
        # App-default_values
    }
    required_fields = ['_id', 'state', 'app_code', 'created_at', 'updated_at']

    validators = {}


class AppKey(BaseModel):
    """应用密钥
    """
    logger = logging.getLogger(__name__)

    __collection__ = "app_key"

    indexes = [
        # AppKey-indexes
        # AppKey-indexes_fields
    ]
    structure = {
        # AppKey-structure

        # id
        '_id': ObjectId,

        # app _id
        'app_id': ObjectId,

        # 开发者key
        'access_key': str,

        # 秘钥
        'secret_key': str,

        # 创建时间
        'created_at': datetime,

        # 更新时间
        'updated_at': datetime,

        # 状态
        'state': int,
        # AppKey-structure
    }

    embed_fields = {
        # AppKey-embed_fields

        # AppKey-embed_fields
    }

    lookup_fields = {
        # 'state_title': ['state', constants.core.STATES],
    }
    has_fields = {
        # AppKey-has_fields

        # AppKey-has_fields
    }
    ref_fields = {
        # AppKey-ref_fields

        # AppKey-ref_fields
    }
    callback_fields = {

    }

    default_values = {
        # AppKey-default_values
        '_id': ObjectId,
        'created_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
        'state': 100,
        # AppKey-default_values
    }
    required_fields = ['_id', 'app_id', 'created_at', 'state']

    validators = {}
