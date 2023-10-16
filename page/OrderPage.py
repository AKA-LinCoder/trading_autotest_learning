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

    def click_order_operation(self,driver,product_title,operation):
        """
        点击订单的操作按钮
        :param driver:
        :param product_title:
        :param operation:
        :return:
        """
        button_xpath = self.order_operation(product_title,operation)
        return self.element_click(driver,By.XPATH,button_xpath)

    def click_order_operation_confirm(self,driver):
        """
        点击订单操作按钮后的弹窗的确定按钮
        :param driver:
        :return:
        """
        button_xpath = self.order_operation_confirm()
        return self.element_click(driver,By.XPATH,button_xpath)
