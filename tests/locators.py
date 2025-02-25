from selenium.webdriver.common.by import By


class Locators:

    reg_button = (By.LINK_TEXT, 'Зарегистрироваться') # кнопка "зарегистрироваться" в форме логин в форме регистрации

    login_reg = (By.XPATH,".//a[text()='Войти']") #кнопка  "Войти" в форме входа для зарегистрированных пользователей
    exit_button = (By.XPATH, ".//button[text()='Выход']") # кнопка выход из аккаунта

    switch_souses = (By.XPATH, ".//span[text()='Соусы']/parent::*") # кнопка конструктора "Соусы"

    ingredients = (By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']") # все ингридиенты в конструкторе. 0 - булки, 1- соусы, 2 - начинки

    current_scroll = (By.XPATH,".//*[contains(@class, 'current')]") #
    switch_bulki = (By.XPATH,".//span[text()='Булки']/parent::*" ) #
    switch_nachinki = (By.XPATH,".//span[text()='Начинки']/parent::*" ) #
    login_button = (By.XPATH, ".//button[text()='Войти']") #кнопка "войти"
    login_input = (By.TAG_NAME, "input") # форма заполнения страница логин
    homepage_buttons = (By.TAG_NAME, "button") # кнопки главной страницы
    lk_button = (By.LINK_TEXT, 'Личный Кабинет') # кнопка "Личный Кабинет"
    password_ap = (By.XPATH, ".//a[text()='Восстановить пароль']") #кнопка "Восстановить пароль"
    constructor = (By.LINK_TEXT, 'Конструктор')
    logo = (By.XPATH, "//div/a/*") # Логотип сайта на главной странице
    reg_input = (By.TAG_NAME, "input") # форма ввода регистрации
    reg_button_2 = (By.XPATH, ".//button[text()='Зарегистрироваться']")# кнопка "зарегистрироваться" в форме логин в форме регистрации
    error_message = (By.XPATH, ".//p[@class='input__error text_type_main-default']") # сообщение о некорректном пароле
