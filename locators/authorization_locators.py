from selenium.webdriver.common.by import By

class TestLocatorsAuthorizationPage:
    # имя пользователя
    login = (By.ID, "Login")
    # пароль
    password = (By.ID, "Password")
    # кнопка Войти
    button_enter = (By.XPATH, ".//button[contains(@class, 'btn btn-default')]")
    # заголовок
    arm_cod = (By.XPATH, ".//a[contains(@href,'/portal/Home/Index')]")
    # сообщение "Введены неправильные имя пользователя или пароль"
    wrong_password = (By.XPATH, ".//span[contains(@class,'field-validation-error')]")