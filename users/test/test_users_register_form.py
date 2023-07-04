from django.test import TestCase
from parameterized import parameterized
from users.forms import RegisterForm
from django.urls import reverse


class UsersRegisterForm(TestCase):
    @parameterized.expand([
        ('username', 'John Doe'),
        ('email', 'name@company.com'),
        ('password', '••••••••'),
        ('confirm_password', '••••••••'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('username', 'Username'),
        ('email', 'Email'),
        ('password', 'Password'),
        ('confirm_password', 'Confirm password'),
    ])
    def test_fields_label(self, field, label):
        form = RegisterForm()
        current_label = form[field].label
        self.assertEqual(current_label, label)

    def test_registration_create_request_type_get_returns_404(self):
        response = self.client.get(reverse('users:register_create'))
        self.assertEqual(response.status_code, 404)
