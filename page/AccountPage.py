from base.AccountBase import AccountBase
from base.ObjectMap import ObjectMap
from selenium.webdriver.common.by import By
from common.tools import get_img_path


class AccountPage(ObjectMap, AccountBase):
    def upload_avatar(self, driver, img_name):
        """
        上传个人头像
        :param driver:
        :param img_name:
        :return:
        """
        img_path = get_img_path(img_name)
        upload_xpath = self.basic_info_avatar_input()
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def click_save(self, driver):
        """
        个人资料保存点击
        :param driver:
        :return:
        """
        button_xpath = self.basic_info_save_button()
        return self.element_click(driver, By.XPATH, button_xpath)
