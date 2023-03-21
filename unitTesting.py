import unittest
from testing import app

class TestFlaskRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_signup_route(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_home_route(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200)


    def test_quiz_route(self):
        response = self.app.get('/quiz')
        self.assertEqual(response.status_code, 200)

    def test_testomonial_route(self):
        response = self.app.get('/testo1')
        self.assertEqual(response.status_code, 200)

    def test_databaseData_route(self):
        response = self.app.get('/testo11')
        self.assertEqual(response.status_code, 405)

    def test_aboutUs_route(self):
        response = self.app.get('/aboutUs')
        self.assertEqual(response.status_code, 200)

    def test_tips_route(self):
        response = self.app.get('/tips')
        self.assertEqual(response.status_code, 404)

    def test_main_route(self):
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 405)

    def test_tips_route(self):
        response = self.app.get('/tips')
        self.assertEqual(response.status_code, 200)

    
    
    
if __name__ == '__main__':
    unittest.main()
