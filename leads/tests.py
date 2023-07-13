from django.test import TestCase
from django.urls import reverse, resolve
from leads import views
from django.contrib.auth.models import User


class LeadsTest(TestCase):
    def user_login(self):
        User.objects.create_user(username='my_user', password='my_pass')
        self.client.login(username='my_user', password='my_pass')

    def test_leads_search_return_successfully(self):
        self.user_login()

        response = self.client.get(
            reverse('dashboard:leads_search') +
            '?q=Teste'
        )

        self.assertIn(
            'Try search again for a lead',
            response.content.decode('utf-8')
        )

    def test_leads_search_raises_404_if_no_search_term(self):
        self.user_login()

        response = self.client.get(
            reverse('dashboard:leads_search') + '?q=')

        self.assertEqual(response.status_code, 404)

    def test_categories_search_return_successfully(self):
        self.user_login()

        response = self.client.get(
            reverse('dashboard:leads_category_search') +
            '?q=Teste'
        )

        self.assertIn(
            'Try search again for a category',
            response.content.decode('utf-8')
        )

    def test_categories_search_raises_404_if_no_search_term(self):
        self.user_login()

        response = self.client.get(
            reverse('dashboard:leads_category_search') + '?q=')

        self.assertEqual(response.status_code, 404)

    def test_agents_search_return_successfully(self):
        self.user_login()

        response = self.client.get(
            reverse('dashboard:leads_agent_search') +
            '?q=Teste'
        )

        self.assertIn(
            'Try search again for a agent',
            response.content.decode('utf-8')
        )

    def test_agents_search_raises_404_if_no_search_term(self):
        self.user_login()

        response = self.client.get(
            reverse('dashboard:leads_agent_search') + '?q=')

        self.assertEqual(response.status_code, 404)
