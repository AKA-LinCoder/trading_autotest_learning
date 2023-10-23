# file = open("/Users/estim/Desktop/自动化测试学习/my_trading/config/environment.yaml", encoding="utf-8")
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()
#
# with open("/Users/estim/Desktop/自动化测试学习/my_trading/config/environment.yaml","r",encoding="utf-8") as file:
#     a = file.read()
#     print(a)
#     for i in file.readlines():
#         print(i)
import yaml
from common.tools import get_project_path, sep


class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            print(self.env)

    def get_username_password(self, user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        return self.env["url"]


    def get_mysql_config(self):
        return self.env["mysql"]

    def get_redis(self):
        return self.env["redis"]

    def get_dingding_webhook(self):
        return self.env["dingding_group"]["webhook"]

    def get_jenkins(self):
        return self.env["jenkins"]["url"]

    def get_qywx_webhook(self):
        return self.env["qywx_group"]["webhook"]


if __name__ == '__main__':
    print(GetConf().get_username_password("jay"))
