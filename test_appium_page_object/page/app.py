from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_appium_page_object.page.base_page import BasePage
from test_appium_page_object.page.main import Main


class App(BasePage):
    _appPackage = "com.wlqq"
    _appActivity = ".activity.HomeActivity"

    def start(self):

        if self._driver is None:
            caps = {}
            caps['platformName'] = 'android'
            caps['deviceName'] = '28d6f388'
            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity
            caps["automationname"] = "uiautomator2"
            caps["chromedriverExecutable"] = "/Users/user/tool/chromedriver/2.35/chromedriver"
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)
            self.find(MobileBy.ID, "com.wlqq:id/dialog_btn_right").click()
            return self
        else:
            self._driver.start_activity(self._appPackage, self._appActivity)

    def restart(self):
        pass

    def stop(self):
        pass

    # 类型提示 ->
    def main(self) -> Main:
        # todo: wait main page
        WebDriverWait(self._driver, 30).until(expected_conditions.element_to_be_clickable((MobileBy.ID,
                                                                                          "android:id/button1")))
        self.find(MobileBy.ID, "android:id/button1").click()
        self.find(MobileBy.XPATH, "//*[@text='知道了']").click()
        WebDriverWait(self._driver, 30).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,
                                                                                          "//*[contains(@resource-id,'content')]\
                                                                                          //*[@class ='android.widget.FrameLayout']//*[@class='android.widget.ImageView']")))
        self.find(MobileBy.XPATH, "//*[contains(@resource-id,'content')]\
                        //*[@class ='android.widget.FrameLayout']//*[@class='android.widget.ImageView']").click()
        # WebDriverWait(self._driver, 30).until(lambda x: "ETC" in self._driver.page_source)  # 等待首页元素出现完成加载
        return Main(self._driver)