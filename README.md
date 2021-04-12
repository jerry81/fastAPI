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

with args - 
router = APIRouter(
    prefix="/admin",
    dependencies=[Depends(cat.get_current_user)],
    responses={404: {"description": "Not found"}}
    route_class=customized_route
)

dependencies adds the dependency to every endpoint defined in this router

route_class allows customized routes

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

router.include_router(another_router) # for composing routers
app.include_router(api_router)

at top of controller router=APIRouter()

@router.get("/") ...

### app lifecycle events

app.add_event_handler("startup/shutdown", handler(app))

### custom middleware 

define a function
def logger(app: FastAPI):
    @app.middleware("http")
    async def logger_request(request: Request, call_next) -> Response: # -> Response is return value
        logger.info(...)
        response = await call_next(request)
        return response

### bcrypt

for hashing and checking passwords

salt - a random value added to input of hash to gen unique hashes 

bcrypt.hashpw(pw, salt)

bcrypt.checkpw(password, hashed) -> bool

### PyJWT

pip install pyjwt
import jwt
encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
jwt.decode(encoded_jwt, "secret", algorithms["HS256"])
exp included in the body with a timestamp is the expiration time claim 

### app setup

app.add_middleware(middleware_object) # for example, starlette.middleware.cors.CORSMiddleware
app.include_router(api_router, prefix=API_PREFIX) # from app.routers.api import router as api_router


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

usage:
from alembic import op
import sqlalchemy as sa

alembic has an .ini file with configurations
env.py file - run when alembic migration tool is invoked 

install using alembic~=1.5.8

scripts:
alembic
alembic upgrade head
alembic downgrade
alembic history

w.r.t. running app
alembic upgrade head
then 
uvicorn --host...

methods
op.create_index(idx_name, table, col)
op.create_table(table_name, sqlalchemy_column1, sqlalchemy_column2, etc...)

### other packages

databases - async db support for python - uses sqlAlchemy expression language 

loguru - logging for python 

inflect - natural language processing (pluralizing words)

cryptography - self explanatory, required by sha256_password

pytest-asyncio - utils for testing async code

httpx - provides async request client for testing endpoints

asgi-lifespan - allow testing async apps without asgi server

starlette - complete asgi fx OR support toolkit - config module is used in project

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

### naming conventions

single underscore - private 

double underscore aka name mangling - distinguish from global scope - class vars

### troubleshooting

when running pytest, ImportError while importing test module
cause: no __init__.py file present in directory with test
solution: add an empty __init__.py file to the directories with tests

could not import added modules
cause: using old image
solution: run docker-compose up -d --build

ImportError: attempted relative import with no known parent package
cause: 
solution: changed to frome -filename- import fn

VARCHAR requires a length on dialect mysql
cause: mysql requirement
solution: src_address = Column(String(16), index=True)

ValueError: [TypeError("'coroutine' object is not iterable"), TypeError('vars() argument must have __dict__ attribute')]
cause: in async controller function, not using await
solution: add await

 RecursionError: maximum recursion depth exceeded in comparison
 caust: my error with naming the controller function the same as the function being called in the crud file
 solution: resolve the scoping issue 

old code being used
cause: docker compose build must run again 
solution: rerun docker-compose -d --build

new database is not being used, old one still being used
cause: docker compose using a cached volume
solution: purge the volume and rebuild the container

even with depends-on, the app runs before the db is ready
cause: the db has not complated initialization, even after the container was fired up
solution: need a script wait-for-it.sh to run in the app
1.  copy the script over
2.  ENTRYPOINT ["wait-for-it.sh", "db:3306", "--", "app_launch_commands"]

no perms on the script
cause: the volume copy was happening after the dockerFile copy/permission setting]
solution: remove the volume in docker-compose

standard_init_linux.go:178: exec user process caused “exec format error”
cause: bash was not set as the executor
solution: add #!/bin/bash to the script

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

### instructions

testing: cleans up docker and runs the test compose 
``` console
docker-compose -f docker-compose.test.yml down && docker-compose -f docker-compose.test.yml rm -v && docker-compose -f docker-compose.test.yml up -d --build && docker-compose -f docker-compose.test.yml up
```