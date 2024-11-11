from pages.base_page import BasePage
from src.data import *
from src.locators import Locators


class SendMessege(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(url)

    def wait_for_site_load(self):
        return self.wait_for_element(Locators.SITE_TAG)

    def new_chat(self):
        self.click(Locators.BUTTON_NEW_CHAT)

    def enter_user(self):
        self.click(Locators.USER_CONT)

    def user_active(self):
        return self.wait_for_element(Locators.USER_WEIT)

    def check_text_container(self):
        self.click(Locators.CONT_TEXT_FIELD)

    def sand_text_1_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE1)

    def sand_massege(self):
        self.click(Locators.BUTTON_SEND)

    def wait_sending(self):
        return self.wait_for_element(Locators.DELYVERY_TAG)

    def sand_text_2_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE2)

    def sand_text_3_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE3)

    def sand_text_4_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE4)

    def sand_text_5_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE5)

    def sand_text_6_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE6)

    def sand_text_7_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE7)

    def sand_text_8_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE8)

    def sand_text_9_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE9)

    def sand_text_10_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE10)

    def sand_text_11_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND1_LINE11)

    def sand_text_12_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE1)

    def sand_text_13_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE2)

    def sand_text_14_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE3)

    def sand_text_15_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE4)

    def sand_text_16_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE5)

    def sand_text_17_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE6)

    def sand_text_18_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE7)

    def sand_text_19_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE8)

    def sand_text_20_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE9)

    def sand_text_21_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE10)

    def sand_text_22_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE11)

    def sand_text_23_text(self):
        self.send_keys(Locators.CONT_TEXT_FIELD, SAND2_LINE12)
