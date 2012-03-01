#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wenbin Wu <wwu@mozilla.com>'
__date__ = '2012-02-24'

import sqlite3


CREATE_EXE = 'create table if not exists data (title text, ori_link text unique, link text, date timestamp)'

INSERT_EXE = 'insert into data values (?, ?, ?, ?)'


class DB():
    def __init__(self):
        self.db_name = 'db.sqlite'
        self.conn = sqlite3.connect(self.db_name)
        self.create_db()

    def create_db(self):
        self.conn.execute(CREATE_EXE)

    def insert_db(self, t):
        try:
            self.conn.execute(INSERT_EXE, t)
            self.conn.commit()
        except:
            pass

    def close(self):
        self.conn.close()

DB()
