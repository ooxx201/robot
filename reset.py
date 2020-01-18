from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Unicode, Float, String, DateTime
import config
import secret
from models.base_model import current_time
from models.order_website import OrderWebsite


def reset_database():
    # 现在 mysql root 默认用 socket 来验证而不是密码
    url = 'mysql+pymysql://root:{}@localhost/?charset=utf8mb4'.format(
        secret.database_password
    )
    e = create_engine(url, echo=True)

    with e.connect() as c:
        c.execute('DROP DATABASE IF EXISTS sunny')
        c.execute('CREATE DATABASE sunny CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        c.execute('USE sunny')

    meta = MetaData()

    orderwebsite = Table(
        'orderwebsite', meta,
        Column('id', Unicode(100), primary_key=True, nullable=False),
        Column('date', DateTime, nullable=False),
        Column('amount', Float, nullable=False),
    )

    orderagent = Table(
        'orderagent', meta,
        Column('id', Unicode(100), primary_key=True, nullable=False),
        Column('date', DateTime, nullable=False),
        Column('amount', Float, nullable=False),
        Column('source', String(100), nullable=False),
    )

    meta.create_all(e)


def generate_fake_date():
    form = dict(
        id='sample-order-1',
        date=current_time(),
        amount=1.0011
    )
    OrderWebsite.new(form)


if __name__ == '__main__':
    reset_database()
    # generate_fake_date()
