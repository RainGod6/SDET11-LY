from appium.webdriver.common.mobileby import MobileBy
from test_appium_page_object.page.base_page import BasePage


class ApplyCreditCard(BasePage):

    _name_apply_card_element = (MobileBy.ID, "com.wlqq.phantom.plugin.etc:id/tv_online_open_card")
    _name_nfc_element = (MobileBy.ID, "com.wlqq:id/btn_back")

    def apply_credit_card(self):
        self.find(self._name_apply_card_element).click()
        self.find(self._name_nfc_element).click()
        return self

    def goto_faq(self):
        pass

    def goto_bind_card(self):
        pass

    def goto_obu(self):
        pass
