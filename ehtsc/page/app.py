from appium import webdriver
from page.base_page import BasePage
from page.main import Main


class App(BasePage):

    # 启动app
    def start(self,):
        _package = "com.android.haitong"  # 包名e海通财
        _activity = "cn.htsec.SecurityHome"  # activity
        if self._driver is None: # 如果是首次启动
            desir_cap = {
                "appPackage": _package,
                "appActivity": _activity,
                "platformName": "Android",
                "platformVersion": "6.0",
                "dontStopAppOnReset": "True",
                "noReset": "True",
                "deviceName": "127.0.0.1:7555"  # 如果用MuMu模拟器，则需要adb connect 127.0.0.1:7555
            }
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desir_cap)
            self._driver.implicitly_wait(5)  # 隐式等待
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)