import json
from datetime import datetime

# Default arguements:
def log(message, when = datetime.now()):
    print(when,':',  message)

log('Hi There!!')
log('Hi Again!!')
# default arguements will evaluated when the module will load i.e at program start up
# Default arguements should be NONE for mutable arguements why beacause default will be shared by all. e.g
def decode(data, default = {}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['something'] = 1
print('Foo: ', foo)
bar = decode('again bad data')
bar['something else']=5
print('Foo: ', foo)
print('Bar: ', bar)

def decode_with_default_as_none(data, default =None):
    if default == None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode_with_default_as_none('bad data')
foo['something'] = 1
bar = decode_with_default_as_none('again bad data')
bar['something else']=5
print('Foo with decode as None: ', foo)
print('Bar with decode as None: ', bar)