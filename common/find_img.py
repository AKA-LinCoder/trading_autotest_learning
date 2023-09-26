import aircv as ac
from common.tools import get_project_path, sep


class FindImg:
    def img_imread(self, img_path):
        """
        读取图片
        :param img_path:
        :return:
        """
        return ac.imread(img_path)

    def get_confidence(self, source_path, search_path):
        """
        查找图片
        :param source_path: 原图路径
        :param search_path: 需要查找的图片的路径
        :return:
        """
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        result = ac.find_template(img_src, img_sch)
        print(result)


if __name__ == '__main__':
    source = get_project_path() + sep(["img", "diff_img/20220710002104-对比的图.png"], add_sep_before=True)
    search = get_project_path() + sep(["img", "assert_img/head_img.png"], add_sep_before=True)
    FindImg().get_confidence(source, search)
