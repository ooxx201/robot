import secret
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session():
    #  resources
    url = 'mysql+pymysql://root:{}@localhost/sunny?charset=utf8mb4'.format(
        secret.database_password
    )
    e = create_engine(url, echo=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=e)

    # create a Session
    session = Session()

    return session


session = create_session()
