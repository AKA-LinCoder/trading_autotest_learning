# from common.tools import
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMeunPage import LeftMenuPage
from time import sleep
from page.AccountPage import AccountPage


class TestPersonalInfo:
    def test_upload_avatar(self,driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, "账户设置")
        sleep(2)
        LeftMenuPage().click_level_two_menu(driver, "个人资料")
        sleep(2)
        AccountPage().upload_avatar(driver, "个人头像二.jpg")
        sleep(3)
        AccountPage().click_save(driver)
        sleep(3)
        driver.quit()
