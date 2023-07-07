from django.test import TestCase
from django.urls import reverse, resolve
from users import views


class UsersViewsTest(TestCase):
    def test_users_login_view(self):
        login_view = resolve(reverse('users:login'))
        self.assertIs(login_view.func, views.login_view)

    def test_users_login_view_status_code(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_users_register_view(self):
        register_view = resolve(reverse('users:register'))
        self.assertIs(
            register_view.func.__name__,
            views.RegisterView.as_view().__name__
        )

    def test_users_register_view_status_code(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
