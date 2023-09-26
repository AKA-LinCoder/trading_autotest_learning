import pytest
from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    # 先实例化
    get_driver = DriverConfig().driver_config()
    # 通过yield返回到测试用例里
    yield get_driver
    # 测试用例执行完返回继续执行
    get_driver.quit()