from django.test import TestCase
from django.urls import reverse


class UsersUrlsTest(TestCase):
    def test_users_login_url(self):
        login_url = reverse('users:login')
        self.assertEqual(login_url, '/')

    def test_users_register_url(self):
        register_url = reverse('users:register')
        self.assertEqual(register_url, '/users/register/')

    def test_users_password_reset_url(self):
        password_reset_url = reverse('users:password_reset')
        self.assertEqual(password_reset_url, '/users/password-reset/')

    def test_users_profile_url(self):
        profile_url = reverse('dashboard:profile')
        self.assertEqual(profile_url, '/dashboard/profile/')
