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
