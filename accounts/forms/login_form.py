from django import forms


class LoginForm(forms.Form):
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

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )
