import pytest
import allure
from time import sleep
from page.LoginPage import LoginPage

class TestLoginByApi:
    @pytest.mark.login
    @allure.feature("api登录")
    def test_login_by_api(self,driver):
        """api登录"""
        with allure.step("登录jay"):
            LoginPage().api_login(driver,"jay")
            sleep(5)

        with allure.step("切换用户到william"):
            LoginPage().api_login(driver,"william")
            sleep(5)