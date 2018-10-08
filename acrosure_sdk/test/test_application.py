# -*- coding: utf-8 -*-

import unittest
from ..client import AcrosureClient
from ..application import ApplicationManager

from .constants import (
    TEST_SECRET_KEY,
    SUBMIT_APP_DATA,
)

class ApplicationTestCase(unittest.TestCase):

    def setUp( self ):
        self.client = AcrosureClient(TEST_SECRET_KEY)
        self.application = self.client.application
        self.packages = []
    
    def test_instance_of_acrosure( self ):
        client = self.client
        application = self.application
        self.assertIsInstance(client, AcrosureClient)
        self.assertIsInstance(application, ApplicationManager)
    
    def test_create_with_empty_data( self ):
        application = self.application
        created_app = application.create(SUBMIT_APP_DATA["product_id"])
        self.assertTrue(created_app)
        self.assertTrue(created_app["id"])
        self.assertEqual(created_app["status"], "INITIAL")

    def test_get_application( self ):
        application = self.application
        got_application = application.get()
        self.assertTrue(got_application)
        self.assertTrue(got_application["id"], application.id)
    
    def test_update_application( self ):
        application = self.application
        updated_application = application.update( basic_data = SUBMIT_APP_DATA["basic_data"] )
        self.assertTrue(updated_application)
        self.assertTrue(updated_application["id"])
        self.assertEqual(updated_application["status"], "PACKAGE_REQUIRED")

    def test_get_packages( self ):
        application = self.application
        self.packages = application.get_packages()
        self.assertIsInstance(self.packages, list)
        self.assertTrue(len(self.packages) > 0)
    
    def test_select_package( self ):
        application = self.application
        first_package = self.packages[0]
        updated_application = application.select_package({
            "package_code": first_package["package_code"]
        })
        self.assertEqual(updated_application["status"], "DATA_REQUIRED")
    
    def test_get_current_package( self ):
        application = self.application
        current_package = application.get_package()
        self.assertIsInstance(current_package, dict)

    def test_update_application_with_completed_data( self ):
        application = self.application
        updated_application = application.update(
            basic_data = SUBMIT_APP_DATA["basic_data"],
            package_options = SUBMIT_APP_DATA["package_options"],
            additional_data = SUBMIT_APP_DATA["additional_data"]
        ) 
        self.assertTrue(updated_application)
        self.assertTrue(updated_application["id"])
        self.assertEqual(updated_application["status"], "READY")
    
    def test_get_2c2p_hash_form( self ):
        application = self.application
        hash_form = application.get_2

#   it('get 2c2p hash form', async () => {
#     const hashForm = await application.get2C2PForm({
#       frontend_url: 'https://acrosure.com'
#     })
#     expect(hashForm).toBeInstanceOf(HTMLFormElement)
#   })

#   it('submit application', async () => {
#     const submittedApp = await application.submit()
#     expect(submittedApp).toBeDefined()
#     expect(submittedApp.id).toBeDefined()
#     expect(submittedApp.status).toBe('SUBMITTED')
#   })


if __name__ == '__main__':
    unittest.main()

