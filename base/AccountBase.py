class AccountBase:
    def basic_info_avatar_input(self):
        """
        基本资料-个人头像
        :return:
        """
        return "//input[@type='file']"

    def basic_info_save_button(self):
        return "//span[text()='保存']/parent::button"
