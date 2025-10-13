#!/bin/env python


import sqlite3
from contextlib import contextmanager

DB_FILE = "users.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    try:
        yield conn        # give the connection to the caller
        conn.commit()     # commit if no error
    except sqlite3.Error:
        conn.rollback()   # rollback if something went wrong
        raise
    finally:
        conn.close()      # always close
