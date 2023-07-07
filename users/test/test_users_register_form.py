from django.test import TestCase
from parameterized import parameterized
from users.forms import RegisterForm
from django.urls import reverse
from django.contrib.auth.models import User


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

    def test_login_create_request_type_get_returns_404(self):
        response = self.client.get(reverse('users:login_create'))
        self.assertEqual(response.status_code, 404)


class UsersRegisterFormIntegrationTest(TestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'email': 'email@anyemail.com',
            'password': '1',
            'password2': '1',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('username', 'This field must not be empty'),
        ('email', 'This field must not be empty'),
        ('password', 'This field must not be empty'),
        ('confirm_password', 'This field must not be empty'),
    ])
    def test_field_can_be_empty(self, field, message):
        self.form_data[field] = ''
        url = reverse('users:register')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertIn(message, response.context['form'].errors.get(field))

    def test_username_field_must_be_unique(self):
        self.user = User.objects.create_user(
            username=self.form_data['username'])

        url = reverse('users:register')
        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'A user with that username already exists.'
        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_email_field_must_be_unique(self):
        self.user = User.objects.create_user(
            username=self.form_data['username'], email=self.form_data['email'])

        url = reverse('users:register')
        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'User e-mail is already in use'
        self.assertIn(msg, response.context['form'].errors.get('email'))

    def test_password_field_have_lower_upper_case_letters_and_numbers(self):
        self.form_data['password'] = 'abc123'
        url = reverse('users:register')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = ('Password must have at least one uppercase letter, one lowercase letter and one number. The length should be at least 8 characters.')  # noqa

        self.assertIn(msg, response.context['form'].errors.get('password'))

    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = '@A123abc123'
        self.form_data['confirm_password'] = '@A123abc1235'

        url = reverse('users:register')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertIn('The password does not match.',
                      response.context['form'].errors.get('confirm_password'))

        self.form_data['password'] = '@A123abc123'
        self.form_data['confirm_password'] = '@A123abc123'

        url = reverse('users:register')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn('The password does not match.',
                         response.content.decode('utf-8'))

    def test_author_created_can_login(self):
        url = reverse('users:register')

        self.form_data.update({
            'username': 'testuser',
            'password': '@Bc123456',
            'confirm_password': '@Bc123456',
        })

        self.client.post(url, data=self.form_data, follow=True)

        is_authenticated = self.client.login(
            username='testuser',
            password='@Bc123456'
        )

        self.assertTrue(is_authenticated)
