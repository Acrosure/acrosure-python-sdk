# -*- coding: utf-8 -*-

import unittest
from ..client import AcrosureClient
from ..application import ApplicationManager

from .constants import (
    TEST_PUBLIC_KEY,
    SUBMIT_APP_DATA,
)

PRODUCT_ID = "prod_contractor"
APPLICATION_ID = "sandbox_appl_lb3RhHns4O5hjwXa"
REF2 = "ref2"
PACKAGE_CODE = "ACROSURE:MOTOR:VOLUNTARY:110:2017:10:5282:22563:FIRSTCLASS:1_569_3597:390000:N:0:10:30:15"

packages = []

class ApplicationTestCase(unittest.TestCase):

    def setUp( self ):
        self.client = AcrosureClient(TEST_PUBLIC_KEY)
        self.application = self.client.application
        self.packages = []
    
    def test_instance_of_acrosure( self ):
        client = self.client
        application = self.application
        self.assertIsInstance(client, AcrosureClient)
        self.assertIsInstance(application, ApplicationManager)
    
    def test_create_with_empty_data( self ):
        application = self.application
        resp = application.create(PRODUCT_ID)
        self.assertEqual(resp["status"], "ok")
        created_application = resp["data"]
        self.assertTrue(created_application)
        self.assertTrue(created_application["id"])
        self.assertEqual(created_application["status"], "INITIAL")

    def test_get_application( self ):
        application = self.application
        resp = application.get(APPLICATION_ID)
        self.assertEqual(resp["status"], "ok")
        got_application = resp["data"]
        self.assertTrue(got_application)
        self.assertTrue(got_application["id"], APPLICATION_ID)
    
    def test_update_application( self ):
        application = self.application
        resp = application.update(APPLICATION_ID, ref2 = REF2 )
        self.assertEqual(resp["status"], "ok")
        updated_application = resp["data"]
        self.assertTrue(updated_application)
        self.assertTrue(updated_application["id"])
        self.assertEqual(updated_application["ref2"], REF2 )

    def test_get_packages( self ):
        application = self.application
        resp = application.get_packages(APPLICATION_ID)
        self.assertEqual(resp["status"], "ok")
        packages = resp["data"]
        self.assertIsInstance(packages, list)
        self.assertTrue(len(packages) > 0)
        # print("SELF11111111111111111111111111111")
        # print(len(packages))
    
    def test_select_package( self ):
        application = self.application
        # print("SELFFFFFFFFFFFFFFFFFFFF")
        # print(len(packages))
        # first_package = packages[0]
        resp = application.select_package(APPLICATION_ID, {
            "package_code": PACKAGE_CODE
            # "package_code": first_package["package_code"]
        })
        self.assertEqual(resp["status"], "ok")
        updated_application = resp["data"]
        self.assertEqual(updated_application["status"], "DATA_REQUIRED")
    
    def test_get_current_package( self ):
        application = self.application
        resp = application.get_package(APPLICATION_ID)
        self.assertEqual(resp["status"], "ok")
        current_package = resp["data"]
        self.assertIsInstance(current_package, dict)

    def test_update_application_with_completed_data( self ):
        application = self.application
        resp = application.update(
            APPLICATION_ID,
            basic_data = SUBMIT_APP_DATA["basic_data"],
            package_options = SUBMIT_APP_DATA["package_options"],
            additional_data = SUBMIT_APP_DATA["additional_data"]
        ) 
        self.assertEqual(resp["status"], "ok")
        updated_application = resp["data"]
        self.assertTrue(updated_application)
        self.assertTrue(updated_application["id"])
        self.assertEqual(updated_application["status"], "READY")

    def test_submit_application( self ):
        application = self.application
        resp = application.submit(APPLICATION_ID)
        self.assertEqual(resp["status"], "ok")
        submitted_application = resp["data"]
        self.assertTrue(submitted_application)
        self.assertTrue(submitted_application["id"])
        self.assertEqual(submitted_application["status"], "SUBMITTED")

if __name__ == '__main__':
    unittest.main()
