class HomeBase:
    def wallet_switch(self):
        """
        获取首页上面的开关
        :return:
        """
        return "//span[contains(@class,'switch')]"

    def logo(self):
        """
        获取进入系统后，首页左上角的logo
        :return:
        """
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        return "//span[starts-with(text(),'欢迎您回来')]"


    def show_date(self):
        """
        following-sibling:寻找同级元素 下一个div
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avatar(self):
        """

        :return:
        """
        return "//span[text(),'我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar)]//img "
        return  "//span[contains(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img"
