# -*- coding: utf-8 -*-

import unittest
from ..client import AcrosureClient
from ..policy import PolicyManager

from .constants import (
    TEST_PUBLIC_KEY,
)

TEST_POLICY_ID = "plcy_sample"

class PolicyTestCase(unittest.TestCase):

    def setUp( self ):
        self.client = AcrosureClient(TEST_PUBLIC_KEY)
        self.policy = self.client.policy
    
    def test_instance_of_acrosure( self ):
        client = self.client
        policy = self.policy
        self.assertIsInstance(client, AcrosureClient)
        self.assertIsInstance(policy, PolicyManager)

    def test_get_policy_detail( self ):
        policy = self.policy
        policy_detail = policy.get(TEST_POLICY_ID)
        self.assertIsInstance(policy_detail, dict)
        self.assertEqual(policy_detail["id"], TEST_POLICY_ID)

    def test_list_policies( self ):
        policy = self.policy
        policies = policy.list()
        self.assertIsInstance(policies, list)

if __name__ == '__main__':
    unittest.main()
