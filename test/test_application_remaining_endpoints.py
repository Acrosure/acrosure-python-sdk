import unittest
from acrosure_sdk import AcrosureClient
from acrosure_sdk.application import ApplicationManager

from .constants import (
    TEST_PUBLIC_KEY,
)

class ApplicationRemainingEndPointsTestCase(unittest.TestCase):

    def setUp( self ):
        self.client = AcrosureClient(TEST_PUBLIC_KEY)
        self.application = self.client.application

    def test_1_list_applications( self ):
        application = self.application
        resp = application.list()
        self.assertEqual(resp["status"], "ok")
        applications = resp["data"]
        self.assertIsInstance(applications, list)

if __name__ == '__main__':
    unittest.main()
