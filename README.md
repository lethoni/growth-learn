## 使用Fabric搭建构建系统
**安装** `pip install fabric3`
**运行** `$ fab [para]`

[Fabric](https://fabric-chs.readthedocs.io/zh_CN/chs/tutorial.html) 是一个 Python的库和命令行工具，用来提高基于 SSH 的应用部署和系统管理效率。具体来说：
- 一个让你通过 命令行 执行 无参数 Python 函数 的工具；
- 一个让通过 SSH 执行 Shell 命令更加 容易 、 更符合 Python 风格 的命令库（建立于一个更低层次的库）。

#### 示例
在当前的工作目录中一个名为 **fabfile.py** 的 Python 模块文件，写入下列代码，然后这个 hello 函数就可以用 fab 工具（随 Fabric 一并安装的命令）来执行了，输出的结果会是这样：
```
def hello():
	"""Print hello""
    print("Hello world!")

>>> $ fab hello
	Hello world!

	Done.
```


## PEP8 代码风格检测
 **安装** `pip install pep8==1.7.0` 
 **运行** `$ pep8 .`

**代码更多的是用来读而不是写的**。python代码需要遵循pep8指南使风格统一，但有以下几点可以违反指南：
- 遵循指南会降低可读性
- 与周围其他代码不一致
- 代码写在引入指南之前，暂时没有理由修改
- 旧版本兼容

其他检测pep8可用包：`pylint`(检测更为严格)


## 编码

常用编码过程：
![编码过程](http://pbn1d3gdg.bkt.clouddn.com/%E7%BC%96%E7%A0%81%E8%BF%87%E7%A8%8B.png)

1.创建首页页面*Tasking*：

- 创建首页应用
- 合并着陆页
- 编写单元测试
- 使用Selenium进行功能测试
- 编写自动测试的Fabric任务

**小步前进**，每一步都有明确任务和衡量指标，完成一步提交一次代码，有问题可随时回滚。

[SMRT原则](http://wiki.mbalib.com/wiki/SMART原则)，对更大的目标管理方法。（S=Specific(明确性)，M=Measurable(衡量性)，A=Attainable(可实现性)，R=Relevant(相关性)，T=Time(时限性)）



## 使用Selenium测试
**安装** pip install selenium

Selenium是一个Web应用程序测试框架，它可以让浏览器自动化地执行任务,且可以模拟真实人为操作。Selenium使用浏览器需要对应驱动，Chrome使用[chromedriver](http://seleniumhq.github.io/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.webdriver.html#module-selenium.webdriver.chrome.webdriver)，Firefox使用[geckodriver](https://github.com/mozilla/geckodriver/releases)，需要放置于对应浏览器根目录。
> PS: 
> 1. 如路径错误( selenium.common.exceptions.WebDriverException: Message: ‘ChromeDriver executable needs to be available in the path.)则配置chromedriver路径：`driver = webdriver.Chrome('/path/to/chromedriver')`
> 2. [Chrome](https://www.chromedownloads.net/chrome64win/)历史版本下载
> 3. 使用webdriver出现的问题：[18796:1808:0730/131103.313:ERROR:install_util.cc(600)] Failed to read HKLM\SOFTWARE\Policies\Google\Chrome\MachineLevelUserCloudPolicyEnrollmentToken: 系统找不到指定的文件。 (0x2) 1,注册表导致 regedit.exe-HKEY_LOCAL_MACHINE-SOFTWARE-Policies-google-Chrome-右键新建字符串值(s):MachineLevelUserCloudPolicyEnrollmentToken 2,确认webdriver是否匹配[修复方法](https://www.cnblogs.com/cthon/p/9390095.html)


*四阶段测试* ：
1. Setup -- 数据准备和初始化
2. Execute -- 执行阶段做好验证结果前工作
3. Verify -- 验证返回的结果是否和预期一致
4. Tear Down -- 收尾工作，关闭浏览器、清除测试数据

*测试的好处*：
- 保证现有代码功能都正常
- 帮组找到代码中的bug
- 编写出长度短小的代码
- 为重构代码打下基础

**测试金字塔**：

组成(金字塔由下至上)：
- 单元测试(针对**程序模块**进行正确性检验，最底层，测试最多)
- 服务测试(不仅测试提供的服务，也测试依赖第三方提供的服务，可使用提供API的Mock Server)
- UI测试(主要对功能测试，尽可能将此层级测试网下层移动，节约测试时间)

**如何测试**：
1. 了解测试目的（Why）
2. 要测哪些内容（What）（单元测试中测试函数功能，服务测试中测试服务，UI测试中测试业务）
3. 要如何进行测试（How）
 - 状态测试（针对结果）
 - 行为测试（针对执行过程）

 
 ## 创建应用Tasking
 Tasking基本框架：
 - 生产基本的脚手架(基本模型、Controller最小逻辑及URL处理、基本模板)
 - 设计和创建数据模型(数据库、表、ORM层)
 - 编写业务逻辑(Controller、前台)
 - 完成页面显示及美化(HTML、CSS、JavaScript)
 
 
## 模板复用
先完成基本模板，后用代码块block代码重构：
- 抽取出一个基本的模板文件base.html
- 将首页内容提取到index.html
- 基于模板优化其他页面 


## 数据与web应用
不同开发人员关注点不同：
- 后端开发人员，关注如何正确、可靠的方式管理数据
- 前端开发人员，关注提供一个好的交互界面
- 业务分析员，关注如何分析数据，便于作出更好的业务决策

**管理数据**
对于数据的操作，有增加、读取、更新和删除四项基本操作，即CRUD。创建数据时，主要考虑**数据验证**和**鉴权**。
1. 鉴权，判定是否有创建权限
2. 验证，数据是否符合要求(为更好用户体验，可用JavaScript校验)

**显示数据**
三步走：获取数据，过滤数据，美化界面。
对后台模板形式返回HTML应用，是在*服务器*完成渲染和过滤，浏览器显示；
对单页面应用，则由前台向后台请求(通常Ajax, Fetch)，服务器返回数据，前台进行过滤，浏览器显示。


## 上线
手动部署与自动化部署步骤差不多：
- 安装运行时所需要的软件包
- 获取代码或已编译的二进制包
- 运行我们的应用
- 为应用配置地址、缓存

**LNMP**介绍：
- L，Linux,对应操作系统
- N，Nginx，对应HTTP服务器
- M，MySQL，对应数据库
- P，PHP/Python等，对应编程语言

**部署应用**：
- 使用SSH连接远程服务器
- 安装web应用所需要的基础软件包
- 安装并测试我们的应用
- 对系统及应用服务进行配置
- 启动和停止系统服务

在服务器上运行runserver，首先需要将软件包放置到服务器上，可使用下列方法：
- 使用git将代码clone到服务器(不推荐，存在安装隐患，如：google - index of/.git)
- 使用scp上次软件包
- 从某个服务器上下载软件包
- 使用包管理工具直接安装

**线上部署工具**:
用[Gunicorn](http://docs.gunicorn.org/en/stable/settings.html)提供应用的多线程服务，用Nginx承担静态文件等请求(Nginx还可承担安全任务，如反爬虫，限制IP访问等)，使用Nginx反向台历HTTP请求给Gunicorn，由Gunicorn再将请求交给web应用程序。
运行 `nohup gunicorn -w 2 -b unix:/tmp/growth_studio.sock growth_studio.wsgi:application&`(nohup..&后台运行)Gunicorn与Django为WSGI通信，与Nginx使用socket套接字通信。

1. Nginx,高性能的HTTP和反向代理服务器
 - 安装 `sudo apt-get install nginx`
 - 配置 `/etc/nginx/site-available/default`
 - 测试 `sudo nginx -t`
 - 启动 `/usr/sbin/nginx -c /etc/nginx/nginx.conf` 
 - 重启 `/usr/sbin/nginx -s reload`
 - 停止 `/usr/sbin/nginx -s stop`
2. Gunicorn, WSGI服务器(其他：Chaussette)
 - 安装 `pip install gunicorn`
 - 启动(项目根目录) `gunicorn -w 3 -b 127.0.0.1:8080 project.wsgi:application`(-w INT 开多个进程， -b ADDRESS)
 - 静态文件收集管理 `python manage.py collectstatic`
3. ~~Supervisor, 进程守护工具(Python 2.x编写)~~
4. Circus, 进程管理工具(Python3)
 - 安装(需退出虚拟环境) `pip install circus`
 - 添加配置文件 `circus.ini`
 - 启动 `circusd circus.ini` (后台参数 --daemon)
  
>circus.ini :
[watcher:growth_studio]
cmd = gunicorn --workers=2 --bind unix:/tmp/growth-studio.sock growth_studio.wsgi:application
working_dir = /home/myproject/growth-studio
copy_env = True
virtualenv = /home/myproject/venv
send_hup = True
  
![supervisord配置方法](http://pbn1d3gdg.bkt.clouddn.com/supervisord%E9%85%8D%E7%BD%AE.png)
![Circus配置方法](http://pbn1d3gdg.bkt.clouddn.com/Circus%E9%83%A8%E7%BD%B2.png)
