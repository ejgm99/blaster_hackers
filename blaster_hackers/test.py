import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.urls = ["/projects","/inventory","/uploads","/"]
    def test_details(self):
        # Issue a GET request.
        for url in self.urls:
            print("testing url "+url)
            response = self.client.get(url)
            # Check that the response is 200 OK.
            self.assertEqual(response.status_code, 200)
            print(url+" passed")
        # # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)
