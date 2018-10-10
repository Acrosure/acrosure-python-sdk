# -*- coding: utf-8 -*-

import unittest
from ..client import AcrosureClient
from ..application import ApplicationManager

from .constants import (
    TEST_PUBLIC_KEY,
    TEST_SECRET_KEY,
    CONFIRM_APP_DATA,
)

class ApplicationFlowTestCase(unittest.TestCase):

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
        resp = application.create(CONFIRM_APP_DATA["product_id"])
        self.assertEqual(resp["status"], "ok")
        created_application = resp["data"]
        self.assertTrue(created_application)
        self.assertTrue(created_application["id"])
        self.assertEqual(created_application["status"], "INITIAL")

    def test_get_application( self ):
        application = self.application
        resp = application.get()
        self.assertEqual(resp["status"], "ok")
        got_application = resp["data"]
        self.assertTrue(got_application)
        self.assertTrue(got_application["id"])
    
    def test_update_application( self ):
        application = self.application
        resp = application.update( basic_data = CONFIRM_APP_DATA["basic_data"] )
        self.assertEqual(resp["status"], "ok")
        updated_application = resp["data"]
        self.assertTrue(updated_application)
        self.assertTrue(updated_application["id"])
        self.assertEqual(updated_application["status"], "PACKAGE_REQUIRED")

    def test_get_packages( self ):
        application = self.application
        resp = application.get_packages()
        self.assertEqual(resp["status"], "ok")
        self.packages = resp["data"]
        self.assertIsInstance(self.packages, list)
        self.assertTrue(len(self.packages) > 0)
    
    def test_select_package( self ):
        application = self.application
        first_package = self.packages[0]
        resp = application.select_package({
            "package_code": first_package["package_code"]
        })
        self.assertEqual(resp["status"], "ok")
        updated_application = resp["data"]
        self.assertEqual(updated_application["status"], "DATA_REQUIRED")
    
    def test_get_current_package( self ):
        application = self.application
        resp = application.get_package()
        self.assertEqual(resp["status"], "ok")
        current_package = resp["data"]
        self.assertIsInstance(current_package, dict)

    def test_update_application_with_completed_data( self ):
        application = self.application
        resp = application.update(
            basic_data = CONFIRM_APP_DATA["basic_data"],
            package_options = CONFIRM_APP_DATA["package_options"],
            additional_data = CONFIRM_APP_DATA["additional_data"]
        ) 
        self.assertEqual(resp["status"], "ok")
        updated_application = resp["data"]
        self.assertTrue(updated_application)
        self.assertTrue(updated_application["id"])
        self.assertEqual(updated_application["status"], "READY")
    
    def test_confirm_application( self ):
        application = self.application
        admin_client = AcrosureClient(
            token = TEST_SECRET_KEY,
            application_id = application.id
        )
        user_application = admin_client.application
        resp = user_application.confirm()
        self.assertEqual(resp["status"], "error")
        confirmed_application = resp["status"]
        self.assertTrue(confirmed_application)
        self.assertTrue(confirmed_application["id"])
        self.assertEqual(confirmed_application["status"], "CONFIRMING")

if __name__ == '__main__':
    unittest.main()
