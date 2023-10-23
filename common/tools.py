import datetime
import os

import requests


def get_now_time():
    return datetime.datetime.now()


def get_now_date_time_str():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def get_project_path():
    """
    获取项目绝对路径
    :return:
    """
    # project_name = "my_trading"
    project_name = "trading_autotest_learning"
    file_path = os.path.dirname(__file__)
    print(file_path)
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


def get_img_path(img_name):
    """
    获取商品图片的路径
    :param img_name:
    :return:
    """
    img_dir_path = get_project_path() + sep(["img", img_name], add_sep_before=True)
    return img_dir_path


def get_every_wallpaper():
    """
    从bing获取每日壁纸
    :return:
    """
    everyday_wallpaper_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&mkt=zh-CN"
    try:
        res = requests.get(url=everyday_wallpaper_url)
        wallpaper_url = "https://cn.bing.com"+res.json()["images"][0]["url"][:-7]
    except Exception as e:
        print(e)
        wallpaper_url = ""
    return wallpaper_url


if __name__ == '__main__':
    print(get_every_wallpaper())
    print(get_img_path("商品图片一.jpg"))
