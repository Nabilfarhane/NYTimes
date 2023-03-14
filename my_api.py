from fastapi import FastAPI
from search_service import get_number_articles_in_db, get_number_articles_with_keyword, get_news_desks

api = FastAPI(title="Exam_Fast_Api",
              version='v1')

@api.get('/status')
def get_status():
    """Returns 1 if the API is running
    """
    return 1

@api.get('/total_articles')
def get_total_articles():
    """Returns number of articles in the database
    """
    num_articles = get_number_articles_in_db()
    return num_articles

@api.get('/num_articles/{keyword}')
def get_num_articles(keyword:str):
    """get number of articles with the keyword keyword
    """
    num_articles = get_number_articles_with_keyword(keyword)
    return num_articles

'''
@api.get('/desks')
def get_desks(keyword:str):
    """get number of articles with the keyword keyword
    """
    news_desks = get_news_desks()
    return news_desks
'''
@api.get('/num_articles/{keyword}')
def get_num_articles(keyword:str):
    """get number of articles with the keyword keyword
    """
    num_articles = get_number_articles_with_keyword(keyword)
    return num_articles
