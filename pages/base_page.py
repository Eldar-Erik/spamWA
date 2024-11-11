from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, keys):
        self.wait_for_element(locator).send_keys(keys)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def is_element_visible(self, locator):
        return self.wait_for_element(locator).is_displayed()

    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def scroll_down(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    def action_chain(self, obj_locator, target_locator):
        obj_element = self.driver.find_element(*obj_locator)
        target_element = self.driver.find_element(*target_locator)
        ActionChains(self.driver).drag_and_drop(obj_element, target_element).perform()
