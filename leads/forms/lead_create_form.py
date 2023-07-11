from django import forms
from leads.models import Lead, Category


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            "first_name",
            "last_name",
            "email",
            "age",
            "category",
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

    age = forms.CharField(
        label='Age',
        widget=forms.NumberInput(attrs={
            'placeholder': 'Age',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'  # noqa
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all().order_by('-id'),
        empty_label=None,
        widget=forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'  # noqa
        })
    )
