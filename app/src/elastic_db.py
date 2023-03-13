from elasticsearch import Elasticsearch

from config import ELASTIC_HOST, ELASTIC_PORT, ELASTIC_INDEX

es = Elasticsearch(f'http://{ELASTIC_HOST}:{ELASTIC_PORT}')