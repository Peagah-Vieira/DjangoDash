from django.test import TestCase
from django.urls import reverse


class UsersUrlsTest(TestCase):
    def test_users_login_url(self):
        login_url = reverse('users:login')
        self.assertEqual(login_url, '/users/login/')
