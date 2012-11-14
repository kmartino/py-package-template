import unittest

from packagetemplate import sample

class BasicTests(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual('hello world', sample.hello_world())
