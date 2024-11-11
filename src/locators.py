from selenium.webdriver.common.by import By


class Locators:
    SITE_TAG = (By.XPATH, ".//h1[text() = '...']") #Чаты
    USER_CONT = (By.XPATH, ".//span[@title = 'aaa']/../../../..")
    USER_WEIT = (By.XPATH, ".//div[@role = 'button']/span[text() = 'aaa']")
    CONT_TEXT_FIELD = (By.XPATH, ".//div[@id = 'main']//p[contains(@class, 'selectable-text')]")
    BUTTON_SEND = (By.XPATH, ".//span[@data-icon = 'send']")
    DELYVERY_TAG = (By.XPATH, ".//span[@aria-label='...']") #' Доставлено '
    BUTTON_NEW_CHAT = (By.XPATH, ".//div[@title = '...']") #'Новый чат'