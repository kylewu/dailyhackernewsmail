#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wenbin Wu <wwu@mozilla.com>'
__date__ = '2012-02-23'
__version__ = '0.1'

from datetime import datetime, date, timedelta

from pyquery import PyQuery as pq

HN_LINK = 'http://www.daemonology.net/hn-daily/'


def fetch():
    """Fetch today's top ten news from Hacker news"""

    TODAY_LINK = HN_LINK + \
                datetime.strftime(
                        date.today() - timedelta(days=1), '%Y-%m-%d'
                        ) +\
                '.html'
    print TODAY_LINK

    d = pq(url=TODAY_LINK)

    '''
        <ul>
            <li>
                <span class="storylink"><a href="http://blog.rapportive.com/rapportive-acquired-by-linkedin">Rapportive (YC S10) Has Been Acquired By LinkedIn</a></span><br>
                <span class="commentlink"><a href="http://news.ycombinator.com/item?id=3621718">(comments)</a></span>
            </li>
        </ul>
    '''

    item_list = []
    for li_item in d('li'):
        spans = pq(li_item)('span')
        link = pq(spans[0])('a').attr('href')
        title = pq(spans[0])('a').text()
        item_list.append((title, link))

    return item_list


if __name__ == '__main__':
    print fetch()
