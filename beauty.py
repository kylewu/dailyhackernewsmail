#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wenbin Wu <wwu@mozilla.com>'
__date__ = '2012-02-24'

from ext import setup_rdd


def add_to_readability(rdd, url):

    bookmark = rdd.add_bookmark(url=url)
    return bookmark


def get_article(rdd, id):
    article = rdd.get_article(id)
    print article.title
    print '-' * len(article.title) + '\n'
    print article.content
    return article


def list_article(rdd):
    bookmarks = rdd.get_me().bookmarks(order='-date_added')

    for mark in bookmarks:
        print mark.article.title + str(mark.article.id)


def make_link(id):
    return 'https://www.readability.com/articles/' + id

if __name__ == '__main__':
    rdd = setup_rdd()
    #article = add_to_readability(rdd, 'http://baidu.com')
    get_article(rdd, 'jpeq3n1d')  # article.id)
    #list_article(rdd)

