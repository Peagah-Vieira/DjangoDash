from django import forms
from leads.models import Agent


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]

    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Type first name',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Type last name',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Type email',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={
            'placeholder': 'Type phone number',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )
