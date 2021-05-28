# 自动化测试

#### 介绍
Web自动化测试项目

#### 软件架构
- 语言：python
- 自动化框架：selenium
- 设计模式:POM/关键字/数据驱动
- 自动化用例组织框架：pytest

#### 安装教程

1.  https://gitee.com/mikb/automated-testing.git 拉取代码
2.  pip install -r requirements.txt 安装依赖库
3.  修改config.ymal配置文件
4.  执行run.py

#### 目录结构
```shell
├─config
│  └─config.yaml	# 配置文件
├─data
│  └─test_data.xlsx	# 测试数据
├─log
│  └─run...x.log	# 日志文件
├─report
│  ├─xml                # 报告数据
│  └─html		# allure报告
├─AppTestCases          # 待开发
|
├─WebUiTestCases        # web测试用例
|  ├─POM                # 页面对象管理
│  ├─conftest.py	# pytest依赖对象初始化
│  └─*_test.py	        # 测试文件
├─libs		        # 工具包
│  ├─__init__.py		# 常用方法封装
│  ├─common	        # web公用方法
│  └─utils	        # 常用工具
├─pytest.ini	   # pytest配置文件
├─requirements.txt		 # 项目依赖库文件
└─run.py	# 主启动文件
```


#### 使用说明

1.  POM层完成元素定位和常用流程的封装，一个页面一个py文件。用例层写整体逻辑调用。
2.  支持谷歌，火狐，IE浏览器。需要将浏览器驱动路经放在系统path变量下。
3.  测试报告使用allure，如要集成jenkins需改动。
4.  本项目会陆续迭代，如果各位有什么建议 欢迎提给我，会尽力解决~~


#### 实现功能
1.  web自动化测试
2.  自动发送邮件
3.  本地执行和远程执行
4.  全局共用一个浏览器对象

#### 待开发
1.  失败重跑
2.  失败截图
3.  多线程执行
4.  接口自动化和app自动化
5.  持续开发中
