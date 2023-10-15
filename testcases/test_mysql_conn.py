from time import sleep

import allure
from common.mysql_operate import MySqloperate
from page.HomePage import HomePage
from page.LoginPage import LoginPage
from logs.log import log


class TestMySqlConn:
    def test_mysql(self, driver):
        with allure.step("登录"):
            LoginPage().login(driver, "jay")
            sleep(3)

        with allure.step("获取账号余额"):
            balance = HomePage().get_balance(driver)
            log.info(balance)
        with allure.step("从mysql获取余额"):
            sql = "select balance from wallet where user_id = 13;"
            db_balance = MySqloperate().query(sql)[0][0]
            log.info(db_balance)
        with allure.step("断言数据库中的数据是否一致"):
            assert str(balance) == str(db_balance)
