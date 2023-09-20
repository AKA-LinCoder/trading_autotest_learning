class IframeBaiduMapBase:
    def search_button(self):
        """
        定位百度地图中的按钮
        :return:
        """
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com']"
