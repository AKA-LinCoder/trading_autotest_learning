# # conftest.py
# import pytest
# from py._xmlgen import html
# from datetime import datetime
#
#
# # 优化报告的环境信息，删除JAVA_HOME行，增加项目名称和操作系统
# @pytest.mark.parametrize
# def pytest_configure(config):
#     config._metadata.pop("JAVA_HOME")  # 删除java_home
#     config._metadata["项目名称"] = "六天测试的演示项目"  # 添加项目名称
#     config._metadata["操作系统"] = "64位Windows 10"  # 添加操作系统信息
#
#
# # 修改用例统计看，Summary部分内容
# @pytest.mark.parametrize
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.p("所属部门：测试组")])
#     prefix.extend([html.p("测试人员：六天测试")])
#
#
# # 修改测试结果 Results 中用例的表头，从第二列（测试用例）后新增Description和Time列，删除最后的link
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th("Description"))  # 表头添加Description
#     cells.insert(3, html.th("Time", class_="sortable time", col="time"))
#     cells.pop(-1)  # 删除link
#
#
# # 修改测试结果 Results 中用例的表头
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))  # 表头对应的内容
#     cells.insert(3, html.td(datetime.now(), class_="col-time"))
#     cells.pop(-1)  # 删除link
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):  # Description取值为用例说明__doc__
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
#     report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")
