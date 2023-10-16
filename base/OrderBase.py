class OrderBase:
    def order_tab(self, tab_name):
        """
        订单tab按钮
        :param tab_name:
        :return:
        """
        return "//div[@role='tab' and text() = '" + tab_name + "']"

    def order_operation(self,product_title,operation):
        """
        订单的操作按钮
        :param product_title: 商品标题
        :param operation: 操作
        :return:
        """
        return "//div[text()='"+product_title+"']/ancestor::tr//span[text()='"+operation+"']/parent::button"

    def order_operation_confirm(self):
        """
        点击操作按钮后，弹框的确定按钮
        :return:
        """
        return "//div[@class='el-dialog__wrapper' and contains(@style,'index')]//span[text()='确 定']/parent::button"
