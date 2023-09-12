from config.driver_config import DriverConfig
from time import sleep

driver = DriverConfig().driver_config()
# driver.get(url="http://www.okoknxx.cn")
driver.get(url="http://139.159.221.240" )
sleep(2)
driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("周杰伦")
sleep(2)
driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys("123456")
sleep(2)
driver.find_element_by_xpath("//span[text()='登录']/parent::button").click()
sleep(2)
driver.quit()
