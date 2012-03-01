#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wenbin Wu <wwu@mozilla.com>'
__date__ = '2012-02-24'

from datetime import date, timedelta, datetime

from ext import setup_rdd
from beauty import add_to_readability, make_link
from fetch import fetch
from db import DB
from mail import send_mail


def worker():
    item_list = fetch()
    conn = DB()
    rdd = setup_rdd()

    readability_list = []
    for item in item_list:
        mark = add_to_readability(rdd, item[1])
        print item[0], item[1], make_link(mark.article.id)
        conn.insert_db(
                (item[0], item[1], make_link(mark.article.id),
                        date.today() - timedelta(days=1))
                )

        article = rdd.get_article(mark.article.id)

        readability_list.append(
                {'title': item[0],
                'link': make_link(mark.article.id),
                'content': article.content
                })

    send_mail(readability_list)
