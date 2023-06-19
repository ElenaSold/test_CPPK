from selenium.webdriver.common.by import By

class TestLocatorsSecurityPage:
    # пользователи ЦОД
    users_cod_button = (By.LINK_TEXT, "Пользователи ЦОД")

    # заголовок страницы "Пользователи ЦОД"
    users_cod_header = (By.XPATH, ".//div[@class = 'title-container']/h2")

    # столбец "Пользователи/Роли"
    users_roles = (By.XPATH, ".//span[contains(@data-bind, 'click: sort.bind')]")

    # столбец "Основной контрагент"
    main_agent = (By.XPATH, ".//th[contains(@data-bind, 'AgentId')]/div[contains(@style, 'display: inline-block;')]")

    # столбец "Делегированные права"
    delegated_rights = (By.XPATH, ".//th[contains(@style, 'width: 10%; position: relative;')]")

    # кнопка "Добавить пользователя" на странице пользователи ЦОД
    button_add_user_cod = (By.XPATH, ".//button[text()='Добавить пользователя']")

    # составной локатор модальных окон на странице "Пользователи ЦОД"
    #headers_user_modal = (By.XPATH, ".//div/div/div[@class = 'modal-header']/h4")

    # заголовок окна "Добавление пользователя ЦОД"
    header_add_user_cod = (By.XPATH, ".//div[@id = 'addUserModal']/div/div/div[@class = 'modal-header']/h4")

