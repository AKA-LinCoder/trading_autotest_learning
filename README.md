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
### 主要目录
- base 包用来存放元素定位
- page 包用来存放元素操作
- testcases 包用来存放测试用例
- common 包用来存放工具类
- config 包用来存放配置文件以及浏览器启动类
- logs 包用来存放日志

## 目录介绍
> base: 包括selenium二次封装以及各个页面元素的封装
> 
> common: 包括部分通用方法
>  
> config: 包括driver方法和配置文件
> 
> img: 存放图片
> 
> logs: 日志相关
> 
> page: 页面类
> 
> testcase: 测试用例


## YAML
- 大小写敏感
- 使用缩进表示层级关系
- 缩进不允许使用Tab，只能使用空格
- 缩进的空格数不重要，只要相同层级的元素左对齐即可
- #表示注释

YAML 数据类型
1. 纯量：单个的，不可再分的值
2. 数组
3. 对象

## Selenium
![流程图](./images/selenium1.png)
![流程图](./images/selenium2.png)

## 封装浏览器驱动  

下载对应浏览器的Chromedriver
进入路径 执行chmod +x chromedriver 

webdrivermanager 自动下载更新webdriver

## 元素定位方法
- CSS
- XPATH

//查找标签h1中class包含123的
//h1[contains(@class,'123')]

//查找标签h1中的值中包含123的
//h1[contains(text(),'123')]

## 前端主流框架

- React
- Vue
- Angular

获取元素的步骤

- 元素需不需要可见
- 元素如果可见，就返回元素定位；元素不可见，需要怎么操作
- 如果一直定位不到元素，应该怎么办

![流程图](./images/xPath1.png)

### 页面什么时候才算加载完成
在浏览器控制台 输出 document.readyState可以查看当前页面加载状态
![流程图](./images/loading1.jpg)

### 等待页面元素消失
![流程图](./images/loading2.jpg)

### 等待页面元素出现
![流程图](./images/loading3.jpg)

### 跳转到指定网站
![流程图](./images/loading4.jpg)