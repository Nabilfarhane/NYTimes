from pymongo import MongoClient
import pandas as pd
from api.models import Article, Keyword, Author
import pprint


client = MongoClient(
    host="127.0.0.1",
    port = 60017,
    username= 'admin',
    password= 'pass'
)


mydb = client["database_nyt"]
archive_collection = mydb["archive_articles"]



query = {'snippet': {'$regex': '.*inflation.*', '$options': 'i'}}
articles_inflation_in_snippet = archive_collection.find(query)
print(len(list(articles_inflation_in_snippet)))



query = {'headline.main': {'$regex': '.*inflation.*', '$options': 'i'}}
articles_inflation_in_headline = archive_collection.find(query)
print(len(list(articles_inflation_in_headline)))

def get_inflation_articles():
    query = {'keywords': {'$elemMatch':{'value': {'$regex': '.*inflation.*', '$options': 'i'}}}}
    articles_inflation_in_keywords = archive_collection.find(query)

    articles = []
    conut = 1
    for article_inflation in articles_inflation_in_keywords:
        keywords = []
        for keyword_obj in article_inflation['keywords']:
            keyword = Keyword(name=keyword_obj['name'],
                                value=keyword_obj['value'],
                                rank=keyword_obj['rank'],
                                major=keyword_obj['major'])
            keywords.append(keyword)    
        authors = []
        for author_obj in article_inflation['byline']['person']:
            author = Author(firstname=author_obj['firstname'],
                            lastname=author_obj['lastname'],
                            organization=author_obj['organization'],
                            rank=author_obj['rank'])
            authors.append(author)
        article = Article(snippet=article_inflation['snippet'],
                        lead_paragraph=article_inflation['lead_paragraph'],
                        source=article_inflation['source'],
                        keywords=keywords,
                        pub_date=article_inflation['pub_date'],
                        document_type=article_inflation['document_type'],
                        news_desk=article_inflation['news_desk'],
                        section_name=article_inflation['section_name'],
                        authors=authors,
                        type_of_material=article_inflation['type_of_material'],
                        word_count=article_inflation['word_count'])
        articles.append(article)
        print('successfully added article' + str(conut))
        conut +=1
    return articles

