import requests
import json
from pymongo import MongoClient
import time

client = MongoClient(
    host="127.0.0.1",
    port = 60017,
    username= 'admin',
    password= 'pass'
)
mydb = client["database_nyt"]
archive_collection = mydb["archive_articles"]

api = 'Article_Archive'
api_key = 'insert your key'
years = ['2020','2021','2022']
months = [i+1 for i in range(12)]

for year in years:
    for month in months:
        url_archive = 'https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key={api_key}'
        url = url_archive.format(year=year, month=month, api_key=api_key)
        r = requests.get(url)
        result_json = json.loads(r.text)
        try:
            x = archive_collection.insert_many(result_json['response']['docs'])
            print("Inserted data for month" + str(month) + "of year" + year)
        except:
            print("Not inserted data for month" + str(month) + "of year" + year)
        #print(x.inserted_ids)
        time.sleep(60)
