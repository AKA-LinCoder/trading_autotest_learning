from common.process_redis import Process
from common.ding_talk import send_dingtalk_msg_markdown
from common.yaml_config import GetConf

from common.qywx import send_qywx_msg_markdown

# 获取测试结果
total, success, fail, _ = Process().get_result()

failed_testcases_name = ",失败的用例为:"
msg_str = f"测试通过{str(success)}个，失败{str(fail)}个"
# 如果有失败,就加上失败的用例名称
if int(fail) > 0:
    msg_str = msg_str + failed_testcases_name
    fail_testcase_names = Process().get_fail_testcase_name()
    for i in range(len(fail_testcase_names)):
        if i == len(fail_testcase_names) - 1:
            failed_testcases_name += fail_testcase_names[i]
        else:
            failed_testcases_name += fail_testcase_names[i] + ","

        msg_str += fail_testcase_names[i] + "\n"

else:
    failed_testcases_name = ""

# 插入测试结束时间
Process().write_end_time()
# 更改运行状态为0
Process().modify_running_status(0)

# 项目名称
project_name = "my_auto_test"

# 报告标题
report_title = "自动化测试报告"

# jenkins地址
jenkins_url = GetConf().get_jenkins()
# allure测试报告地址
allure_url = jenkins_url + "/job/" + project_name + "/allure/"
# 发送报告到钉钉
dingding_webhook = GetConf().get_dingding_webhook()
send_dingtalk_msg_markdown(dingding_webhook,
                           allure_url,
                           total,
                           success,
                           fail,
                           failed_testcases_name,
                           report_title
                           )

# 发送到企业微信
qywx_webhook = GetConf().get_qywx_webhook()
send_qywx_msg_markdown(qywx_webhook, allure_url, report_title, total, success, fail, failed_testcases_name)
