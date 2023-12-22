#
# import requests
#
# def my_func():
#     pass
#
# class Human:
#     pass
#
# class Worker(Human):
#     pass
#
#
# x = my_func
# nick = Human
#
# print(requests.__name__)
# print(my_func.__name__)
# print(x.__name__)
# print(Human.__name__)
# print(nick.__name__)
# print(__name__)
#
# print(type(requests))
#
# for method in dir():
#     print(method)
# print(list(dir()))
#
# l = list()
# print(hasattr(l, 'append'))
# print(hasattr(l, 'split'))
# print(getattr(l, 'split', None))
# print(getattr(l, 'append'))
#
# print(callable(my_func))
# print(callable(l))
#
# print(issubclass(Human, Worker))
# print(issubclass(Worker, Human))
#
# print(isinstance('hello', str))
# print(isinstance('hello', int))

import inspect
import colorama

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))

for name, data in inspect.getmembers(colorama):
    if name.startswith('__'):
        continue
    print(f"{name} : {data}")

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print(inspect.getmodule(list))

print(dir(__builtins__))