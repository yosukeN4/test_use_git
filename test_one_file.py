import unittest
from one_file import hello

class Checkfunction(unittest.TestCase):
    # from one_file import hello
    def test_func_hello(self):
        # result = hello()
        self.assertEqual(hello(), "hi, world!") # why hello() is not defined?

class Checkfunction_import(unittest.TestCase):
    # from one_file import hello
    def test_func_inside(self):
        from one_file import hello
        # result = hello()
        self.assertEqual(hello(), "hi, world!")