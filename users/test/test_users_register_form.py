from django.test import TestCase
from parameterized import parameterized
from users.forms import RegisterForm


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
