from .base import AgentBaseTest
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from leads.models import Agent
from django.urls import reverse


class AgentsTest(AgentBaseTest):
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
        self.browser.get(self.live_server_url + reverse('accounts:login'))

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
            '//*[@id="agentCreateModal"]/div/div/form'
        )

    def get_update_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[4]/div/div/form'
        )

    def data_create(self):
        Agent.objects.create(
            first_name="Pedro Henrique",
            last_name="Vieira",
            email="test@test.com",
            phone_number="99999999999"
        )

    def test_agents_return_correct_data(self):
        # Usuario faz login
        self.user_login()

        # Usuário abre a página de agentes
        self.browser.get(
            self.live_server_url +
            reverse('dashboard:leads_agent')
        )

        # Vê a mensagem de procurar por outras agentes
        self.assertIn('Try search again for a agent',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_agents_create_returns_successfully(self):
        # Usuario faz login
        self.user_login()

        # Usuário abre a página de agentes
        self.browser.get(
            self.live_server_url +
            reverse('dashboard:leads_agent')
        )

        # Vê o botão de criação de agentes e clicka para abrir o modal
        create_modal = self.browser.find_element(
            By.XPATH,
            '/html/body/div/main/section/div/div/div[1]/div[2]/button'
        )
        create_modal.click()

        # Usuário preenche os dados
        first_name_field = self.browser.find_element(By.NAME, 'first_name')
        last_name_field = self.browser.find_element(By.NAME, 'last_name')
        email_field = self.browser.find_element(By.NAME, 'email')
        phone_number_field = self.browser.find_element(By.NAME, 'phone_number')
        first_name_field.send_keys('John Doe')
        last_name_field.send_keys('Impsum')
        email_field.send_keys('test@test.com')
        phone_number_field.send_keys('99999999999')

        # Envia o formulário
        create_form = self.get_create_form()
        create_form.submit()

        # Vê a mensagem de criação bem sucedida
        self.assertIn('Agent created successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_agents_create_returns_error(self):
        # Usuario faz login
        self.user_login()

        # Usuário abre a página de agentes
        self.browser.get(
            self.live_server_url +
            reverse('dashboard:leads_agent')
        )

        # Vê o botão de criação de agentes e clicka para abrir o modal
        create_modal = self.browser.find_element(
            By.XPATH,
            '/html/body/div/main/section/div/div/div[1]/div[2]/button'
        )
        create_modal.click()

        # Envia o formulário
        create_form = self.get_create_form()
        create_form.submit()

        # Vê a mensagem de erro na criação
        self.assertIn('Agent not created successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_agents_update_returns_succesfully(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de agentes
        self.browser.get(self.live_server_url +
                         reverse('dashboard:leads_agent'))

        # Vê o botão de update de category e clicka para abrir o modal
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
        phone_number_field = self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[4]/div/div/form/div/div[4]/input'
        )
        first_name_field.send_keys('John Doe')
        last_name_field.send_keys('Impsum')
        email_field.send_keys('test@test.com')
        phone_number_field.send_keys('99999999999')

        # Envia o formulário
        update_form = self.get_update_form()
        update_form.submit()

        # Recebe a mensagem de update
        self.assertIn('Agent updated successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_agents_update_returns_error(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de agentes
        self.browser.get(self.live_server_url +
                         reverse('dashboard:leads_agent'))

        # Vê o botão de update de agentes e clicka para abrir o modal
        update_modal = self.browser.find_element(By.NAME, 'item_update')
        update_modal.click()

        # Envia o formulário
        update_form = self.get_update_form()
        update_form.submit()

        # Recebe a mensagem de update bem sucedido
        self.assertIn('Agent not updated successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_agents_delete_returns_successfully(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de agentes
        self.browser.get(
            self.live_server_url +
            reverse('dashboard:leads_agent')
        )

        # Vê o botão de delete
        delete_modal = self.browser.find_element(By.NAME, 'item_delete')
        delete_modal.click()

        # Vê o botão de confirmação do delete
        delete_button = self.browser.find_element(
            By.ID,
            'confirmDeleteButtonModal'
        )
        delete_button.click()

        # Recebe a mensagem de delete bem sucedida
        self.assertIn('Agent deleted successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_agents_export_returns_successfully(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de agentes
        self.browser.get(self.live_server_url +
                         reverse('dashboard:leads_agent'))

        # Vê o botão de ações
        action_button = self.browser.find_element(
            By.XPATH, '//*[@id="actionsDropdownButton"]')
        action_button.click()

        # Vê o botão de exportar
        export_button = self.browser.find_element(
            By.XPATH, '//*[@id="actionsDropdown"]/ul/li/a')
        export_button.click()

        # Recebe a mensagem de exportar bem sucedida
        self.assertIn('Agent export successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)
