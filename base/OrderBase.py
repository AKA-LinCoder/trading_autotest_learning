class OrderBase:
    def order_tab(self, tab_name):
        """
        订单tab按钮
        :param tab_name:
        :return:
        """
        return "//div[@role='tab' and text() = '" + tab_name + "']"
