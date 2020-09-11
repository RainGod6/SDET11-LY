# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueQiu:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "test1"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["chromedriverExecutable"] = "/Users/user/tool/chromedriver/2.20/chromedriver"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MobileBy.ID, 'com.xueqiu.android:id/tv_agree')))
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_agree').click()
        self.driver.implicitly_wait(10)

    def test_webview_context(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易' and contains(@resource-id,'tab_name')]").click()
        # WebDriverWait(self.driver, 15).until(lambda x: len(self.driver.contexts) > 1)
        for i in range(5):
            print(self.driver.contexts)
            sleep(1)
        print(self.driver.page_source)
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.contexts)
        print(self.driver.page_source)



    def teardown(self):
        sleep(20)
        self.driver.quit()