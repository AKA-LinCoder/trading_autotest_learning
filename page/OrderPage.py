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

    def click_delivery_logistics(self,dirver):
        """
        点击物流
        :param dirver:
        :return:
        """
        input_xpath = self.delivery_logistics()
        return self.element_click(dirver,By.XPATH,input_xpath)

    def click_select_logistics(self,driver,company):
        """
        选择物流公司
        :param driver:
        :param company:
        :return:
        """
        select_xpath = self.select_logistics(company)
        return self.element_click(driver,By.XPATH,select_xpath)

    def input_logistics_order_no(self,driver,order_no):
        """
        填入物流单号
        :param driver:
        :param order_no:
        :return:
        """
        input_xpath = self.logistics_order_no()
        return self.element_fill_value(driver,By.XPATH,input_xpath,order_no)

    def click_evaluation(self,driver,num):
        """
        评价星级
        :param driver:
        :param num:
        :return:
        """
        star_xpath = self.evaluation(num)
        return  self.element_click(driver,By.XPATH,star_xpath)

    def click_evaluation_confirm(self,driver):
        """
        评价后点击确定
        :param driver:
        :return:
        """
        button_xpath = self.evaluation_confirm()
        return self.element_click(driver,By.XPATH,button_xpath)



