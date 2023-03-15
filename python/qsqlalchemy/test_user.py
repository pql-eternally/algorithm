from sqlalchemy import select

from .models import User, Address
from .bootstrap import bootstrap_mysql

bootstrap_mysql()

from .globals import MysqlSession


def test_add_user():
    user = User(name="some name", fullname="some fullname")
    with MysqlSession() as session:
        session.add(user)
        session.commit()
        print(user)
        assert user.id is not None


def test_add_address():
    with MysqlSession() as session:
        address = Address(
            email_address="some_email@qq.com",
            user=User(name="pql", fullname="some address fullname")
        )
        session.add(address)
        session.commit()
        assert address.id is not None


def test_select_user():
    """
    scalar: 用于查询单个结果，如果查询结果不止一个，会抛出异常
    scalars: 用于查询多个结果，返回一个生成器，如果调用one()方法不止一个结果，会抛出异常
    """
    stmt = select(User).where(User.name.like("pql")).order_by(User.id.desc())
    with MysqlSession() as session:
        # Any -> Object 等价于find_one
        user = session.scalar(stmt)
        print(user, ' ---> scalar')

        # ScalarResult -> Generator 等价于find
        for user in session.scalars(stmt):
            print(user, ' ---> scalars')


def test_select_with_join():
    stmt = select(Address).join(Address.user). \
        where(User.name.like("pql")). \
        where(Address.email_address.like("some_email@qq.com"))

    with MysqlSession() as session:
        address_records = session.scalars(stmt)
        for address in address_records:
            print(address)


def test_select_multiple_entities():
    stmt = select(User, Address).join(User.addresses).order_by(User.id, Address.id)
    with MysqlSession() as session:
        for row in session.execute(stmt):
            print(row.User, row.Address)


def test_select_individual_attributes():
    stmt = select(User.name, Address.email_address).join(User.addresses).order_by(User.id, Address.id)
    with MysqlSession() as session:
        for row in session.execute(stmt):
            print(row.name, row.email_address)


def test_delete():
    with MysqlSession() as session:
        user = session.get(User, 2)
        session.delete(user)
        session.commit()
