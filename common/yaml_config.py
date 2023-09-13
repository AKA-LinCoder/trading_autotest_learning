# file = open("/Users/estim/Desktop/自动化测试学习/my_trading/config/environment.yaml", encoding="utf-8")
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()

with open("/Users/estim/Desktop/自动化测试学习/my_trading/config/environment.yaml","r",encoding="utf-8") as file:
    a = file.read()
    print(a)
    for i in file.readlines():
        print(i)
