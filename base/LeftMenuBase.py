class LeftMenuBase:
    def level_one_menu(self, menu_name):
        """

        :param menu_name:一级菜单栏名称
        :return:
        """
        return "//aside[@class='el-aside]//span[text()='" + menu_name + "']/ancestor::li"

    def level_two_meu(self, menu_name):
        """
        查找二级菜单
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text() = '" + menu_name + "']/parent::li"
