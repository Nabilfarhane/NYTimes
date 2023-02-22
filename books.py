import requests
import json
from elasticsearch import Elasticsearch

# configure elasticsearch
config = {
    'host': 'vmi334550.contaboserver.net'
}
#es = Elasticsearch([config,], timeout=300)

apiKey='0bZbi4PqGb6xJa7IfA0tV6JuX0JlRqbT'
bookUrl = 'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key=' + apiKey

titleList = ['inflation']

for title in titleList:
    url = bookUrl + '&title=' + title
    r = requests.get(url)
    result_json = json.loads(r.text)
    #es.indices.create(index = 'books_' + title + '_index', body = result_json)
    print(result_json)