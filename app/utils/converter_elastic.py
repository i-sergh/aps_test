from elasticsearch import Elasticsearch
import pandas as pd


es = Elasticsearch('http://elastic:9200')

CSV_PATH = 'posts.csv'

df = pd.read_csv(CSV_PATH)

for idx, row in df.iterrows():
    resp = es.index(index="doc-index", id=idx, document={'text': row['text']})
    print(f'append row %s from %s to elasticsearch to doc-index'%  (idx, CSV_PATH), end='\r')
es.indices.refresh(index="doc-index")
print('\ndata appended successfully\n doc-index refreshed')