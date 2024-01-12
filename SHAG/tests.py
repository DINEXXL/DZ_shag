# import unittest
# from _2 import adder
#
# class MyTest(unittest.TestCase):
#     def test_args(self):
#         self.assertEquals(adder(2, 2), 4)
#     def test_kwargs(self):
#         self.assertEquals(adder(a=10, b=11), 21)
#
#     def test_mixed(self):
#         self.assertEquals(adder(1, a=2), 3)
#
#     def test_diff(self):
#         x = 10
#         y = 0
#         self.assertEquals(adder(0, -5, y, a=x), 5)
#
#     def test_wrong_datatype(self):
#         self.assertEquals(adder())

def adder(*args, **kwargs):
    res = 0
    for _ in args:
        if isinstance()