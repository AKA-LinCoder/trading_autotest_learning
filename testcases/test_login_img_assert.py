from time import sleep
from page.LoginPage import LoginPage
import pytest
import allure
from common.report_add_img import add_img_to_report


class TestLoginAssert:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录后断言图片")
    def test_login_assert(self, driver):
        """
        登陆后断言图片
        :param driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().login(driver, "jay")
            sleep(3)
            add_img_to_report(driver,"登录")
        with allure.step("断言图片"):
            assert LoginPage().login_assert(driver, "head_img.png") > 0.9
