from django.test import TestCase
from django.urls import reverse


class AccountsUrlsTest(TestCase):
    def test_accounts_login_url(self):
        login_url = reverse('accounts:login')
        self.assertEqual(login_url, '/')

    def test_accounts_register_url(self):
        register_url = reverse('accounts:register')
        self.assertEqual(register_url, '/accounts/register/')

    def test_accounts_password_reset_url(self):
        password_reset_url = reverse('accounts:password_reset')
        self.assertEqual(password_reset_url, '/accounts/password-reset/')

    def test_accounts_profile_url(self):
        profile_url = reverse('dashboard:profile')
        self.assertEqual(profile_url, '/dashboard/profile/')
