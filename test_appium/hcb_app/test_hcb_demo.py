from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHcbDemo:

    def setup(self):
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
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((MobileBy.ID,
                                                                                         "android:id/button1")))
        self.driver.find_element(MobileBy.ID, "android:id/button1").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='知道了']").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,
        "//*[contains(@resource-id,'content')]\
        //*[@class ='android.widget.FrameLayout']//*[@class='android.widget.ImageView']")))
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'content')]\
        //*[@class ='android.widget.FrameLayout']//*[@class='android.widget.ImageView']").click()

    def test_etc_home(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='ETC']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='快速办卡']").click()

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='ETC']").click()
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((MobileBy.ID,
                                                                                          "android:id/button1")))
        self.driver.find_element(MobileBy.ID, "android:id/button1").click()
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((MobileBy.ID, 'com.wlqq.phantom.plugin.etc:id/tv_online_open_card')))
        self.driver.find_element(MobileBy.ID, "com.wlqq.phantom.plugin.etc:id/tv_online_open_card").click()
        print(self.driver.contexts)
        self.driver.find_element(MobileBy.ID, "com.wlqq:id/btn_back").click()
        # 打印当前页面结构page_source，当前xml结构
        # print(self.driver.page_source)
        # 等待上下文出现，webview出现
        WebDriverWait(self.driver, 20).until(lambda x: (len(self.driver.contexts) > 1))
        # 切换至webview容器
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 打印当前页面结构page_source，当前html结构
        print(self.driver.page_source)
        self.driver.find_element(By.CSS_SELECTOR, ".button-container.fixed-button").click()
        # webview中toast定位获取到div中的id属性
        toast = self.driver.find_element(By.CSS_SELECTOR, "#goblin-toast").text
        print(toast)
        assert "未选择车牌" in toast
        print(self.driver.contexts)
        # self.driver.switch_to.context(self.driver.contexts['NATIVE_APP'])
        self.driver.find_element(MobileBy.ID, "com.wlqq:id/back_btn").click()

    def teardown(self):
        pass
