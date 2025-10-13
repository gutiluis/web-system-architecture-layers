# to run:
- python3 -m venv venv
- source venv/bin/activate
- pip install flask



# initialize sqlite3 db in python repl
- import sqlite3
- on_disk_connection = sqlite3.connect("users.db")
- execute_sql_statements_and_fetch_results_from_sql_queries_with_cursor = on_disk_connection.cursor()

- execute_sql_statements_and_fech_results_from_sql_queries_with_cursor.execute("""
- CREATE TABLE IF NOT EXISTS users (
-    id INTEGER PRIMARY KEY AUTOINCREMENT,
-    name TEXT NOT NULL,
-    email TEXT NOT NULL UNIQUE
- )
- """)
- conn.commit()
- conn.close()

# python sqlite3 api reference
# https://docs.python.org/3/library/sqlite3.html


# run flask server
- python3 app.py
