from pymongo import MongoClient
import pandas as pd
from models import Article, Keyword, Author
import pprint


client = MongoClient(
    host="127.0.0.1",
    port = 60017,
    username= 'admin',
    password= 'pass'
)

mydb = client["database_nyt"]
archive_collection = mydb["archive_articles"]

def get_number_articles_in_db():
    number_of_articles = archive_collection.count_documents({})
    return number_of_articles

def get_number_articles_with_keyword(keyword):
    query = {'keywords': {'$elemMatch':{'value': {'$regex': keyword, '$options': 'i'}}}}
    articles_with_keywords = archive_collection.find(query)
    return len(list(articles_with_keywords))



def get_articles_by_keyword(keyword:str):
    query = {'keywords': {'$elemMatch':{'value': {'$regex': keyword, '$options': 'i'}}}}
    articles_with_keyword = archive_collection.find(query)

    articles = []
    for article_with_keyword in articles_with_keyword:
        keywords = []
        for keyword_obj in article_with_keyword['keywords']:
            keyword = Keyword(name=keyword_obj['name'],
                                value=keyword_obj['value'],
                                rank=keyword_obj['rank'],
                                major=keyword_obj['major'])
            keywords.append(keyword)    
        authors = []
        for author_obj in article_with_keyword['byline']['person']:
            author = Author(firstname=author_obj['firstname'],
                            lastname=author_obj['lastname'],
                            organization=author_obj['organization'],
                            rank=author_obj['rank'])
            authors.append(author)
        article = Article(snippet=article_with_keyword['snippet'],
                        lead_paragraph=article_with_keyword['lead_paragraph'],
                        source=article_with_keyword['source'],
                        keywords=keywords,
                        pub_date=article_with_keyword['pub_date'],
                        document_type=article_with_keyword['document_type'],
                        news_desk=article_with_keyword['news_desk'],
                        section_name=article_with_keyword['section_name'],
                        authors=authors,
                        type_of_material=article_with_keyword['type_of_material'],
                        word_count=article_with_keyword['word_count'])
        articles.append(article)
    return articles


def get_news_desks():
    articles = get_inflation_articles()
    desks = []
    for article in articles:
        if not(article.news_desk in desks):
         desks.append(article.news_desk)
    return desks

def get_keywords_associations(keyword):
    articles = get_articles_by_keyword(keyword)
    keywords = []
    for article in articles:
         keywords.append(article.keywords)
    return keywords