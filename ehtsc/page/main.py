from page.base_page import BasePage
from page.home import Homepage


class Main(BasePage):
    
    def quit(self):
        self._driver.quit()
        
    def goto_homepage(self):
        self.opera_steps('../data/main.yml')
        return Homepage(self._driver)
    
    