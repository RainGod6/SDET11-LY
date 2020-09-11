# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestYmmAPP:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "xiaomi5"
        caps["appPackage"] = "com.xiwei.logistics"
        caps["appActivity"] = "com.xiwei.logistics.carrier.ui.CarrierMainActivity"
        # caps["noReset"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)  # 全局隐式等待
        # 同意协议
        self.driver.find_element_by_id("com.xiwei.logistics:id/dialog_btn_right").click()
        # 加入显示等待机制，因为此处页面元素呈现较慢,需要等待20s
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((MobileBy.ID, "android:id/button1")))
        # 同意NFC授权
        self.driver.find_element(MobileBy.ID, "android:id/button1").click()
        # 点击知道了弹框
        self.driver.find_element(MobileBy.ID, "com.xiwei.logistics:id/buttons_layout").click()
        # 关闭广告弹窗x按钮
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((MobileBy.ID, "com.xiwei.logistics:id/iv_close")))
        self.driver.find_element(MobileBy.ID, "com.xiwei.logistics:id/iv_close").click()

    def test_etchome(self):
        # page_source方法返回页面xml结构
        # print(self.driver.page_source)
        tab = "// *[@text='服务']/../../.."  # 父节点
        tab1 = "//*[contains(@resource-id,'ll_tab_container')]"  # 模糊匹配：使用contains
        tab2 = "//*[contains(@resource-id,'tv_tab') and @text='服务']"  # 使用多表达式组合 and
        # 点击服务，进入满帮服务首页
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'tv_tab') and @text='服务']").click()
        # 滑动屏幕
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        print(window_rect)
        width = window_rect['width']
        height = window_rect['height']
        for i in range(3):
            action.press(x=width * 1 / 2, y=height * 5 / 6).wait(2000).move_to(x=width * 1 / 2,

                                                                       y=height * 1 / 6).release().perform()
        # 再滑动回至原位置
        for i in range(3):
            action.press(x=width * 1 / 2, y=height * 1 / 6).wait(2000).move_to(x=width * 1 / 2,
                                                                               y=height * 5 / 6).release().perform()

        etc_tab = "//*[@text='ETC']"
        self.driver.find_element(MobileBy.XPATH, etc_tab).click()
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable((MobileBy.ID, "android:id/button1")))
        # 点击NFC授权
        self.driver.find_element(MobileBy.ID, "android:id/button1").click()
        quick_appaly_image = "//*[contains(@resource-id,'ll_online_open_card')]"
        assert not (self.driver.find_element(MobileBy.XPATH, quick_appaly_image).get_attribute(
            "resourceId")) != "com.wlqq.phantom.plugin.etc:id/ll_online_open_card"

    def test_apply_card(self):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'tv_tab') and @text='服务']").click()
        etc_tab = "//*[@text='ETC']"
        self.driver.find_element(MobileBy.XPATH, etc_tab).click()
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable((MobileBy.ID, "android:id/button1")))
        # 点击NFC授权
        self.driver.find_element(MobileBy.ID, "android:id/button1").click()
        quick_appaly_image = "//*[contains(@resource-id,'ll_online_open_card')]"
        assert (self.driver.find_element(MobileBy.XPATH, quick_appaly_image).get_attribute(
            "resourceId")) == "com.wlqq.phantom.plugin.etc:id/ll_online_open_card"
        # 点击快速开卡
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable((MobileBy.XPATH, "//*[@text='快速开卡']")))
        self.driver.find_element(MobileBy.XPATH, "//*[@text='快速开卡']").click()
        # 点击返回
        self.driver.find_element(MobileBy.ID, 'com.xiwei.logistics:id/btn_back').click()
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        print(self.driver.contexts)


    def test_ui_selector(self):
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'tv_tab') and @text='服务']").click()
        # 利用ui_selector滑动查找元素进行定位
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("去卖车").'
                                                        'instance(0));').click()

        # 加入显示等待,新调转的页面是webview，后面需要修改断言代码
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MobileBy.ID,
                                                        "com.xiwei.logistics:id/tv_title"))
        assert self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'tv_title')]").\
            get_attribute('text') == '我要卖车'

    def test_etc_services(self):
        etc_service_more = "//*[@text='ETC服务']//*[@text='查看更多']"
        etc_service_apply_credit_card = "//*[@text='ETC服务']//*[contains(@text,'全国记账卡')]//*[@text='去办卡']"
        etc_service_apply_stored_card = "//*[@text='ETC服务']//*[contains(@text,'全国储值卡')]//*[@text='去办卡']"

    def test_etc_apply_card(self):
        quick_apply = "//*[contains(@resource-id,'pager_banner')][1]"
        apply_card_tab = " "

    def teardown(self):
        # self.driver.quit()
        pass


















