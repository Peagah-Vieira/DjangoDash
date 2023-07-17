from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountsLogoutTest(TestCase):
    def test_user_tries_to_logout_using_get_method(self):
        User.objects.create_user(username='my_user', password='my_pass')
        self.client.login(username='my_user', password='my_pass')

        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 405)

    def test_user_can_logout_successfully(self):
        User.objects.create_user(username='my_user', password='my_pass')
        self.client.login(username='my_user', password='my_pass')

        response = self.client.post(
            reverse('accounts:logout'),
            data={
                'username': 'my_user'
            },
            follow=True
        )

        self.assertIn(
            'Logged out successfully',
            response.content.decode('utf-8')
        )
