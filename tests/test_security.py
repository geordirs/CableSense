import unittest
from src.api import app

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.token = "cable-secure-token-2024"

    def test_unauthorized_access(self):
        # Accessing history without token should fail
        response = self.app.get('/api/history')
        self.assertEqual(response.status_code, 401)

    def test_authorized_access(self):
        # Accessing history with correct token should succeed
        response = self.app.get('/api/history', headers={'X-API-Token': self.token})
        self.assertEqual(response.status_code, 200)

    def test_public_access(self):
        # Root and status should be public (or handled differently)
        response = self.app.get('/api/status')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
