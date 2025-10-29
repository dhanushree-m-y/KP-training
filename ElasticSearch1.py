from elasticsearch import Elasticsearch

# Connect to Elasticsearch cluster running on localhost
es = Elasticsearch("http://localhost:9200")

# Create an index
es.indices.create(index="employees", ignore=400)

# Index a document
doc = {
    "name": "John Doe",
    "age": 30,
    "position": "Developer"
}
es.index(index="employees", id=1, document=doc)

# Get a document by ID
res = es.get(index="employees", id=1)
print(res["_source"])

# Search documents
search_res = es.search(index="employees", body={"query": {"match_all": {}}})
print(f"Got {search_res['hits']['total']['value']} hits")
for hit in search_res['hits']['hits']:
    print(hit["_source"])
