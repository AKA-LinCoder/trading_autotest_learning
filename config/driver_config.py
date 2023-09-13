from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

from common.tools import get_project_path, sep

from webdriver_manager.chrome import ChromeDriverManager


class DriverConfig:
    @staticmethod
    def driver_config():
        """
        浏览器启动
        :return:
        """
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        # 设置窗口大小
        options.add_argument("window-size=1920,1080")
        # 无头模式
        # options.add_argument('--headless')
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-dev-shm-usage')
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        # 无痕模式
        options.add_argument("--incognito")
        # 去除"chrome正受到自动化测试软件的控制"
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )

        # 实例化浏览器驱动

        driver = webdriver.Chrome(

            ChromeDriverManager().install(),
            # ChromeDriverManager(url="http://npm.taobao.org/mirrors/chromedriver",
            #                     latest_release_url="http://npm.taobao.org/mirrors/chromedriver/LATEST_RELEASE").install(),
            # executable_path=get_project_path() + sep(["driver_files", "chromedriver"], add_sep_before=True),
            # executable_path="/Users/estim/Downloads/chromedriver_mac_arm64/chromedriver",

            options=options
        )

        # driver = webdriver.Chrome(ChromeDriverManager(url="https://registry.npmmirror.com/-/binary/chromedriver",
        #                                               latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
        #                                               ).install(),
        #                           options=options)
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # 删除所有cookies
        driver.delete_all_cookies()
        # 隐性等待时间
        driver.implicitly_wait(10)
        return driver


if __name__ == "__main__":
    DriverConfig().driver_config()
