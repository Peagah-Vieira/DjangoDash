from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={
            'placeholder': 'name@company.com',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
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
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    confirm_password = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        email_registered = User.objects.filter(email=email).exists()

        if email_registered:
            raise ValidationError(
                'User e-mail is already in use',
                code='invalid',
            )

        return email
