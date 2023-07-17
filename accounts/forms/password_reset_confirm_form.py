from django import forms
from django.contrib.auth.forms import SetPasswordForm


class SetPasswordCustomForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'placeholder': '••••••••',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'  # noqa
        }),
        strip=False,
    )

    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'placeholder': '••••••••',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'  # noqa
        }),
        strip=False,
    )
