from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import yaml
import pytest
from time import sleep


class BasePage:
    # 创建黑名单列表用于处理弹窗
    _black_list = []
    _error_count = 0
    _error_max = 5
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator):
        try:
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                             locator)
            self._error_count = 0  # 如果找到该元素那么错误次数为0
            return element
        except Exception as e:
            # 没有找到该元素的话，错误次数+1
            self._error_count += 1
            # 当错误次数大于最大次数时抛出异常
            if self._error_count >= self._error_max:
                raise e
            # 没有大于最大次数，去找黑名单里边的内容
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:  # 找到黑名单中的内容进行点击操作（关闭窗口）
                    elements[0].click()
                    return self.find(by, locator)
            raise e  # 没有找到就抛出异常

    # 定义一个方法用于输入框的输入
    def send(self, value, by, locator=None):
        try:
            self._driver.find(by, locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_element(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            raise e
        
    # 定义一个方法用于滑动触屏幕，从(x_start,y_start)坐标滑动到(x_end,y_end)
    # def slide(self, x_start, y_start, x_end, y_end):
    #     action = TouchAction(self._driver)
    #     action.press(x_start, y_start).wait(500).move_to(x_end, y_end).release().perform()
    #
    # 定义一个操作步骤的方法，用于数据驱动的方式进行执行案例
    def opera_steps(self, path):
        # 读取yml文件
        with open(path, 'r', encoding='utf-8') as f:
            steps: list[dict] = yaml.safe_load(f)
            # 遍历操作步骤
            for step in steps:
                if 'by' in step.keys():
                    element = self.find(step['by'], step['locator'])
                if 'action' in step.keys():
                    if 'click' == step['action']:
                        element.click()
                    if 'send' == step['action']:
                        content: str = step['value']
                        for param in self._params:
                            content = content.replace("{%s}" % param, self._params[param])
                        element.send(content, step['by'], step['locator'])
                    if 'TouchAction' in step['action']:
                        action = TouchAction(self._driver)
                        action.press(x=step['value'][0]['x_start'], y=step['value'][0]['y_start']).wait(300).move_to(
                            x=step['value'][1]['x_end'], y=step['value'][1]['y_end']).release().perform()
                # 数据驱动断言
                if 'assertion' in step.keys():
                    if "sleep" in step['assertion'].keys():
                        sleep(step['assertion']['sleep'])
                    element = self.find(step['assertion']['by'], step['assertion']['locator'])
                    attribute = element.get_attribute(step['assertion']['attribute'])
                    pytest.assume(attribute == step['assertion']['assert_info'])
                if 'back' in step.keys():
                    self._driver.back()
                    
                    
                        
                    
                    