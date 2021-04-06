# fastAPI

### body params
if Body used to declare body param, the key will be necessary in the JSON request
if not, then there is no key.
if multiple bodies are present, then they will be wrapped, and keys will need to be present

### python async await
method declared with async returns coroutine and requires asyncio.run to run 

3 types of awaitables
coroutine 
task - run concurrently
future - eventual result of async operation, normally not used

asyncio.createTask(asyncfunc) to create coroutine 

generators: use yield - iterables that get values 


## data types

### basic 

int 
float 
str
bool

### advanced

UUID
datetime.datetime
datetime.date
datetime.time
datetime.timedelta
frozenset - same as set
bytes
Decimal - similar to float

### sqlAlchemy

SQL toolkit and ORM

SQL vs NoSQL note: sql db are better when size and performance start to matter
noSql less like tables and rows when abstraction starts to matter

known for its ORM - optional layer

very open source

data mapper pattern - a mapper layer between the objects and the db ensures independence between the layers

2 comonents: Core and ORM 

uses queue system for insert/update/delete operations, flushes them as batch - fowler's "unit of work" pattern


### pymysql

client library for Python MySQL

requires Cpython, pypy, mysql or mariaDB

provides SQL stateents in python code,

connection, connection.cursor()

### pydantic 

provides data validation using python type annotations

provides BaseModel

used by FastAPI 

### alembic 

part of sqlalchemy 

migration tool 

create, manage, invoke change management scripts for relational db 

has CLI 

versions/ folder has migration scripts

op object op.create_table()
op.drop_table()

alembic downgrade goes backwards in time (rollback)

### defs

asgi server - asynchronous server gateway interface
successor to WSGI: web server gateway interface - specifically tied to python 
support Websocket  and long-poll HTTP
single async callable

python class - 
class ClassName: 
    statement1
    statement2
    ...
    statementN

    def __init__(self, *args): # this is like the constructor
    def f(self): # member function 
instantiating: x = MyClass()

python types
item_id: int - can use classes

pydantic - for data validation

检索： look up

Hibernate - java's leading ORM 