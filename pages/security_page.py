from locators.security_locators import TestLocatorsSecurityPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class SecurityPage:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    # метод выбора Безопасность/Пользователи ЦОД
    def click_users_cod(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsSecurityPage.users_cod_button))
        element = self.driver.find_element(*TestLocatorsSecurityPage.users_cod_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        self.driver.find_element(*TestLocatorsSecurityPage.users_cod_button).click()

        # метод нажатия кнопки "Добавить пользователя ЦОД"
    def click_add_user_cod(self):
        self.driver.find_element(*TestLocatorsSecurityPage.button_add_user_cod).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsSecurityPage.header_add_user_cod))
        element = self.driver.find_element(*TestLocatorsSecurityPage.users_cod_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

