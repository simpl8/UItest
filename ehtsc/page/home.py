from page.base_page import BasePage
from time import sleep
import pytest


class Homepage(BasePage):
    
    # 进入客服，返回
    def customer_service(self):
        self.opera_steps("../data/homepage/home_service.yml")
        
    # 广告轮播
    def banner_slide(self):
        for i in range(4):
            self.opera_steps("../data/homepage/home_banner_slide.yml")
    
    # 进入广告
    def banner_click(self):
        self.opera_steps("../data/homepage/home_banner_click.yml")
    
    # 进入首页蓝底，点赞
    def blue_info_like(self):
        self.opera_steps("../data/homepage/blue_info_like.yml")

    # 切换要闻tab
    def tab_yaowen(self):
        self.opera_steps("../data/homepage/home_yaowen.yml")
    
    # 切换转类tab
    def tab_zhuanlan(self):
        self.opera_steps("../data/homepage/home_zhuanlan.yml")
    