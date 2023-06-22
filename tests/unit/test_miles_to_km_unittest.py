import unittest
import logging
from miles_to_km.core import miles_to_km, km_to_miles

# Get logger
logger = logging.getLogger('__miles_to_km__')
logger.setLevel(logging.INFO)

class Test(unittest.TestCase):
    def test_miles_to_km(self):
        self.assertEqual(miles_to_km(1), 1.61)

    def test_km_to_miles(self):
        self.assertEqual(km_to_miles(1), 0.62)

    def test_miles_to_km_dict_type(self):
        with self.assertRaises(TypeError):
            miles_to_km({'a': 1, 'b': 2})

    def test_miles_to_km_list_type(self):
        with self.assertRaises(TypeError):
            miles_to_km([1,2,3])
            