import pytest

from config.driver_config import DriverConfig
from time import sleep
from page.LoginPage import LoginPage
from page.LeftMeunPage import LeftMenuPage
from page.OrderPage import OrderPage

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]


class TestOrderBuy:
    @pytest.mark.parametrize("tab", tab_list)
    def test_order_buy(self, driver, tab):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(2)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(2)
        OrderPage().click_order_tab(driver, tab)
        sleep(3)

