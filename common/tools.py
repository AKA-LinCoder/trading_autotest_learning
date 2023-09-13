import datetime
import os


def get_now_time():
    return datetime.datetime.now()


def get_now_date_time_str():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def get_project_path():
    """
    获取项目绝对路径
    :return:
    """
    project_name = "my_trading"
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


if __name__ == '__main__':
    get_project_path()
