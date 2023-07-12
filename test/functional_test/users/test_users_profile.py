from .base import UsersBaseTest
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from django.urls import reverse
from time import sleep


class UserProfileTest(UsersBaseTest):
    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/div/div/div/form'
        )

    def test_dashboard_profile_return_correct_view(self):
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

        # Usuário abre a página de perfil
        self.browser.get(self.live_server_url + reverse('dashboard:profile'))

        # Vê o header da página
        self.assertIn('Profile Information',
                      self.browser.find_element(By.TAG_NAME, 'body').text)
