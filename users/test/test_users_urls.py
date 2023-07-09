from django.test import TestCase
from django.urls import reverse


class UsersUrlsTest(TestCase):
    def test_users_login_url(self):
        login_url = reverse('users:login')
        self.assertEqual(login_url, '/')

    def test_users_register_url(self):
        register_url = reverse('users:register')
        self.assertEqual(register_url, '/users/register/')
