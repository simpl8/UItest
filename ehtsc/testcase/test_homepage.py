from page.app import App
import pytest
from appium import webdriver
from page.home import Homepage

class TestHome:
    
    def setup_class(self):
        self.testDriver = App().start().main()

    def teardown_class(self):
        self.testDriver.quit()
    @pytest.mark.skip
    def test_service(self):
        self.testDriver.goto_homepage().customer_service()
    
    def test_banner_slide(self):
        self.testDriver.goto_homepage().banner_slide()
    
    def test_banner_click(self):
        self.testDriver.goto_homepage().banner_click()
        
    def test_blue_info_click(self):
        self.testDriver.goto_homepage().blue_info_like()
    
    def test_tab_yaowen(self):
        self.testDriver.goto_homepage().tab_yaowen()
    def test_tab_zhuanlan(self):
        self.testDriver.goto_homepage().tab_zhuanlan()
        
    
    
    
    
        
        