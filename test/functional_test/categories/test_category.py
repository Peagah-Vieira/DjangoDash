from .base import CategoryBaseTest
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from leads.models import Lead, Agent, Category
from django.urls import reverse
from time import sleep


class CategoriesTest(CategoryBaseTest):
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
            '//*[@id="categoryCreateModal"]/div/div/form'
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

    def test_categories_return_correct_data(self):
        # Usuario faz login
        self.user_login()

        # Usuário abre a página de categorias
        self.browser.get(
            self.live_server_url +
            reverse('dashboard:leads_category')
        )

        # Vê a mensagem de procurar por outras categorias
        self.assertIn('Try search again for a category',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_categories_create_returns_successfully(self):
        # Usuario faz login
        self.user_login()

        # Usuário abre a página de categorias
        self.browser.get(
            self.live_server_url +
            reverse('dashboard:leads_category')
        )

        # Vê o botão de criação de categorias e clicka para abrir o modal
        create_modal = self.browser.find_element(
            By.XPATH,
            '/html/body/div/main/section/div/div/div[1]/div[2]/button'
        )
        create_modal.click()

        # Usuário preenche os dados
        name_field = self.browser.find_element(By.NAME, 'name')
        description_field = self.browser.find_element(By.NAME, 'description')
        name_field.send_keys('Teste')
        description_field.send_keys('Teste')

        # Envia o formulário
        create_form = self.get_create_form()
        create_form.submit()

        # Vê a mensagem de criação bem sucedida
        self.assertIn('Category created successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_categories_create_returns_error(self):
        # Usuario faz login
        self.user_login()

        # Usuário abre a página de categorias
        self.browser.get(
            self.live_server_url +
            reverse('dashboard:leads_category')
        )

        # Vê o botão de criação de categorias e clicka para abrir o modal
        create_modal = self.browser.find_element(
            By.XPATH,
            '/html/body/div/main/section/div/div/div[1]/div[2]/button'
        )
        create_modal.click()

        # Envia o formulário
        create_form = self.get_create_form()
        create_form.submit()

        # Vê a mensagem de criação bem sucedida
        self.assertIn('Category not created successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_categories_update_returns_succesfully(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de category
        self.browser.get(self.live_server_url +
                         reverse('dashboard:leads_category'))

        # Vê o botão de update de category e clicka para abrir o modal
        update_modal = self.browser.find_element(By.NAME, 'item_update')
        update_modal.click()

        # Usuário preenche os dados
        name_field = self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[4]/div/div/form/div/div[1]/input'
        )
        description_field = self.browser.find_element(
            By.XPATH,
            '/html/body/div[1]/main/section/div/div/div[4]/div/div/form/div/div[2]/textarea'
        )

        name_field.send_keys('Teste')
        description_field.send_keys('Teste')

        # Envia o formulário
        update_form = self.get_update_form()
        update_form.submit()

        # Recebe a mensagem de update
        self.assertIn('Category updated successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_categories_update_returns_error(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de category
        self.browser.get(self.live_server_url +
                         reverse('dashboard:leads_category'))

        # Vê o botão de update de category e clicka para abrir o modal
        update_modal = self.browser.find_element(By.NAME, 'item_update')
        update_modal.click()

        # Envia o formulário
        update_form = self.get_update_form()
        update_form.submit()

        # Recebe a mensagem de update
        self.assertIn('Category not updated successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_categories_delete_returns_successfully(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de categorias
        self.browser.get(
            self.live_server_url +
            reverse('dashboard:leads_category')
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

        # Recebe a mensagem de delete
        self.assertIn('Category deleted successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)

    def test_categories_export_returns_successfully(self):
        # Criação de dados
        self.data_create()

        # Usuario faz login
        self.user_login()

        # Usuário abre a página de leads
        self.browser.get(self.live_server_url +
                         reverse('dashboard:leads_category'))

        # Vê o botão de ações
        action_button = self.browser.find_element(
            By.XPATH, '//*[@id="actionsDropdownButton"]')
        action_button.click()

        # Vê o botão de exportar
        export_button = self.browser.find_element(
            By.XPATH, '//*[@id="actionsDropdown"]/ul/li/a')
        export_button.click()

        # Recebe a mensagem de exportar
        self.assertIn('Category export successfully',
                      self.browser.find_element(By.TAG_NAME, 'body').text)
