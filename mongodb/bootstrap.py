import logging

from qcore.core.mongo import init_mongokit_from_config, load_mongokit_models
from qcore.core.globals import global_context

from mongodb import mongo_uri

logger = logging.getLogger(__name__)


def init_mongo():
    mongo_config = {
        'live': {
            'uri': mongo_uri,
            'database': 'test',
            'options': {},
        }
    }
    mongo_service = init_mongokit_from_config(mongo_config)

    auto_load_models = [
        'mongodb.model',
    ]
    for module_path in auto_load_models:
        load_mongokit_models(module_path)
    logger.info(f'model {auto_load_models} auto loaded')
    return mongo_service


def bootstrap_mongo():
    mongo_service = init_mongo()
    db = mongo_service.live_db
    global_context.conn = mongo_service.connection_pool.get(mongo_service.live_pool_id)
    global_context.db = db
    global_context.push()
