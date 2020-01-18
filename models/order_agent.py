from sqlalchemy import Column, Integer, Float, Unicode, String, DateTime
from models.base_model import SQLMixin, Base
import time


class OrderAgent(SQLMixin, Base):
    __tablename__ = 'orderagent'
    id = Column(Unicode(100), primary_key=True, nullable=False)
    date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    source = Column(String, nullable=False)

    @classmethod
    def new_from_series(cls, se, source):
        form = {}
        # unix_time = time.mktime(se[0].timetuple())
        # unix_time = int(unix_time)
        form['id'] = se[1]
        # form['date'] = unix_time
        form['date'] = se[0].to_pydatetime()
        form['amount'] = float(se[2])
        form['source'] = source
        return cls.refresh(form)


