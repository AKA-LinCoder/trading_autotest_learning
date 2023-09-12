## 显示ValueError: Timeout value connect was ……, but it must be an int, float or None
是Selenium和urllib3版本不兼容的问题，降低urllib3的版本就好，当前使用 版本urllib3 为1.26.2,Selenium版本为3.141.0
链接：https://blog.csdn.net/weixin_60535956/article/details/131660133

##  selenium chromedriver unexpectedly exited. Status code was: -9
能正常运行一次，再想运行就会报错，更新了Chrome浏览器之后 运行起了一次，然后又报这个错了
https://cloud.tencent.com/developer/article/1365269

https://registry.npmmirror.com/binary.html?path=chromedriver/

总之就在Chrome浏览器和Chromedriver版本不兼容

https://googlechromelabs.github.io/chrome-for-testing/#stable


## PO模式
1. 增强测试维护
2. 减少代码重复