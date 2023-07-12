from .base import UsersBaseTest
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from leads.models import Lead, Agent, Category
from django.urls import reverse
from time import sleep


class UserProfileTest(UsersBaseTest):
    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/div/div/div/form'
        )

    def get_modal_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[3]/div/div/form'
        )

    def test_dashboard_leads_return_correct_data(self):
        string_password = 'P@ssw0rd1'

        user = User.objects.create_user(
            username='my_user',
            password=string_password,
        )

        # Usuário abre a página de login
        self.browser.get(self.live_server_url + reverse('users:login'))

        # Usuário vê o formulário de login
        form = self.get_form()

        username_field = self.browser.find_element(By.NAME, 'username')
        password_field = self.browser.find_element(By.NAME, 'password')

        # Usuário digita seu usuário e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # Envia o formulário
        form.submit()

        # Usuário abre a página de leads
        self.browser.get(self.live_server_url + reverse('dashboard:leads'))

        # Vê o botão de criação de leads
        self.assertIn('No results found.',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_dashboard_leads_create_modal(self):
        string_password = 'P@ssw0rd1'

        user = User.objects.create_user(
            username='my_user',
            password=string_password,
        )

        Category.objects.create(
            name="Lore",
            description="Impsum",
        )

        Agent.objects.create(
            first_name="Pedro Henrique",
            last_name="Vieira",
            email="teste@teste.com",
            phone_number="22998438864"
        )

        Lead.objects.create(
            first_name="Pedro Henrique",
            last_name="Vieira",
            email="teste@teste.com",
            age="20",
            category_id=1,
            agent_id=1
        )

        # Usuário abre a página de login
        self.browser.get(self.live_server_url + reverse('users:login'))

        # Usuário vê o formulário de login
        form = self.get_form()

        username_field = self.browser.find_element(By.NAME, 'username')
        password_field = self.browser.find_element(By.NAME, 'password')

        # Usuário digita seu usuário e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # Envia o formulário
        form.submit()

        # Usuário abre a página de leads
        self.browser.get(self.live_server_url + reverse('dashboard:leads'))

        # Vê o botão de criação de leads e clicka para abrir o modal
        create_modal = self.browser.find_element(
            By.XPATH,
            '/html/body/div/main/section/div/div/div[1]/div[2]/button'
        )
        create_modal.click()

        # Usuário preenche os dados
        first_name_field = self.browser.find_element(By.NAME, 'first_name')
        last_name_field = self.browser.find_element(By.NAME, 'last_name')
        email_field = self.browser.find_element(By.NAME, 'email')
        age_field = self.browser.find_element(By.NAME, 'age')
        first_name_field.send_keys('Pedro Henrique')
        last_name_field.send_keys('Vieira')
        email_field.send_keys('peagahvieira2003@gmail.com')
        age_field.send_keys('20')

        # Envia o formulário
        modal_form = self.get_modal_form()
        modal_form.submit()

        # Vê o botão de criação de leads
        self.assertIn('Lead created successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)
