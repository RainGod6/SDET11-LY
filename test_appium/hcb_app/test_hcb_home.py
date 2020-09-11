from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestHcb:

    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = '28d6f388'
        caps['appPackage'] = 'com.wlqq'
        caps['appActivity'] = 'com.wlqq.activity.HomeActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        # 启动APP点击同意
        el1 = self.driver.find_element(MobileBy.ID, 'com.wlqq:id/dialog_btn_right')
        el1.click()
        self.driver.implicitly_wait(15)
        # 点击首页温馨提示
        el2 = self.driver.find_element(MobileBy.ID, 'com.wlqq:id/text_positive')
        el2.click()
        self.driver.implicitly_wait(20)  # 隐式等待：在设置超时时间范围内，一直寻找元素，若在时间内找到则立即执行后面操作，若时间内未找到则抛出异常
        # 点击NFC授权
        el3 = self.driver.find_element(MobileBy.ID, 'android:id/button1')
        el3.click()

    def test_etc_home(self):
        e2 = self.driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@text="ETC"]')
        e2.click()
        print(e2.get_attribute('text'))

        print("点击ETC服务完成，进入ETC插件首页")
        # print(self.driver.page_source)
        assert 'ETC' == e2.get_attribute('text')

    def test_hcb_home(self):
        el1 = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@text="ETC服务"]')
        el1.click()

    def teardown(self):
        sleep(20)  # 强制等待
        self.driver.quit()

