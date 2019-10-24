from elasticsearch import Elasticsearch
from datetime import datetime
from pprint import pprint

pprint(globals())
pprint(locals())

elasticsearch = Elasticsearch()

document = {
    'author': 'Gage',
    'text': 'initial elastic',
    'timestamp': datetime.now(),
}
def index_single_document():
    if check_index_exists() is False:
        elasticsearch.index(index="new-index", doc_type='tweet', id=1, body=document)
        return 'indexed!'
    else:
        return 'index already exists!'

def check_index_exists():
    return elasticsearch.exists(index="new-index", id=1)
