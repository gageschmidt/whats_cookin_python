from elasticsearch import Elasticsearch
from datetime import datetime

elasticsearch = Elasticsearch()

document = {
    'author': 'Gage',
    'text': 'initial elastic',
    'timestamp': datetime.now(),
}
def index_single_document():
    response = elasticsearch.index(index="new-index", doc_type='tweet', id=1, body=document)
    if response:
        return 'indexed!'