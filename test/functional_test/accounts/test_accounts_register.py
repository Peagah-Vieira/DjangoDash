from .base import AccountsBaseTest
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from django.urls import reverse


class AccountsRegisterTest(AccountsBaseTest):
    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/div/div/div/form'
        )

    def test_user_logged_cant_see_register_view(self):
        string_password = 'P@ssw0rd1'

        user = User.objects.create_user(
            username='my_user',
            password=string_password,
        )

        # Usuário abre a página de register
        self.browser.get(self.live_server_url + reverse('accounts:login'))

        # Usuário vê o formulário de register
        form = self.get_form()

        username_field = self.browser.find_element(By.NAME, 'username')
        password_field = self.browser.find_element(By.NAME, 'password')

        # Usuário digita seu usuário e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # Usuário envia o formulário
        form.submit()

        # Usuário é redirecionado para o dashboard
        response = self.client.get(reverse('dashboard:home'))
        self.assertEqual(response.status_code, 302)

        # Usuário tenta acessar register e
        # é redirecionado para o dashboard automaticamente
        self.browser.get(self.live_server_url + reverse('accounts:register'))
        self.assertEqual(response.status_code, 302)
