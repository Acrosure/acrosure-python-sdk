# -*- coding: utf-8 -*-

import unittest
from ..client import AcrosureClient
from ..data import DataManager

from .constants import (
    TEST_PUBLIC_KEY,
)

class DataTestCase(unittest.TestCase):

    def setUp( self ):
        self.client = AcrosureClient(TEST_PUBLIC_KEY)
        self.data = self.client.data
    
    def test_instance_of_acrosure( self ):
        client = self.client
        data = self.data
        self.assertIsInstance(client, AcrosureClient)
        self.assertIsInstance(data, DataManager)

    def test_get_data_value_with_no_dependencies( self ):
        data = self.data
        values = data.get({
            "handler": "province"
        })
        self.assertIsInstance(values, list)

    def test_get_data_value_with_one_dependencies( self ):
        data = self.data
        values = data.get({
            "handler": "district",
            "dependencies": ["กรุงเทพมหานคร"]
        })
        self.assertIsInstance(values, list)

    def test_get_data_value_with_two_dependencies( self ):
        data = self.data
        values = data.get({
            "handler": "subdistrict",
            "dependencies": ["กรุงเทพมหานคร", "ห้วยขวาง"]
        })
        self.assertIsInstance(values, list)

if __name__ == '__main__':
    unittest.main()
