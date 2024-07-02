from elasticsearch import Elasticsearch
##setup connection
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=('elastic', 'suVlWmYRKKFk6RYs_TrU'))
print(es.ping())

index_basename="october"
for i in  range(1,11):
    response=es.indices.create(index=index_basename+"_"+str(i))
    print(response)