#!/usr/bin/env python
# coding=utf-8

import repository


def get_most_popular_articles():
    """Get the list os most popular articles"""
    return "1. Three most popular articles\n\n" +\
           "".join("\t* \"{0}\" — {1} views\n".format(article, a_views)
                   for article, a_views
                   in repository.list_most_popular_articles())


def get_most_popular_authors():
    """Get most popular authors"""
    return "2. Most popular authors\n\n" +\
           "".join("\t* {0} — {1} views\n".format(author, a_views)
                   for author, a_views
                   in repository.list_most_popular_authors())


def get_failed_requests_above_one_percent():
    """Get days with more than 1 percent of failed requests"""
    return "3. Days with more than 1% of requests failures\n\n" +\
           "".join("\t* {0} — {1:.2%} errors\n"
                   .format(date.strftime('%B %d, %Y'), fail_percent)
                   for date, fail_percent
                   in repository.list_failed_requests_above_one_percent())


def main():
    f = open("report.txt", "w+")
    articles = get_most_popular_articles()
    print articles
    f.write(articles + "\n")
    authors = get_most_popular_authors()
    print authors
    f.write(authors + "\n")
    failed_requests = get_failed_requests_above_one_percent()
    print failed_requests
    f.write(failed_requests + "\n")
    f.close()


if __name__ == '__main__':
    main()
