# # class Human:
# #     height = 170
# # class Student(Human):
# #     gladness = 50
# # class Worker(Human):
# #     gladness = 30
# #
# #
# # nick = Student()
# # ann = Worker()
# #
# # print(nick.gladness)
# # print(ann.gladness)
#
#
# class HelloWorld:
#
#     hello = 'hello'
#     _hello = '_hello'
#     __hello = '__hello'
#
#     def __init__(self):
#         self.world = 'world'
#         self._world = '__world'
#         self.__world = '__world'
#
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# class test(HelloWorld):
#     def print_hi(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
# #
# # hello - HelloWorld()
# # hello.printer()
# # x = test()
# # x.printer_hi()
# #
# class Hello:
#     def __init__(self):
#         print("Hello!")
# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World!")
#
# hw = Hello_World()

# class Grandparent:
#     def about(self):
#         print("I am GrandParent")

#     def about_myself(self):
#         print("I am Grandparent")


# class Parent(Grandparent):
#     def about_myself(self):
#         print("I am Parent")


# class Child(Parent):
#     def __init__(self):
#         super().about()
#         super().about_myself()

# c = Child()

import random

class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128
class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"

class SmartPhone(Display, Computer):

    def info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)

class Cipher:
    def __init__(self, num):
        self.num = num + random.randint(1, 1000) * 23

    def __str__(self):
        return str(self.num)

Cipher = (1)
print("password for your IPhone =", Cipher)

iphone = SmartPhone(model = "IPhone 25 Pro max super puper ultra 60HZ")
iphone.info()