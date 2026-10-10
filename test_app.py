import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a temporary test client for our Flask application
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_addition(self):
        # Test if 5 + 3 equals 8.0
        response = self.client.post('/', data={'num1': '5', 'num2': '3', 'operation': 'add'})
        self.assertIn(b'Result: 8.0', response.data)

    def test_division_by_zero(self):
        # Test if dividing by zero displays our custom security error banner
        response = self.client.post('/', data={'num1': '10', 'num2': '0', 'operation': 'divide'})
        self.assertIn(b'Error: Cannot divide by zero!', response.data)

if __name__ == '__main__':
    unittest.main()