from django.test import TestCase
from django.urls import reverse, resolve
from accounts import views


class AccountsViewsTest(TestCase):
    def test_accounts_login_view(self):
        login_view = resolve(reverse('accounts:login'))
        self.assertIs(
            login_view.func.__name__,
            views.LoginView.as_view().__name__
        )

    def test_accounts_login_view_status_code(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_accounts_register_view(self):
        register_view = resolve(reverse('accounts:register'))
        self.assertIs(
            register_view.func.__name__,
            views.RegisterView.as_view().__name__
        )

    def test_accounts_register_view_status_code(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)

    def test_accounts_logout_view_status_code(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)

    def test_accounts_profile_view(self):
        profile_view = resolve(reverse('dashboard:profile'))
        self.assertIs(profile_view.func.__name__,
                      views.UserProfileView.as_view().__name__)
