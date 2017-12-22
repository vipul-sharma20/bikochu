from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class SearchTest(TestCase):

    fixtures = ['test_users.json']

    def test_search_no_auth(self):
        response = self.client.get('/tweets/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
                response.data,
                {"detail": "Authentication credentials were not provided."})

    def test_search_with_auth(self):
        token = Token.objects.get(user__username='bruce')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.get('/tweets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

