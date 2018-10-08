# -*- coding: utf-8 -*-

import unittest
from ..client import AcrosureClient
from ..product import ProductManager

from .constants import (
    TEST_PUBLIC_KEY,
)

TEST_PRODUCT_ID = "prod_contractor"

class ProductTestCase(unittest.TestCase):

    def setUp( self ):
        self.client = AcrosureClient(TEST_PUBLIC_KEY)
        self.product = self.client.product
    
    def test_instance_of_acrosure( self ):
        client = self.client
        product = self.product
        self.assertIsInstance(client, AcrosureClient)
        self.assertIsInstance(product, ProductManager)

    def test_get_product_detail( self ):
        product = self.product
        product_detail = product.get(TEST_PRODUCT_ID)
        self.assertIsInstance(product_detail, dict)
        self.assertEqual(product_detail["id"], TEST_PRODUCT_ID)

    def test_list_products( self ):
        product = self.product
        products = product.list()
        self.assertIsInstance(products, list)

if __name__ == '__main__':
    unittest.main()
