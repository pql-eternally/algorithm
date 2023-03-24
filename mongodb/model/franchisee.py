import logging

from bson import ObjectId
from datetime import datetime

from qcore.model.base import BaseModel


class Franchisee(BaseModel):
    """加盟商
    """
    logger = logging.getLogger(__name__)

    __collection__ = "franchisee"

    indexes = [
        # franchisee-indexes

        # franchisee-indexes_fields
    ]
    structure = {
        # franchisee-structure

        # _id
        '_id': ObjectId,

        # 业务唯一索引
        'index': str,

        # 加盟商名称
        'name': str,

        # 省份编码
        'province_code': str,

        # 省份名称
        'province_name': str,

        # 城市编码
        'city_code': str,

        # 城市名称
        'city_name': str,

        # 加盟商地址
        'address': str,

        # 状态(100:启用,-100:禁用, -101:删除)
        'state': int,

        # 更新时间
        'updated_at': datetime,

        # 创建时间
        'created_at': datetime,

        # 操作人ID
        'operator_id': ObjectId,

        # 创建人ID
        'creator_id': ObjectId,
        # franchisee-structure
    }

    embed_fields = {
        # franchisee-embed_fields

        # franchisee-embed_fields
    }

    lookup_fields = {
        # 'state_title': ['state', constants.franchisee.STATES],
    }
    has_fields = {
        # franchisee-has_fields

        # franchisee-has_fields
    }
    ref_fields = {
        # franchisee-ref_fields

        # franchisee-ref_fields
    }
    callback_fields = {

    }

    default_values = {
        # franchisee-default_values
        '_id': ObjectId,
        'state': 100,
        'updated_at': datetime.utcnow,
        'created_at': datetime.utcnow,
        # franchisee-default_values
    }
    required_fields = ['_id', 'name']

    validators = {}
