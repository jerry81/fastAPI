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

### APIRouter

from fastapi import APIRouter

router = APIRouter()

usage: 

@router.get("/users", tags=["users"])
async def read_users():
    return [{"username":"Rick" }, {"username":"Morty"}]

organize file structure as 
app 
    __init__.py # allows for importing code from one file to another
    main.py
    dependencies.py
    routers
        __init__.py # allows for importing code from one file to another
        items.py
        users.py
    internal
        __init__.py # allows for importing code from one file to another
        admin.py

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

### other packages

databases - async db support for python - uses sqlAlchemy expression language 

loguru - logging for python 

inflect - natural language processing (pluralizing words)

cryptography - self explanatory, required by sha256_password

pytest-asyncio - utils for testing async code

httpx - provides async request client for testing endpoints

asgi-lifespan - allow testing async apps without asgi server

### python typing Generic

example of generic classes - collection classes like Array 

Syntax - use square brackets to wrap the type 
declare: Generic[T]
use Stack[Int]

### uvicorn 

fast ASGI server inplementation 

### testing 

can use pytest directly with FastAPI

client = TestClient(app)

then
response = client.get('/') # calls the endpoint /

assert on response
assert response.json() == ...

then run the test with 

pytest 

from blog entry, <a href="https://www.jeffastor.com/blog/testing-fastapi-endpoints-with-docker-and-pytest">Testing Fastapi endpoints with docker and pytest (1/13/21)</a>
use a combo of pytest, pytest-asyncio, httpx, asgi-lifespan

0.  in db config, fork the DB URL to test if environment is testing
1.  apply migrations at beginning and end of testing session using pytest.fixture
    a.  set environment to "TESTING"
    b.  alembic.command.upgrade
    c.  yield
    d.  alembic.command.downgrade
    e.  set scope to "session" so that the db persists between tests, otherwise fresh db for each test
2.  create application for testing
3.  provide db where required
4.  create client fixtture

### pytest

provides assert

will run all files test_*.py or *_test.py
standard test discovery rules

### pip install from requirements file

python -m pip install -r -requirements file-

### troubleshooting

when running pytest, ImportError while importing test module
cause: no __init__.py file present in directory with test
solution: add an empty __init__.py file to the directories with tests

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

python relative import
from ..dependencies import get_token_header

python self - refers to current instance of this class 
used to access variables in class

jsonable_encoder - provided by fastAPI to convert data type to JSON dict/list