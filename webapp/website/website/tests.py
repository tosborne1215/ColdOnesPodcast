import unittest
from django.test import Client
from django.core.urlresolvers import reverse


class BasicWebsiteTest(unittest.TestCase):
    fixtures = ['test.data.json']

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_index(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        # Issue a 404
        response = self.client.get('/404')

        self.assertEqual(response.status_code, 404)

    def test_about(self):
        # Issue a GET request.
        response = self.client.get(reverse('about'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_contactus(self):
        # Issue a GET request.
        response = self.client.get(reverse('contactus'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_forum(self):
        # Issue a GET request.
        response = self.client.get(reverse('forum'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_legal(self):
        # Issue a GET request.
        response = self.client.get(reverse('legal'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_privacypolicy(self):
        # Issue a GET request.
        response = self.client.get(reverse('privacypolicy'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        # Issue a GET request.
        response = self.client.get(reverse('search'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
