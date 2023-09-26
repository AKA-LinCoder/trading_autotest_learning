import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMeunPage import LeftMenuPage
from page.GoodsPage import GoodsPage
from time import sleep


class TestAddGoods:

    def test_add_goods_001(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(driver,
                                  goods_title="新增商品测试2012",
                                  goods_detail="测试详情",
                                  goods_num=5,
                                  goods_price=23,
                                  good_img_list=["商品图片一.jpg"],
                                  goods_status="上架",
                                  button_name="提交"
                                  )
        sleep(3)
        driver.quit()
