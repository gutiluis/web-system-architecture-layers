> [!WARNING]
> CURRENTLY UNDER DEVELOPMENT

# Layers and Services

## How it works:

```
python3 -m venv venv
source venv/bin/activate
pip install flask
```

---

### Layers and services

### Building layers
Layers are necessary:
    Multiple data sources
    Validate or transform data
    Reuse logic
    Maintainability and testing

Layered are isolated levels of responsability. which is safer...
Request -> validation -> logic -> database -> response

Layers:
    Router or controller. request
    Service. validate input and coordinate logic
    Model. talk to database
    Response. data back

Advantages of layers:
    Readibility and debug
    Reusable
    Test each layer independently
    Scalability


Data flow is layered. api -> service -> model -> db
Validation and model function calls hapens in the service layer: services.py
Database operations are inside a context manager. safe commit/rollback: db.py
Custom excpetions. handle errors cleanly at the api level
Global error handlers. consistent api responses


app.py is flask main app. the API is here. it has routes, http requests, json responses, errors globally
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

---

## Features

### initialize sqlite3 db in python repl
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

### python sqlite3 api reference
### https://docs.python.org/3/library/sqlite3.html


### run flask server

```
python3 app.py
```

## Tech-Stack

- Python
- Flask
- sqlite3
- Flask

---

## Contributing

If you are interested in reporting/fixing issues and contributing directly to the code base, please see CONTRIBUTING.md for more information on what we're looking for and how to get started.

---

## Community

Info on reporting bugs, getting help, finding third-party tools and sample apps, and more can be found on the Community page.

---

## Licenses

[MIT LICENSE](LICENSE)
