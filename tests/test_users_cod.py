from locators.security_locators import TestLocatorsSecurityPage
from pages.authorization_page import AuthorizationPage
from pages.security_page import SecurityPage
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestUsersCodPage:
    @allure.title('ЦОД: переход на страницу "Безопасность/Пользователи ЦОД"')
    @allure.step('Перешли на страницу авторизации')
    @allure.step('Авторизовались')
    @allure.step('Нажали на "Безопасность/Пользователи ЦОД"')
    @allure.step('Проверили переход на страницу "Пользователи ЦОД"')
    def test_successful_open_page_users_cod(self, driver):

        #Перешли на страницу авторизации
        driver.get('https://cppk2.srvdev.ru/portal/Home/Index')

        # создали объект класса страницы авторизации
        authorization_page = AuthorizationPage(driver)

        #Авторизовались
        authorization_page.authorization('esoldatenkova', '1234Test')

        # создали объект класса страницы Безопасность
        security_page = SecurityPage(driver)

        #Нажали на "Безопасность/Пользователи ЦОД"
        security_page.click_users_cod()

        # Дождались загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsSecurityPage.users_cod_header))

        #Проверили переход на страницу "Пользователи ЦОД"
        assert driver.current_url == 'https://cppk2.srvdev.ru/portal/Security/Users/Index'

    @allure.title('ЦОД: проверка отображения страницы "Безопасность/Пользователи ЦОД"')
    @allure.step('Перешли на страницу авторизации')
    @allure.step('Авторизовались')
    @allure.step('Нажали на "Безопасность/Пользователи ЦОД"')
    @allure.step('Проверили корректность названия полей в таблице')
    def test_successful_display_page_users_cod(self, driver):
        #Перешли на страницу авторизации
        driver.get('https://cppk2.srvdev.ru/portal/Home/Index')

        # создали объект класса страницы авторизации
        authorization_page = AuthorizationPage(driver)

        # авторизовались
        authorization_page.authorization('esoldatenkova', '1234Test')

        # создали объект класса страницы Безопасность
        security_page = SecurityPage(driver)

        # нажали на "Безопасность/Пользователи ЦОД"
        security_page.click_users_cod()

        # Дождались загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsSecurityPage.users_cod_header))

        # проверили корректность названия полей в таблице
        assert driver.find_element(*TestLocatorsSecurityPage.users_roles).text == 'Пользователи/Роли' and \
               driver.find_element(*TestLocatorsSecurityPage.main_agent).text == 'Основной контрагент' and driver.find_element(*TestLocatorsSecurityPage.delegated_rights).text == 'Делегированные права'

    @allure.title('ЦОД: проверка открытия окна "Добавление пользователя ЦОД"')
    @allure.step('Перешли на страницу авторизации')
    @allure.step('Авторизовались')
    @allure.step('Нажали на "Безопасность/Пользователи ЦОД"')
    @allure.step('Нажали на "Добавить пользователя ЦОД"')
    @allure.step('Проверили название окна')
    def test_open_window_add_user_cod(self, driver):
        #Перешли на страницу авторизации
        driver.get('https://cppk2.srvdev.ru/portal/Home/Index')

        # создали объект класса страницы авторизации
        authorization_page = AuthorizationPage(driver)

        # авторизовались
        authorization_page.authorization('esoldatenkova', '1234Test')

        # создали объект класса страницы Безопасность
        security_page = SecurityPage(driver)

        # нажали на "Безопасность/Пользователи ЦОД"
        security_page.click_users_cod()

        # Дождались загрузки страницы
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocatorsSecurityPage.users_cod_header))

        # Нажали кнопку "Добавить пользователя"
        security_page.click_add_user_cod()

        # Проверили, что открылось окно с названием "Добавление пользователя ЦОД"
        assert driver.find_element(*TestLocatorsSecurityPage.header_add_user_cod).text == 'Добавление пользователя ЦОД'








