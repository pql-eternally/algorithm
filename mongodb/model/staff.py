import logging

from bson import ObjectId
from datetime import datetime

from qcore.model.base import BaseModel


class Staff(BaseModel):
    """账户
    """
    logger = logging.getLogger(__name__)

    __collection__ = "staff"

    indexes = [
        # Account-indexes

        # Account-indexes_fields
    ]
    structure = {
        # Account-structure

        # _ID
        '_id': ObjectId,

        # 姓名
        'name': str,

        # 手机号
        'phone': str,

        # 年龄
        'age': int,

        # 状态(100:正常/-100:禁用)
        'state': int,

        # 创建时间
        'created_at': datetime,

        # 更新时间
        'updated_at': datetime,

        # 创建人ID
        'creator_id': ObjectId,

        # 操作人ID
        'operator_id': ObjectId,
        # Account-structure
    }

    embed_fields = {
        # Account-embed_fields

        # Account-embed_fields
    }

    lookup_fields = {
        # 'state_title': ['state', constants.account.STATES],
    }
    has_fields = {
        # Account-has_fields

        # Account-has_fields
    }
    ref_fields = {
        # Account-ref_fields

        # Account-ref_fields
    }
    callback_fields = {

    }

    default_values = {
        # Account-default_values
        '_id': ObjectId,
        'state': 100,
        'created_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
        # Account-default_values
    }
    required_fields = ['_id', 'name']

    validators = {}
