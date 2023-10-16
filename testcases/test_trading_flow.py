
from time import sleep
import pytest
import allure
from page.LoginPage import LoginPage
from page.LeftMeunPage import LeftMenuPage
from page.GoodsPage import GoodsPage
from common.tools import get_now_date_time_str
from common.report_add_img import add_img_to_report
from page.TradingMarketPage import TradingMarketPage
from page.OrderPage import OrderPage

class TestTradingFlow:
    @pytest.mark.trading_flow
    @allure.feature("交易流")
    def test_trading_flow(self,driver):
        """交易流"""
        with allure.step("登录卖家"):
            LoginPage().api_login(driver,"jay")
            add_img_to_report(driver,"登录卖家")
        with allure.step("进入新增二手商品页面"):
            LeftMenuPage().click_level_one_menu(driver,"产品")
            sleep(1)
            LeftMenuPage().click_level_two_menu(driver,"新增二手商品")
            sleep(1)
            add_img_to_report(driver,"进入新增二手商品")
        with allure.step("卖家发布商品"):
            good_title = "交易流测试"+get_now_date_time_str()
            GoodsPage().add_new_goods(driver,
                                      button_name="提交",
                                      goods_title=good_title,
                                      goods_detail="交易流测试",
                                      goods_num=1,
                                      goods_price=250,
                                      goods_status="上架",
                                      good_img_list=["商品图片一.jpg"],

                                      )
            add_img_to_report(driver,"新增商品")
            sleep(8)
        with allure.step("登录买家"):
            LoginPage().api_login(driver,"william")
            add_img_to_report(driver,"登录买家")
        with allure.step("进入交易市场"):
            LeftMenuPage().click_level_one_menu(driver,"交易市场")
            add_img_to_report(driver,"进入交易市场")
        with allure.step("搜索宝贝"):
            TradingMarketPage().input_search_input(driver,good_title)
            TradingMarketPage().click_search(driver)
            add_img_to_report(driver,"搜索宝贝")
        with allure.step("点击商品卡片"):
            TradingMarketPage().click_product_card(driver,good_title)
            sleep(1)
            add_img_to_report(driver,"点击商品卡片")
        with allure.step("点击我想要"):
            TradingMarketPage().click_i_want(driver)
            sleep(1)
            add_img_to_report(driver,"点击我想要")
        with allure.step("选择收获地址"):
            TradingMarketPage().click_address(driver)
            sleep(1)
            TradingMarketPage().select_detail_address(driver,1)
            sleep(1)
            add_img_to_report(driver,"选择收获地址")
        with allure.step("点击确定"):
            TradingMarketPage().click_bottom_button(driver)
            sleep(1)
            add_img_to_report(driver,"点击确定")

        with allure.step("买家支付"):
            OrderPage().click_order_operation(driver,good_title,"去支付")
            sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_to_report(driver,"买家支付")



