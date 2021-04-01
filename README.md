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

