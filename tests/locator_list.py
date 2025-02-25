lk_button = .// p[text() = 'Личный Кабинет'] # кнопка "Личный кабинет"
#.// a[text() = 'Зарегистрироваться'] # кнопка "зарегистрироваться" на странице "Вход"
#.//button[text()='Войти в аккаунт']    .//button[0]   #  кнопка "Войти в аккаунт"

reg_button = driver.find_element(By.LINK_TEXT, 'Зарегистрироваться') # кнопка "зарегистрироваться" в форме логин в форме регистрации
#.//input #поля ввода в форме регистрации "имя", "почта", "пароль"
login_reg = driver.find_element(By.XPATH,".//a[text()='Войти']") #кнопка  "Войти" в форме входа для зарегистрированных пользователей
exit_button = driver.find_element(By.XPATH, ".//button[text()='Выход']") # кнопка выход из аккаунта
#.//p[@class='input__error text_type_main-default'] #сообщение о некорректном пароле
#.//button[0] # Кнопка входа в аккаунт на главной странице
#.//a[(@href='https://stellarburgers.nomoreparties.site/forgot-password') or (text()='Восстановить пароль')] #кнопка "Восстановить пароль"
#.//a[(@href='https://stellarburgers.nomoreparties.site/login') or text()='Войти']#кнопка"войти" на страницке восстановления пароля
#.//p[(contains(@class, 'AppHeader_header')) or (text()='Конструктор')] #иконка и подпись "конструктор"
#.//svg
#//div/a/* #логотип Stellar Burgers
#.//img[contains(@alt, 'булка')] # список изображений булок
switch_souses = driver.find_element(By.XPATH, ".//span[text()='Соусы']/parent::*") # кнопка конструктора "Соусы"
#.//img[contains(@alt, 'Соус')] #  соусы в конструкторе
#.//span[text()='Булки']/parent::* # кнопка конструктора "Булки"
#.//span[text()='Начинки']/parent::* #кнопка конструктора "Начинки"
ingredients = driver.find_elements(By.XPATH, ".//ul[@class='BurgerIngredients_ingredients__list__2A-mT']") # все ингридиенты в конструкторе. 0 - булки, 1- соусы, 2 - начинки
elements_souses = ingredients[1] # список соусов
current_scroll = driver.find_elements(By.XPATH,".//*[contains(@class, 'current')]") #
switch_bulki = driver.find_elements(By.XPATH,".//span[text()='Булки']/parent::*" ) #
switch_nachinki = driver.find_elements(By.XPATH,".//span[text()='Начинки']/parent::*" ) #
login_button = driver.find_element(By.XPATH, ".//button[text()='Войти']") #кнопка "войти"
login_input = driver.find_elements(By.TAG_NAME, "input") # форма заполнения страница логин
homepage_buttons = driver.find_elements(By.TAG_NAME, "button") # кнопки главной страницы
lk_button = driver.find_element(By.LINK_TEXT, 'Личный Кабинет') # кнопка "Личный Кабинет"
password_ap = driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']") #кнопка "Восстановить пароль"
constructor = driver.find_element(By.LINK_TEXT, 'Конструктор')
logo = driver.find_element(By.XPATH, "//div/a/*") # Логотип сайта на главной странице
reg_input = driver.find_elements(By.TAG_NAME, "input")
reg_button_2 = driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']")# кнопка "зарегистрироваться" в форме логин в форме регистрации
error_message = driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']")