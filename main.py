from config import *
import pandas as pd
from models.order_website import OrderWebsite
from models.order_agent import OrderAgent
from pathlib import Path
from utils import session


def dump_website_data(home_dir):
    for file in Path(home_dir).rglob('*.xlsx'):
        df = pd.read_excel(file)
        df.apply(OrderWebsite.new_from_series, axis=1)


def dump_agent_data(home_dir):
    for path in Path(home_dir).glob('*'):
        if path.is_dir():
            agent_name = path.parts[-1]
            filenames = Path(path).rglob('*.xlsx')
            for filename in filenames:
                df = pd.read_excel(filename)
                f = lambda x: OrderAgent.new_from_series(x, agent_name)
                df.apply(f, axis=1)


def export_table():
    data = session.query(OrderWebsite.id, OrderWebsite.date, OrderWebsite.amount, OrderAgent.date,
                         OrderAgent.amount, OrderAgent.source).filter(OrderWebsite.id == OrderAgent.id).all()
    df = pd.DataFrame.from_records(data)
    df = df.rename(columns={
        0: 'id',
        1: 'Website.date',
        2: 'Website.amount',
        3: 'Agent.date',
        4: 'Agent.amount',
        5: 'Agent.source',
    })
    df.to_excel(export_dir)
    print(df)


if __name__ == '__main__':
    dump_website_data(website_dir)
    dump_agent_data(agent_dir)
    export_table()
