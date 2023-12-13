import unittest
from one_file import hello

class Checkfunction(unittest.TestCase):
    def test_func_hello(self):
        # from one_file import hello
        # result = hello()
        self.assertEqual(hello(), "hi, world!")