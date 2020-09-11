# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "xiaomi5"
caps["appPackage"] = "com.xiwei.logistics"
caps["appActivity"] = "com.xiwei.logistics.carrier.ui.CarrierMainActivity"
# caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 同意协议
el1 = driver.find_element_by_id("com.xiwei.logistics:id/dialog_btn_right")
el1.click()

# 同意NFC授权，需要等待20s
driver.implicitly_wait(25)
el2 = driver.find_element(MobileBy.ID, "android:id/button1")
el2.click()

# 点击知道了弹框
el3 = driver.find_element(MobileBy.ID, "com.xiwei.logistics:id/buttons_layout")
# el3 = driver.find_element(MobileBy.XPATH, "//*[@text='知道了' and contains(@resource-id,'com.xiwei.logistics:id/buttons_layout')]")
el3.click()

# 关闭广告弹窗x按钮
driver.implicitly_wait(15)
el4 = driver.find_element(MobileBy.ID, "com.xiwei.logistics:id/iv_close")
el4.click()


