import logging

from bson import ObjectId
from datetime import datetime

from qcore.model.base import BaseModel


class RequestToken(BaseModel):
    """授权Request Token
    """
    logger = logging.getLogger(__name__)

    __collection__ = "request_token"

    indexes = [
        # RequestToken-indexes
        # RequestToken-indexes_fields
    ]
    structure = {
        # RequestToken-structure

        # _id
        '_id': str,

        # 绑定的Account ID
        'account_id': ObjectId,

        # app id
        'app_id': ObjectId,

        # 存活时间(秒)
        'ttl': int,

        # 是否失效
        'state': int,

        # 创建时间
        'created_at': datetime,

        # 过期时间
        'expired_at': datetime,

        # 更新时间时间
        'updated_at': datetime,
        # RequestToken-structure
    }

    embed_fields = {
        # RequestToken-embed_fields

        # RequestToken-embed_fields
    }

    lookup_fields = {
        # 'state_title': ['state', constants.auth.STATES],
    }
    has_fields = {
        # RequestToken-has_fields

        # RequestToken-has_fields
    }
    ref_fields = {
        # RequestToken-ref_fields

        # RequestToken-ref_fields
    }
    callback_fields = {

    }

    default_values = {
        # RequestToken-default_values
        'created_at': datetime.utcnow,
        'expired_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
        # RequestToken-default_values
    }
    required_fields = ['_id', 'account_id', 'app_id', 'ttl', 'state', 'created_at', 'expired_at', 'updated_at']

    validators = {}

    @property
    def is_ok(self):
        """
        验证request token是否可用
        :return:
        """
        now = datetime.utcnow()
        return now < self['expired_at'] and self['state'] == 100


class AccessToken(BaseModel):
    """授权存取Token
    """
    logger = logging.getLogger(__name__)

    __collection__ = "access_token"

    indexes = [
        # AccessToken-indexes
        # AccessToken-indexes_fields
    ]
    structure = {
        # AccessToken-structure

        # _id
        '_id': str,

        # app id
        'app_id': ObjectId,

        # 对于AccountAccessToken绑定的Account ID
        'account_id': ObjectId,

        # 用于兑换AcesssToken的RequestToken
        'request_token': str,

        # 用于刷新和兑换新的AcesssToken
        'refresh_token': str,

        # 是否失效
        'state': int,

        # 创建时间
        'created_at': datetime,

        # 过期时间
        'expired_at': datetime,

        # 更新时间
        'updated_at': datetime,
        # AccessToken-structure
    }

    embed_fields = {
        # AccessToken-embed_fields

        # AccessToken-embed_fields
    }

    lookup_fields = {
        # 'state_title': ['state', constants.auth.STATES],
    }
    has_fields = {
        # AccessToken-has_fields

        # AccessToken-has_fields
    }
    ref_fields = {
        # AccessToken-ref_fields

        # AccessToken-ref_fields
    }
    callback_fields = {

    }

    default_values = {
        # AccessToken-default_values
        'created_at': datetime.utcnow,
        'expired_at': datetime.utcnow,
        'updated_at': datetime.utcnow,
        # AccessToken-default_values
    }
    required_fields = ['_id', 'app_id', 'account_id', 'state', 'created_at', 'expired_at', 'updated_at']

    validators = {}

    @property
    def is_ok(self):
        """

        Returns
        -------

        """
        now = datetime.utcnow()
        return now < self['expired_at'] and self['state'] == 100
