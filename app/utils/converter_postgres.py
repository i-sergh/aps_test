

from sqlalchemy import create_engine, Insert
from sqlalchemy.orm import Session

import pandas as pd
from pandas.core.series import Series as PandasSeries

import os 
import sys
import re

sys.path.append(os.path.join(sys.path[0].replace('/utils', '', 1), 'src'))

from database import DATABASE_URL
from search.models import documents_tb

from time import sleep

CSV_PATH = 'posts.csv'
df = pd.read_csv(CSV_PATH)

engine = create_engine(DATABASE_URL.replace('+asyncpg', '', 1))

def rubrics_str2list(string):
    """Переводит рубрики из строки в список"""
    ex = r"VK-?[0-9]*"
    return re.findall(ex, string)

def append_data_from_pd_to_postgres(data: dict, session ):
    
    stmt = Insert(documents_tb).values(data)
    session.execute(stmt)
    session.commit()



with Session(engine) as session:
    for idx, row in df.iterrows():
        data = {'id':idx,
                'rubrics': rubrics_str2list( row['rubrics']), 
                'text': row['text'], 
                'created_date': row['created_date']}
        append_data_from_pd_to_postgres(data, session)
        print(f'append row %s from %s to postgres db'%  (idx, CSV_PATH), end='\r')
        
    print('\ndata appended successfully')
