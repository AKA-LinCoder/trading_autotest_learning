import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMeunPage import LeftMenuPage
from page.GoodsPage import GoodsPage
from time import sleep

goods_info_list = [
    {
        "goods_title": "新增批量商品测试1",
        "goods_details": "新增批量商品测试详情1",
        "goods_num": 1,
        "goods_pic_list": ["商品图片一.jpg"],
        "goods_price": 100,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    },
    {
        "goods_title": "新增批量商品测试2",
        "goods_details": "新增批量商品测试详情2",
        "goods_num": 2,
        "goods_pic_list": ["商品图片一.jpg"],
        "goods_price": 200,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    }
]


class TestAddGoods:

    @pytest.mark.parametrize("goods_info", goods_info_list)
    def test_add_goods_001(self, driver, goods_info):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(driver,
                                  goods_title=goods_info["goods_title"],
                                  goods_detail=goods_info["goods_details"],
                                  goods_num=goods_info["goods_num"],
                                  goods_price=goods_info["goods_price"],
                                  good_img_list=goods_info["goods_pic_list"],
                                  goods_status=goods_info["goods_status"],
                                  button_name=goods_info["bottom_button_name"]
                                  )
        sleep(3)
