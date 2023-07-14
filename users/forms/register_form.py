from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import strong_password


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'John Doe',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'name@company.com',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        validators=[strong_password],
        required=True,
    )

    confirm_password = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_exists = User.objects.filter(username=username).exists()

        if username_exists:
            raise ValidationError(
                'A user with that username already exists.',
                code='invalid'
            )

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise ValidationError(
                'User e-mail is already in use',
                code='invalid'
            )

        return email

    def clean(self):
        super(RegisterForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            password_confirmation_error = ValidationError(
                'The password does not match.',
                code='invalid'
            )
            raise ValidationError({
                'confirm_password': password_confirmation_error,
            })

        return self.cleaned_data
