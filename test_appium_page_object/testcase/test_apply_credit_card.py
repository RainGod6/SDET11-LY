from test_appium_page_object.page.app import App


class TestApplyCreditCard:

    def setup(self):
        self.main = App().start().main()

    def test_apply_credit_card(self):
        self.main.goto_etc_home().apply_credit_card()