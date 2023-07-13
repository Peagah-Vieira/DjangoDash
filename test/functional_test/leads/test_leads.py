from .base import LeadBaseTest
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from leads.models import Lead, Agent, Category
from django.urls import reverse
from time import sleep


class LeadsTest(LeadBaseTest):
    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/div/div/div/form'
        )

    def user_login(self):
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

    def get_create_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[3]/div/div/form'
        )

    def get_update_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[4]/div/div/form'
        )

    def data_create(self):
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
        )

    def test_leads_return_correct_data(self):
        # Usuario faz login
        self.user_login()

        # Usuário abre a página de leads
        self.browser.get(self.live_server_url + reverse('dashboard:leads'))

        # Vê o botão de criação de leads
        self.assertIn('No results found.',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_leads_create_returns_successfully(self):
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

        # Usuario faz login
        self.user_login()

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
        create_form = self.get_create_form()
        create_form.submit()

        # Vê o botão de criação de leads
        self.assertIn('Lead created successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_leads_create_returns_error(self):
        # Usuario faz login
        self.user_login()

        # Usuário abre a página de leads
        self.browser.get(self.live_server_url + reverse('dashboard:leads'))

        # Vê o botão de criação de leads e clicka para abrir o modal
        create_modal = self.browser.find_element(
            By.XPATH,
            '/html/body/div/main/section/div/div/div[1]/div[2]/button'
        )
        create_modal.click()

        # Envia o formulário
        create_form = self.get_create_form()
        create_form.submit()

        # Vê o botão de criação de leads
        self.assertIn('Lead not created successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_leads_update_returns_succesfully(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de leads
        self.browser.get(self.live_server_url + reverse('dashboard:leads'))

        # Vê o botão de criação de leads e clicka para abrir o modal
        update_modal = self.browser.find_element(By.NAME, 'item_update')
        update_modal.click()

        # Usuário preenche os dados
        first_name_field = self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[4]/div/div/form/div/div[1]/input'
        )
        last_name_field = self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[4]/div/div/form/div/div[2]/input'
        )
        email_field = self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[4]/div/div/form/div/div[3]/input'
        )
        age_field = self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[4]/div/div/form/div/div[4]/input'
        )
        first_name_field.send_keys('Pedro Henrique')
        last_name_field.send_keys('Vieira')
        email_field.send_keys('peagahvieira2003@gmail.com')
        age_field.send_keys('20')

        # Envia o formulário
        update_form = self.get_update_form()
        update_form.submit()

        # Recebe a mensagem de update
        self.assertIn('Lead updated successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_leads_update_returns_error(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de leads
        self.browser.get(self.live_server_url + reverse('dashboard:leads'))

        # Vê o botão de criação de leads e clicka para abrir o modal
        update_modal = self.browser.find_element(By.NAME, 'item_update')
        update_modal.click()

        # Envia o formulário
        update_form = self.get_update_form()
        update_form.submit()

        # Recebe a mensagem de update
        self.assertIn('Lead not updated successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_leads_delete_returns_successfully(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de leads
        self.browser.get(self.live_server_url + reverse('dashboard:leads'))

        # Vê o botão de delete
        delete_modal = self.browser.find_element(By.NAME, 'item_delete')
        delete_modal.click()

        # Vê o botão de confirmação do delete
        delete_button = self.browser.find_element(
            By.ID,
            'confirmDeleteButtonModal'
        )
        delete_button.click()

        # Recebe a mensagem de delete
        self.assertIn('Lead deleted successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_leads_export_returns_successfully(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de leads
        self.browser.get(self.live_server_url + reverse('dashboard:leads'))

        # Vê o botão de ações
        action_button = self.browser.find_element(
            By.XPATH, '//*[@id="actionsDropdownButton"]')
        action_button.click()

        # Vê o botão de exportar
        export_button = self.browser.find_element(
            By.XPATH, '//*[@id="actionsDropdown"]/ul/li/a')
        export_button.click()

        # Recebe a mensagem de exportar
        self.assertIn('Lead export successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)
