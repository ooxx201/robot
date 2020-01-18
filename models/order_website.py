from sqlalchemy import Column, Integer, Float, Unicode, DateTime
from models.base_model import SQLMixin, Base
import time


class OrderWebsite(SQLMixin, Base):
    __tablename__ = 'orderwebsite'
    id = Column(Unicode(100), primary_key=True, nullable=False)
    date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)

    @classmethod
    def new_from_series(cls, se):
        form = {}
        # unix_time = time.mktime(se[0].timetuple())
        # unix_time = int(unix_time)
        form['id'] = se[1]
        # form['date'] = unix_time
        form['date'] = se[0].to_pydatetime()
        form['amount'] = float(se[2]) / 100
        return cls.refresh(form)
