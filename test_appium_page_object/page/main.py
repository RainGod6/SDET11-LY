from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium_page_object.page.apply_etc_card.apply_credit_card import ApplyCreditCard
from test_appium_page_object.page.base_page import BasePage


class Main(BasePage):
    def goto_etc_home(self):
        self.find(MobileBy.XPATH, "//*[@text='ETC']").click()
        WebDriverWait(self._driver, 20).until(expected_conditions.element_to_be_clickable((MobileBy.ID,
                                                                                          "android:id/button1")))
        self.find(MobileBy.ID, "android:id/button1").click()
        return ApplyCreditCard(self._driver)

    def goto_etc_services_more(self):
        pass

    def goto_profile(self):
        pass

    def goto_message(self):
        pass
