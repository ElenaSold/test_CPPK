from pages.authorization_page import AuthorizationPage
from locators.authorization_locators import TestLocatorsAuthorizationPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class TestAuthorization:
    @allure.title('ЦОД: успешная авторизация')
    @allure.step('Перешли на страницу авторизации')
    @allure.step('Авторизовались с корректными кредами')
    @allure.step('Проверили переход на страницу с Меню')
    def test_successful_authorization(self, driver):

        # перешли на страницу авторизации
        driver.get('https://cppk2.srvdev.ru/portal/Home/Index')

        # создали объект класса страницы авторизации
        authorization_page = AuthorizationPage(driver)

        # авторизовались
        authorization_page.authorization('esoldatenkova', '1234Test')

        # дождались загрузки страницы
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(TestLocatorsAuthorizationPage.arm_cod))

        # проверили переход на страницу с Меню
        assert driver.current_url == 'https://cppk2.srvdev.ru/portal/Home/Index'

    @allure.title('ЦОД: успешная авторизация')
    @allure.step('Перешли на страницу авторизации')
    @allure.step('Авторизовались с несуществующими кредами')
    @allure.step('Проверили отображение ошибки на странице авторизации')
    def test_unsuccessful_authorization(self, driver):

        # перешли на страницу авторизации
        driver.get('https://cppk2.srvdev.ru/portal/Home/Index')

        # создали объект класса страницы авторизации
        authorization_page = AuthorizationPage(driver)

        # авторизовались
        authorization_page.authorization('esoldatenkova', '1234')

        # проверили отображение ошибки на странице авторизации
        assert driver.find_element(*TestLocatorsAuthorizationPage.wrong_password).text == "Введены неправильные имя пользователя или пароль"