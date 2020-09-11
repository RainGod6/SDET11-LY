from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestApiDemo:

    def setup(self):
        caps = {}
        caps['platformName'] = "android"
        caps['deviceName'] = "小米5"
        caps['appPackage'] = "io.appium.android.apis"
        caps['appActivity'] = ".ApiDemos"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_toast(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Views' and contains(@resource-id,'text1')]").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("Popup Menu").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Make a Popup!').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        # toast定位，由于toast短暂最好用变量存下来
        toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        print(toast)
        assert 'Clicked' in toast
        assert 'popup menu' in toast
        assert 'API Demos：Clicked popup menu item Search' == toast

    def teardown(self):
        pass






