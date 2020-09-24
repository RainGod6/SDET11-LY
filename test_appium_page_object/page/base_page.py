from appium.webdriver.webdriver import WebDriver
import logging


class BasePage:
    logging.basicConfig(level=logging.INFO)  # 使用logging
    _driver: WebDriver
    _black_list = []
    _error_max = 5
    _error_count = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # todo：当有广告、各种异常弹框出现的时候，要进行异常处理，通常用装饰器进行异常处理
    def find(self, locator, value: str = None):
        logging.info(locator, value)
        try:
            # 寻找控件
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            # 如果成功，清空错误计数
            self._error_count = 0
            return element
            # todo:self._error_max = 0
        except Exception as e:
            # 如果次数太多，就退出异常处理，直接报错
            if self._error_count > self._error_max:
                raise e
            # 记录一直异常的次数
            self._error_max += 1
            # 对黑名单弹框进行处理
            for element in self._black_list:
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续寻找原来正常的控件，使用递归
                    return self.find(locator, value)
            # 如果黑名单也没找到，就报错
            logging.warn("black list no found")
            raise e
