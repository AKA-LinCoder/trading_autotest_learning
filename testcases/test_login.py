# from config.driver_config import DriverConfig
# from time import sleep
#
# driver = DriverConfig().driver_config()
# # driver.get(url="http://www.okoknxx.cn")
# driver.get(url="http://139.159.221.240" )
# sleep(2)
# driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
# sleep(2)
# driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("123456")
# sleep(2)
# driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
# sleep(2)
# driver.quit()

# from  selenium import  webdriver
# from common.tools import get_project_path,sep
# options = webdriver.ChromeOptions()
# # 设置窗口大小
# options.add_argument("window-size=1920,1080")
# # 去掉浏览器显示的正在被控制文本
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# # 解决selenium无法访问https的问题
# options.add_argument("--ignore-certificate-errors")
# # 允许忽略localhost的TLS/SSL错误
# options.add_argument("--allow-insecure-localhost")
# # 设置为无痕模式
# options.add_argument("--incognito")
# # 设置无头模式(不打开浏览器也能执行)
# # options.add_argument("--headless")
# # 解决卡顿
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# driver = webdriver.Chrome(
#     options=options,
#     executable_path=get_project_path()+sep(["driver_files","chromedriver"],add_sep_before=True)
# )
#
# driver.get("https://www.baidu.com")
from time import sleep
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage


# 必须在setting中找到 Python Integrated Tool 中 的 Default test runner 选择为pytest,否则不会按照测试用例执行
# pyChame很智能，如果class里面有两个用例,鼠标右键时在哪个用例就执行哪个用例，放外面就会都执行
class TestLogin:
    def test_login(self,driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")

        # # driver.get(url="http://www.okoknxx.cn")
        # driver.get(url="http://139.159.221.240")
        # sleep(3)
        # LoginPage().login_input_value(driver, "用户名", "周杰伦")
        # sleep(3)
        # LoginPage().login_input_value(driver, "密码", "123456")
        # sleep(3)
        # LoginPage().click_login(driver, "登录")
        sleep(3)
        driver.quit()
