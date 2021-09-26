# UI自动化测试框架

#### 介绍
基于selenium,python的WebUI自动化测试框架,移动端移到android_app仓库

#### 软件架构
- 语言：python
- 自动化框架：selenium
- 设计模式:POM/关键字驱动/数据分离/配置分离
- 自动化用例组织框架：pytest
- 自动化报告：allure

#### 设计原则
1.  公共方法为页面提供操作服务
2.  封装细节，对外只提供方法名（或者接口）
3.  断言放在用例
4.  通过return跳转到新页面
5.  页面中重要元素进行PO管理
6.  对相同行为产生不同结果进行封装

#### 安装教程

1.  https://gitee.com/mikb/automated-testing.git 拉取代码
2.  pip install -r requirements.txt 安装依赖库
3.  修改config.yaml配置文件
4.  执行run_web.py

#### 目录结构
```shell
|-- 自动化测试 # 主目录
    ├─config
    │  └─config.yaml	# 配置文件
    ├─data
    │  └─test_data.yaml	# 测试数据
    ├─log
    │  └─...x.log	# 日志文件
    ├─img
    │  └─...x.png	# 测试失败截图文件
    ├─report
    │  ├─xml                # 报告数据
    │  └─html		# allure报告
    ├─POM                # 页面对象管理
    │  ├─web_pom
    ├─TestCases        # web测试用例
    │  ├─conftest.py	# pytest依赖对象初始化
    │  └─*_test.py	        # 测试文件
    ├─libs		        # 工具包
    │  ├─__init__.py		# 常用方法封装
    │  ├─common	        # web公用方法
    │  └─utils	        # 常用工具
    ├─globalvar.py      # 项目全局变量管理
    ├─pytest.ini	   # pytest配置文件
    ├─requirements.txt		 # 项目依赖库文件
    ├─README.md          #自述文件
    ├─setting.py         #项目相关设置
    └─run_web.py	# web测试主启动文件
```


#### 使用说明

1.  页面对象层封装，可以浏览器对象为基础对象封装，或者公共对象为基础封装。
2.  封装页面对象可以以单页面为基础模块封装，也能以业务模块为基础封装。本例采用单页面模块封装适合业务流程不复杂场景（具体跟据项目场景合理选择封装方式）
3.  支持谷歌，火狐，IE浏览器。需要将浏览器驱动路经放在系统path变量下。
4.  测试报告使用allure，如要集成jenkins需需将run里面生成报告注释掉
5.  本项目会陆续优化，如果各位有什么建议 欢迎给我留言，会尽力解决~~


#### 实现功能
1.  底层全部采用EC模块封装，提高框架执行效率和稳定性
2.  自动发送压缩allure报告
3.  log模块采用页面描述和元素描述，实现快速定位问题
4.  全局共用一个浏览器，提高执行效率
5.  自动生成测试数据
6.  自动清除上次执行的截图以及log
7.  测试失败截图，并加入allure报告
8.  定制美观的allure报告
9.  用例失败重跑
10. 采用通用配置文件，增强框架可维护性
11. 采用yaml文件管理测试数据
12. 采用类管理元素定位，方便后期维护


#### 待开发
1.  多线程执行
2.  兼容linux

