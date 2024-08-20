from selenium.webdriver.common.by import By
class OrderPageLocators:

# Для "Кого самокат"
    name = (By.XPATH, "//input[@placeholder='* Имя']")
    lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    choice_metro = (By.XPATH, ".//li[@class='select-search__row']")
    phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, "//button[text()='Далее']")

# Про аренду

    date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    calendar = (By.XPATH, "//div[@class='react-datepicker-popper']")
    calendar_item = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    renta_term = (By.XPATH, ".//div[text()='* Срок аренды']")
    term_renta = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='шестеро суток']")
    color_scooter = (By.XPATH, "//input[@id='black']")
    commit = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    button_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

# про заказ
    button_confirm_order = (By.XPATH, "//button[text()='Да']")
    button_view_order = (By.XPATH, ".//*[text()='Посмотреть статус']")