from time import sleep
from config.driver_config import DriverConfig
import pytest


class TestPyTestMClass:

    @pytest.fixture(scope="class")
    def scope_class(self):
        print("我是class级别，我只执行一次")

    @pytest.fixture(scope="function")
    def driver(self):
        get_driver = DriverConfig().driver_config()
        return get_driver

    @pytest.mark.bing
    def test_open_bing(self, driver):
        # driver = DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self, driver):
        # driver = DriverConfig().driver_config()
        driver.get("https://www.baidu.com")
        sleep(3)
        driver.quit()

    @pytest.mark.google
    def test_open_google(self, driver):
        # driver = DriverConfig().driver_config()
        driver.get("https://www.google.com")
        sleep(3)
        driver.quit()
