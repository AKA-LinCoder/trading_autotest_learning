import datetime
import os
import time
from selenium.common.exceptions import ElementNotInteractableException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from common.yaml_config import GetConf
from selenium.webdriver.common.keys import Keys
from common.tools import get_project_path, sep
from common.find_img import FindImg


class ObjectMap:
    url = GetConf().get_url()

    def element_get(self, driver, locate_type, locate_expression, timeout=10, must_be_visible=False):
        # 开始时间
        start_ms = time.time() * 1000
        # 设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find_element(by=locate_type, value=locate_expression)
                # 如果元素不是必须可见的就直接返回元素
                if not must_be_visible:
                    return element
                # 如果元素是必须可见的,则徐图先判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception
            except Exception:
                # 判断当前时间是否大于总时间
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotInteractableException("元素定位失败，定位方式" + locate_type)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        start_ms = time.time() * 1000
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # 获取页面的状态
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                # 如果有driver的错误，执行js出错,就直接跳过
                time.sleep(0.03)
                return True
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # 如果超时了就break
                if now_ms >= stop_ms:
                    break
                time.sleep(0.01)
        raise Exception("打开网页时，页面元素在%s秒后仍然没有加载完成" % timeout)

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
            :param driver: 浏览器驱动
            :param locate_type: 定位方式类型
            :param locator_expression: 定位表达式
            :param timeout: 超时时间
            :return:
            """
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.01)
                    pass

            raise ElementNotInteractableException(
                "元素没有出现，定位方式：" + locate_type + "定位表达式" + locator_expression)
        else:
            pass

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        """

        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:
            start_ms = time.time() * 1000
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.01)
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式：" + locate_type + "定位表达式" + locator_expression)
        else:
            pass

    def element_to_url(self, driver, url, locate_type_disappear=None, locator_expression_disappear=None,
                       locate_type_appear=None, locator_expression_appear=None):
        """

        :param driver: 浏览器驱动
        :param url: 跳转的地址
        :param locate_type_disappear: 等待页面元素消失的定位方式
        :param locator_expression_disappear: 等待页面元素消失的定位表达式
        :param locate_type_appear: 等待页面元素出现的定位方式
        :param locator_expression_appear: 等待页面元素出现的定位表达式
        :return:
        """
        try:
            driver.get(self.url + url)
            # 等待页面元素加载完成
            self.wait_for_ready_state_complete(driver)
            # 跳转地址后等到元素消失
            self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)
            # 跳转地址后等带元素出现
            self.element_appear(driver, locate_type_appear, locator_expression_appear)
        except Exception as e:
            print("跳转地址出现异常,异常原因%s" % e)
            return False
        return True

    # 元素是否显示
    def element_is_display(self, driver, locate_type, locator_expression):
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            # 发生NoSuchElementException,说明页面中没有找到该元素
            return False

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        元素填值
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param fill_value: 填入的值
        :param timeout: 超时时间
        :return:
        """
        # 元素必须先出现
        element = self.element_appear(
            driver,
            locate_type,
            locator_expression,
            timeout
        )
        try:
            # 清除输入框值
            element.clear()
        except StaleElementReferenceException:
            # 页面元素没有刷新出来，就对元素进行捕获，就会触发
            self.wait_for_ready_state_complete(driver)
            time.sleep(0.06)
            element = self.element_appear(
                driver,
                locate_type,
                locator_expression,
                timeout
            )
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass

        # 填的值转字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        # 判断字符串后面是否跟了\n
        # 填入的值不是\n结尾
        try:
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type, locator_expression)
            element.clear()
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver)
        except Exception:
            raise Exception("元素填值失败")

        return True

    def element_click(self, driver, locate_type, locator_expression, locate_type_disappear=None,
                      locator_expression_disappear=None,
                      locate_type_appear=None, locator_expression_appear=None, timeout=30):
        """
        元素点击
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param locate_type_disappear: 等待元素消失的定位方式
        :param locator_expression_disappear: 等待元素消失的定位表达式
        :param locate_type_appear: 等待元素出现的定位方式
        :param locator_expression_appear: 等待元素出现的定位表达式
        :param timeout: 超时时间
        :return:
        """
        # 元素要可见
        element = self.element_appear(driver, locate_type, locator_expression, timeout)
        try:
            # 元素点击
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type, locator_expression, timeout)
            element.click()
        except Exception as e:
            print("页面出现异常元素不可点击" + e)
            return False
        try:
            # 点击元素后，元素出现或消失
            self.element_appear(
                driver,
                locate_type_appear,
                locator_expression_appear
            )
            self.element_disappear(
                driver,
                locate_type_disappear,
                locator_expression_disappear
            )
        except Exception as e:
            print("等待元素出现或消失失败" + e)
            return False
        return True

    def upload(self, driver, locate_type, locator_expression, file_path):
        """
        文件上传
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param file_path:
        :return:
        """
        element = self.element_get(driver, locate_type, locator_expression)
        return element.send_keys(file_path)

    def switch_window_2_latest_handle(self, driver):
        """
        句柄切换窗口到最新的窗口
        :param driver:
        :return:
        """
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

    def switch_into_iframe(self, driver, locate_iframe_type, locate_iframe_expression):
        """
        进入iframe
        :param driver:
        :param locate_iframe_type: 定位iframe方式
        :param locate_iframe_expression: 表达式
        :return:
        """
        iframe = self.element_get(driver, locate_iframe_type, locate_iframe_expression)
        driver.switch_to.frame(iframe)

    def switch_from_iframe_to_content(self, driver):
        """
        从iframe切回主文档
        :param driver:
        :return:
        """
        driver.switch_to.parent_frame()

    def find_img_in_source(self, driver, img_name):
        """
        截图，并在截图中查找图片
        :param driver:
        :param img_name:
        :return:
        """
        # 截图后图片保存路径
        source_img_path = get_project_path() + sep(["img", "diff_img", img_name], add_sep_before=True)
        # 需要查找的图片路径
        search_img_path = get_project_path() + sep(["img", "assert_img", img_name], add_sep_before=True)
        # 截图并保存图片
        driver.get_screenshot_as_file(source_img_path)
        time.sleep(3)
        # 在原图中查找是否有指定的图片，返回信心值
        confidence = FindImg().get_confidence(source_path=source_img_path, search_path=search_img_path)
        return confidence


    def element_screenshot(self, driver, locate_type, locator_expression):
        """
        元素截图
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        ele_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
        ele_img_dir_path = get_project_path() + sep(["img", "ele_img"], add_sep_before=True, add_sep_after=True)
        if not os.path.exists(ele_img_dir_path):
            os.mkdir(ele_img_dir_path)
        ele_img_path = ele_img_dir_path + ele_name
        self.element_get(driver, locate_type, locator_expression).screenshot(ele_img_path)
        return ele_img_path

    def scroll_to_element(self, driver, locate_type, locator_expression):
        """
        滚动到元素
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        ele = self.element_get(driver, locate_type, locator_expression)
        driver.execute_script("arguments[0].scrollIntoView()", ele)
        return True