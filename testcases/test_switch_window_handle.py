from time import sleep
from config.driver_config import DriverConfig
from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMeunPage import LeftMenuPage
from page.LoginPage import LoginPage
import allure
from common.report_add_img import add_img_to_report


class TestWindowHandle:
    @allure.description("测试外链")
    @allure.epic("测试外链epic ")
    @allure.feature("测试外链feature")
    @allure.story("测试外链story")
    @allure.tag("测试外链tag")
    def test_switch_window_handles(self,driver):
        with allure.step("登录"):
            LoginPage().login(driver, "jay")
            sleep(3)
            add_img_to_report(driver,"login")
        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(driver, "外链")
            sleep(2)
            add_img_to_report(driver,"tap url")
        with allure.step("断言"):
            title = ExternalLinkPage().goto_imooc(driver)
            print(title)

