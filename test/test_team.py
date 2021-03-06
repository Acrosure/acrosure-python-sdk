import unittest
from acrosure_sdk import AcrosureClient
from acrosure_sdk.team import TeamManager
from .constants import (
    TEST_PUBLIC_KEY,
)
import os

API_URL = os.environ.get('API_URL')

class TeamTestCase(unittest.TestCase):

    def setUp( self ):
        self.client = AcrosureClient(TEST_PUBLIC_KEY, API_URL)
        self.team = self.client.team
    
    def test_1_instance_of_acrosure( self ):
        client = self.client
        team = self.team
        self.assertIsInstance(client, AcrosureClient)
        self.assertIsInstance(team, TeamManager)

    def test_2_get_team_info( self ):
        team = self.team
        resp = team.get_info()
        self.assertEqual(resp["status"], "ok")
        team_info = resp["data"]
        self.assertIsInstance(team_info, dict)

if __name__ == '__main__':
    unittest.main()
