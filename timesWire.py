import requests
import json
from elasticsearch import Elasticsearch

# configure elasticsearch
config = {
    'host': 'vmi334550.contaboserver.net'
}
#es = Elasticsearch([config,], timeout=300)

apiKey='0bZbi4PqGb6xJa7IfA0tV6JuX0JlRqbT'

timesWireUrl = 'https://api.nytimes.com/svc/news/v3/content/all/{section}.json?api-key=' + apiKey

def getSections():
    sections = []
    sectionUrl = 'https://api.nytimes.com/svc/news/v3/content/section-list.json?api-key=' + apiKey
    r = requests.get(sectionUrl)
    r_json = json.loads(r.text)
    sectionList = json.dumps(r_json['results'])
    sectionList = json.loads(sectionList)
    #print(sectionList)
    for s in sectionList:
        #print(s['section'])
        sections.append(s['section'])
    return sections
    

sections = getSections()
for section in sections:
    url = timesWireUrl.replace("{section}" , section)
    r = requests.get(url)
    result_json = json.loads(r.text)
    #es.indices.create(index = 'timeswire_' + q + '_index', body = result_json)
    print(result_json)