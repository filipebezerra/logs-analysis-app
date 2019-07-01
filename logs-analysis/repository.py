import psycopg2

DBNAME = "news"


def list_most_popular_articles():
    """Return most popular articles ordered by the most viewed of all time"""
    database = psycopg2.connect(database=DBNAME)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM most_popular_articles")
    articles = cursor.fetchall()
    database.close()
    return articles


def list_most_popular_authors():
    """Return most popular article authors ordered by the sum of views of
    their articles
    """
    database = psycopg2.connect(database=DBNAME)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM most_popular_authors")
    authors = cursor.fetchall()
    database.close()
    return authors


def list_failed_requests_above_one_percent():
    """Return days with more than 1 percent of failed requests"""
    database = psycopg2.connect(database=DBNAME)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM failed_requests_above_one_percent")
    requests = cursor.fetchall()
    database.close()
    return requests
