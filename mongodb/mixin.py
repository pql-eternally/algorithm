import logging

logger = logging.getLogger(__name__)


def transactional(conn):
    """
    A decorator that wraps a function in a transaction.
    """

    def wrapper(func):
        def inner(*args, **kwargs):
            with conn.start_session() as session:
                try:
                    # Start a transaction
                    logger.info('Start transaction session ...')
                    session.start_transaction()
                    kwargs['session'] = session
                    func(*args, **kwargs)
                except Exception as e:
                    # If any operation fails, abort the transaction
                    session.abort_transaction()
                    logger.info(f'Handle transaction session error: {e}, rollback done ...')
                    raise e
                else:
                    # If all operations succeed, commit the transaction
                    session.commit_transaction()
                    logger.info('Commit transaction session done ...')

        return inner

    return wrapper


class TransactionSessionSupport(object):

    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        session = self.conn.start_session()
        return session

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
