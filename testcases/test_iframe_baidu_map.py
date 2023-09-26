from page.LoginPage import LoginPage
from page.LeftMeunPage import LeftMenuPage
from page.IframeBaiduMapPage import IframeBaiduMapPage
from config.driver_config import DriverConfig
from time import sleep


class TestIframeBaiduMap:
    def test_iframe_baidu_map(self,driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, 'iframe测试')
        sleep(3)
        IframeBaiduMapPage().switch_to_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        IframeBaiduMapPage().iframe_out(driver)
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "首页")
        driver.quit()
