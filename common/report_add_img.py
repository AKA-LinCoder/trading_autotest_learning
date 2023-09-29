import allure
from time import sleep

def add_img_to_report(driver,step_name,need_sleep=True):
    """
    直接截图并插入allure
    :param driver:
    :param step_name:
    :param need_sleep:
    :return:
    """
    if need_sleep:
        sleep(2)
    allure.attach(driver.get_screenshot_as_png(),step_name+".png",allure.attachment_type.PNG)

def add_img_path_to_report(img_path,step_name):
    """
    将图片插入Allure报告
    :param img_path: 图片路径
    :param step_name: 步骤名称
    :return:
    """
    allure.attach.file(img_path,step_name,allure.attachment_type.PNG)