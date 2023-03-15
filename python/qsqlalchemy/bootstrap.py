import logging

from qcore.core.mysql import init_mysql_from_config
from qcore.core.globals import global_context

logger = logging.getLogger(__name__)


def init_mysql():
    mysql_config = {
        'live': {
            'url': "mysql+pymysql://root:root@127.0.0.1:3306/live_db",
            'database': 'live_db',
            'options': {},
        }
    }
    mysql_service = init_mysql_from_config(mysql_config)
    return mysql_service


def bootstrap_mysql():
    mongo_service = init_mysql()
    engine = mongo_service.live_engine
    global_context.mysql_engine = engine
    global_context.MysqlSession = engine.Session
    global_context.push()
