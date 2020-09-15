from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium_page_object.page.main import Main


class App:

    def start(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = '28d6f388'
        caps["appPackage"] = "com.wlqq"
        caps["appActivity"] = ".activity.HomeActivity"
        caps["automationname"] = "uiautomator2"
        caps["chromedriverExecutable"] = "/Users/user/tool/chromedriver/2.35/chromedriver"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        self.driver.find_element(MobileBy.ID, "com.wlqq:id/dialog_btn_right").click()
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    # 类型提示 ->
    def main(self) -> Main:
        # todo: wait main page
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((MobileBy.ID,
                                                                                          "android:id/button1")))
        self.driver.find_element(MobileBy.ID, "android:id/button1").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='知道了']").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,
                                                                                          "//*[contains(@resource-id,'content')]\
                                                                                          //*[@class ='android.widget.FrameLayout']//*[@class='android.widget.ImageView']")))
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'content')]\
                        //*[@class ='android.widget.FrameLayout']//*[@class='android.widget.ImageView']").click()
        return Main(self.driver)