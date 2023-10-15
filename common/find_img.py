import aircv as ac
import cv2
from common.tools import get_project_path, sep,get_now_date_time_str
from common.report_add_img import add_img_path_to_report


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
        # 在原图上画框
        cv2.rectangle(
            img_src,
            result["rectangle"][0],
            result["rectangle"][3],
            (255, 0, 0),
            thickness=2
        )
        diff_img_path = get_project_path()+sep(["img","diff_img",get_now_date_time_str()+"-对比的图.jpg"],add_sep_before=True)
        # 保存图片到指定地址
        cv2.imencode(".png",img_src)[1].tofile(diff_img_path)
        # 图片加入测试报告
        add_img_path_to_report(diff_img_path,"查找到的图")
        return result["confidence"]
