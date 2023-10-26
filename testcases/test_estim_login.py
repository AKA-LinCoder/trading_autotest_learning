from time import sleep

import allure
import pytest

from page.LoginPage import LoginPage
from common.report_add_img import add_img_to_report


class TestLogin:
    @pytest.mark.login
    @allure.feature("钻井信息管理系统登录")
    @allure.description("钻井信息管理系统登录")
    def test_login(self, driver):
        """账号密码登录"""
        with allure.step("登录"):
            LoginPage().estim_login(driver,)
            sleep(3)
            add_img_to_report(driver, "登录")