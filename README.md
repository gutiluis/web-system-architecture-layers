
## How it works:

# to run:
- python3 -m venv venv
- source venv/bin/activate
- pip install flask

-----

## Features:

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

----------------------------------------------------------------------------------------------------------
Layers and services

# what are layers?
when are layers necessary:
    multiple data sources
    validate or transform data
    reuse logic
    maintainability and testing

layered are isolated levels of responsability. which is safer...
request -> validation -> logic -> database -> response

layers:
    router or controller. request
    service. validate input and coordinate logic
    model. talk to database
    response. data back

advantages of layers:
    readibility and debug
    reusable
    test each layer independently
    scalability


data flow is layered. api -> service -> model -> db
validation and model function calls hapens in the service layer: services.py
database operations are inside a context manager. safe commit/rollback: db.py
custom excpetions. handle errors cleanly at the api level
global error handlers. consistent api responses


app.py is flask main app. the api is here. it has routes, http requests, json responses, errors globally
db.py is database connection and helper functions, commits
models.py is data models, orm like functions, sql query
services.py is business logic and processing. validation
errors.py is custom exceptions. centralize error types


Tips for Structuring Data Flow:
Separate layers
    Validation / Parsing
    Business logic
    Database access
    Response formatting
Centralize error handling
    Flask / FastAPI allow global exception handlers.
Use return types consistently
    For API: always return a JSON object with status and data or error.
Use context managers for all resources
    DB connections, files, network sockets.
Validate early, fail fast
    Check input before processing or writing to DB.


client POST /users -> app.py receives json -> services.py validates names/email, calls db -> models.py sql query -> db.py open db connection, commit -> db insert success and response goes back

input -> validation and error handling -> processing -> storage -> output

input/request
validation and parsing
business logic
    services
database layer
error handling
    try/except
response/output
    json
initialization & context

#

## Technologies Used:

- Python
- Flask

------

## 

Clone repo:
