from locators.authorization_locators import TestLocatorsAuthorizationPage

class AuthorizationPage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    # метод заполняет Имя пользователя
    def fill_login(self, login):
                self.driver.find_element(*TestLocatorsAuthorizationPage.login).send_keys(login)

    # метод заполняет пароль
    def fill_password(self,password):
        self.driver.find_element(*TestLocatorsAuthorizationPage.password).send_keys(password)

    # метод кликает по кнопке Войти
    def click_enter(self):
        self.driver.find_element(*TestLocatorsAuthorizationPage.button_enter).click()

    # метод с авторизацией
    def authorization(self, login, password):
        # заполнили поле Имя пользователя
        self.fill_login(login)

        # заполнили поле Пароль
        self.fill_password(password)

        # нажали "Войти"
        self.click_enter()
