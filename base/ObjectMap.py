import time
from selenium.common.exceptions import ElementNotInteractableException


class ObjectMap:
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
        raise ElementNotInteractableException("元素定位失败，定位方式"+locate_type)
