import time

import requests

from base.LoginBase import LoginBase
from selenium.webdriver.common.by import By
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf
from logs.log import log
from common.report_add_img import add_img_path_to_report
from common.ocr_identify import OcrIndentify


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        input_xpath = self.login_input(input_placeholder)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def click_login(self, driver, button_name):
        button_xpath = self.login_button(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)
        # return driver.find_element_by_xpath(input_xpath).click()

    def login(self, driver, user, need_captcha=False):
        self.element_to_url(driver, "/login")
        if need_captcha:
            time.sleep(3)
            log.info("need captche")
            self.select_need_captcha(driver)
            captcha_xpath = self.captcha()
            element_img_path = self.element_screenshot(driver, By.XPATH, captcha_xpath)
            add_img_path_to_report(element_img_path, "图像验证码")
            identify = OcrIndentify().identify(element_img_path)
            log.info("code is" + str(identify))
            input_captcha_xpath = self.input_captcha()
            self.element_fill_value(driver, By.XPATH, input_captcha_xpath, identify)
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.click_login(driver, "登录")
        self.assert_login_success(driver)

    def estim_login(self, driver):
        """
        钻井账号密码登录测试
        :param driver:
        :param user:
        :return:
        """
        self.element_to_url(driver, "/login")
        self.login_input_value(driver, "请输入账号", "admin")
        self.login_input_value(driver, "请输入密码", "123456")
        self.click_login(driver, "登录")
        self.assert_login_success(driver)

    def api_login(self, driver, user):
        """
        通过api登录
        :param driver:
        :param user:
        :return:
        """
        log.info("跳转登录页")
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        log.info("用户名" + username)
        url = GetConf().get_url()
        data = {
            "user": username,
            "password": password
        }
        log.info("通过api登录")
        res = requests.post(url + "/api/user/login", json=data)
        log.info("这是结果")
        log.info(res)
        token = res.json()["data"]["token"]
        js_script = "window.sessionStorage.setItem('token','%s');" % token
        log.info("将token写入session")
        driver.execute_script(js_script)
        time.sleep(2)
        log.info("跳转主页")
        self.element_to_url(driver, "/")

    def login_assert(self, driver, img_name):
        """
        登陆后判断头像
        :param driver:
        :param img_name:
        :return:
        """
        log.info("登录后判断头像")
        return self.find_img_in_source(driver, img_name)

    def assert_login_success(self, driver):
        """
        验证是否登录成功
        :param driver:
        :return:
        """
        success_xpath = self.login_success()
        self.element_appear(driver, By.XPATH, success_xpath, timeout=2)

    def select_need_captcha(self, driver):
        """
        点击勾选是否需要验证码
        :param driver:
        :return:
        """
        log.info("点击勾选是否需要验证码")
        select_xpath = self.need_captcha()
        return self.element_click(driver, By.XPATH, select_xpath)
