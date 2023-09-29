import pytest
import allure
from time import sleep

from common.report_add_img import add_img_to_report
from page.LoginPage import LoginPage

class TestCaptchaLogin:
    @pytest.mark.login
    @allure.feature("login")
    @allure.description("验证码登陆")
    def test_captcha_login(self,driver):
        """验证码登陆"""
        with allure.step("login"):
            LoginPage().login(driver,"jay",need_captcha=True)
            sleep(3)
            add_img_to_report(driver,"login")