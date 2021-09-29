# UI自动化测试框架

#### 介绍
基于selenium,python的WebUI自动化测试框架,移动端移到android_app仓库

#### 软件架构
- 语言：python
- 自动化框架：selenium
- 设计模式:POM/关键字驱动/数据分离
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
    │  └─config.ini	# 配置文件
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
    │  ├─locator          #页面定位
    │  └─page.py          #业务封装
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
    └─run.py	# 主启动文件
```


#### 使用说明

1.  本框架已经完成公共方法部分，只需要根据项目具体需求完成元素定位器，业务封装和用例封装即可运行自动化测试
2.  支持Chrome，火狐，IE，Safari，Edge启动
5.  本项目会陆续优化，如果各位有什么建议 欢迎给我留言，会尽力解决~~


#### 实现功能
1.  底层全部采用显示等待和EC模块封装，提高框架执行效率和稳定性
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
13. 底层方法大多与selenium接口同名或者见名知其意，方便团队其他人使用

#### 待开发
1.  多线程执行
2.  兼容linux

