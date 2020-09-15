from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium_page_object.page.apply_etc_card.apply_credit_card import ApplyCreditCard


class Main:
    _driver: WebDriver

    def __init__(self, driver):
        self._driver = driver

    def goto_etc_home(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='ETC']").click()
        WebDriverWait(self._driver, 20).until(expected_conditions.element_to_be_clickable((MobileBy.ID,
                                                                                          "android:id/button1")))
        self._driver.find_element(MobileBy.ID, "android:id/button1").click()
        return ApplyCreditCard(self._driver)

    def goto_etc_services_more(self):
        pass

    def goto_profile(self):
        pass

    def goto_message(self):
        pass
