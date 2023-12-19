
import requests

def my_func():
    pass

class Human:
    pass

class Worker(Human):
    pass


x = my_func
nick = Human

print(requests.__name__)
print(my_func.__name__)
print(x.__name__)
print(Human.__name__)
print(nick.__name__)
print(__name__)

print(type(requests))

for method in dir():
    print(method)
print(list(dir()))

l = list()
print(hasattr(l, 'append'))
print(hasattr(l, 'split'))
print(getattr(l, 'split', None))
print(getattr(l, 'append'))

print(callable(my_func))
print(callable(l))

print(issubclass(Human, Worker))
print(issubclass(Worker, Human))

print(isinstance('hello', str))
print(isinstance('hello', int))

import inspect

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))


print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))

import sys

print(sys.executable)
print(sys.version)
print(sys.platform)
print(sys.argv)
print('======================')
for mn, mp in sys.modules.items():
    print(mn, mp)

print(dir(__build__))

