import pytest
from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    print("打开浏览器")
    # 先实例化
    get_driver = DriverConfig().driver_config()
    # 通过yield返回到测试用例里
    yield get_driver
    # 测试用例执行完返回继续执行
    get_driver.quit()
    print("关闭浏览器")