import os
import json
import jwt
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class TestAPI(TestCase):
    def test_signUp(self):
        client = APIClient()
        response = client.post(
            '/register/',
            {
                "username": "user_prueba_1",
                "password": "password_prueba_1",
                "first_name": "john",
                "last_name": "doe",
                "email": "dev@dev.com",
                "country": "Colombia",
            },
            format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('refresh' in response.data.keys(), True)
        self.assertEqual('access' in response.data.keys(), True)

    def test_login(self):
        client = APIClient()
        response = client.post(
            '/login/',
            {
                "username": "johndoe",
                "password": "123456"
            },
            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('refresh' in response.data.keys(), True)
        self.assertEqual('access' in response.data.keys(), True)

    def test_user(self):
        client = APIClient()
        token_access = client.post(
            '/login/',
            {"username": "johndoe", "password": "123456"},
            format='json'
        ).data["access"]

        secret = os.environ.get(
            'SECRET_KEY', 'django-insecure-3ngw8dbn4&wx8f%7***+m(%7$p7l(3sm!1pkmq3&u!6=ng39a8')
        user_id = jwt.decode(token_access, secret,
                             algorithms=["HS256"])["user_id"]

        url = '/user/' + str(user_id) + '/'
        auth_headers = {'HTTP_AUTHORIZATION': 'Bearer ' + token_access, }

        response = client.get(url, **auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "johndoe")
