import time
from utils import session
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


def current_time():
    return int(time.time())


Base = declarative_base()


class SQLMixin(object):

    @classmethod
    def new(cls, form):
        m = cls()
        for name, value in form.items():
            setattr(m, name, value)

        session.add(m)
        session.commit()
        return m

    @classmethod
    def update(cls, id, form):
        m = session.query(cls).filter_by(id=id).first()
        for name, value in form.items():
            setattr(m, name, value)

        session.add(m)
        session.commit()

    @classmethod
    def all(cls, **kwargs):
        ms = session.query(cls).filter_by(**kwargs).all()
        return ms

    @classmethod
    def one(cls, **kwargs):
        m = session.query(cls).filter_by(**kwargs).first()
        return m

    @classmethod
    def delete(cls, id):
        m = session.query(cls).filter_by(id=id).first()
        session.delete(m)
        session.commit()

    @classmethod
    def refresh(cls, form):
        id = form['id']
        m = cls.one(id=id)
        if m:
            if not m.equals(form):
                cls.update(id, form)
        else:
            m = cls.new(form)
        return m

    def equals(self, form):
        for k, v in form.items():
            if hasattr(self, k) and getattr(self, k) == v:
                continue
            return False
        else:
            return True

    @classmethod
    def columns(cls):
        return cls.__mapper__.c.items()

    def __repr__(self):
        name = self.__class__.__name__
        s = ''
        for attr, column in self.columns():
            if hasattr(self, attr):
                v = getattr(self, attr)
                s += '{}: ({})\n'.format(attr, v)
        return '< {}\n{} >\n'.format(name, s)

    def save(self):
        session.add(self)
        session.commit()

    def json(self):
        d = dict()
        for attr, column in self.columns():
            if hasattr(self, attr):
                v = getattr(self, attr)
                d[attr] = v
        return d

    # def json(self):
    #     dict = self.__dict__
    #     dict.pop('_sa_instance_state')
    #     return dict


