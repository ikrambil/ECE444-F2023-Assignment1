import unittest

from utils import utils

class TestUtils(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(utils.reversed(789), 987)
    
    def test_reversed2(self):
        self.assertEqual(utils.reversed(900), 9)
    
    def test_reversed3(self):
        self.assertEqual(utils.reversed('789'), 987)
    
    def test_reversed4(self):
        self.assertEqual(utils.reversed(543.00), 345)
    
    def test_formatter(self):
        self.assertEqual(utils.formatter(789), ('0b1100010101', '0o1425'))
    
    def test_formatter2(self):
        self.assertEqual(utils.formatter(900), ('0b1110000100', '0o1604'))
    
    def test_formatter3(self):
        self.assertEqual(utils.formatter('789'), ('0b1100010101', '0o1425'))
    
    def test_formatter4(self):
        self.assertEqual(utils.formatter(543.00), ('0b1000011111', '0o1037'))

        


unittest.main()