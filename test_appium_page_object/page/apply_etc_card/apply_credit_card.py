from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class ApplyCreditCard:
    _driver: WebDriver

    def __init__(self, driver):
        self._driver = driver

    def apply_cedit_card(self):
        self._driver.find_element(MobileBy.ID, "com.wlqq.phantom.plugin.etc:id/tv_online_open_card").click()
        self._driver.find_element(MobileBy.ID, "com.wlqq:id/btn_back").click()
        return self

    def goto_faq(self):
        pass

    def goto_bind_card(self):
        pass

    def goto_obu(self):
        pass
