from base.LoginBase import LoginBase
from selenium.webdriver.common.by import By
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        input_xpath = self.login_input(input_placeholder)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def click_login(self, driver, button_name):
        button_xpath = self.login_button(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)
        # return driver.find_element_by_xpath(input_xpath).click()

    def login(self, driver, user):
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.click_login(driver, "登录")

    def login_assert(self, driver, img_name):
        """
        登陆后判断头像
        :param driver:
        :param img_name:
        :return:
        """
        # log.info("登录后判断头像")
        return self.find_img_in_source(driver, img_name)
