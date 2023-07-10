from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Type category name',
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )

    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={
            'placeholder': 'Write category description here',
            'rows': '2',
            'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'
        }),
        error_messages={
            'required': 'This field must not be empty'
        },
        required=True,
    )
