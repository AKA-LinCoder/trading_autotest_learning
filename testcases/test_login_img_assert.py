from time import sleep
from page.LoginPage import LoginPage
import pytest


class TestLoginAssert:
    @pytest.mark.login
    def test_login_assert(self, driver):
        """
        登陆后断言图片
        :param driver:
        :return:
        """
        LoginPage().login(driver, "jay")
        sleep(3)
        assert LoginPage().login_assert(driver, "head_img.png") > 0.9
