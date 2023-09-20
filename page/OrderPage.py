from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase
from selenium.webdriver.common.by import By

class OrderPage(ObjectMap,OrderBase):
    def click_order_tab(self,driver,tab_name):
        """
        点击订单tab按钮
        :param driver:
        :param tab_name:
        :return:
        """
        tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver,By.XPATH,tab_xpath)