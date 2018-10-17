import unittest
from acrosure_sdk import AcrosureClient
from acrosure_sdk.policy import PolicyManager
from .constants import (
    TEST_PUBLIC_KEY,
)
import os

API_URL = os.environ.get('API_URL')

class PolicyTestCase(unittest.TestCase):

    POLICIES = []

    def setUp( self ):
        self.client = AcrosureClient(TEST_PUBLIC_KEY, API_URL)
        self.policy = self.client.policy
    
    def test_1_instance_of_acrosure( self ):
        client = self.client
        policy = self.policy
        self.assertIsInstance(client, AcrosureClient)
        self.assertIsInstance(policy, PolicyManager)

    def test_2_list_policies( self ):
        policy = self.policy
        resp = policy.list()
        self.assertEqual(resp["status"], "ok")
        policies = resp["data"]
        self.assertIsInstance(policies, list)
        self.assertTrue(len(policies) > 0)
        self.__class__.POLICIES = policies

    def test_3_get_policy_detail( self ):
        policy = self.policy
        policy_id = self.__class__.POLICIES[0]["id"]
        resp = policy.get(policy_id)
        self.assertEqual(resp["status"], "ok")
        policy_detail = resp["data"]
        self.assertIsInstance(policy_detail, dict)
        self.assertEqual(policy_detail["id"], policy_id)


if __name__ == '__main__':
    unittest.main()
