[精益实践源码](https://github.com/phodal/growth-code)

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

> fabfile中一些语句使用[方法](http://www.bjhee.com/fabric.html)

> fab 使用的fabfile.py 未放置于当前路径时，需要使用-f指定路径，`fab -f "path" test`

> fabric在远程执行run（'nohup xxx &'） 后台运行进程时，虽然返回的$?是0，但是机器上并没有执行命令，这种情况主要是由于Fabric过早关闭了连接的Session导致的，在需要执行命令后加sleep，比如run（'nohup xxx & '） 改为 run（'（nohup xxx & ）&& sleep 1'）  这样就可以解决问题。


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

**管理数据**：

对于数据的操作，有增加、读取、更新和删除四项基本操作，即CRUD。创建数据时，主要考虑**数据验证**和**鉴权**。
1. 鉴权，判定是否有创建权限
2. 验证，数据是否符合要求(为更好用户体验，可用JavaScript校验)

**显示数据**：

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

**Linux下SSH服务器端工具**：

安装：`sudo apt-get install openssh-server`
启动：`/etc/init.d/ssh start`

Windows下使用[PuTTY](https://www.putty.org/)软件登陆SSH：
配置文件设置：
>如不修改默认使用KEY文件,用户名登陆会出现错误(PuTTY error: "No supported authentication methods available")，这里解决这个问题。
```
/etc/ssh/sshd_config

PasswordAuthentication yes
PermitRootLogin yes  #默认prohibit-passwd
```

在服务器上运行runserver，首先需要将软件包放置到服务器上，可使用下列方法：
- 使用git将代码clone到服务器(不推荐，存在安装隐患，如：google - index of/.git)
- 使用scp上次软件包
- 从某个服务器上下载软件包
- 使用包管理工具直接安装

**线上部署工具**：

用[Gunicorn](http://docs.gunicorn.org/en/stable/settings.html)提供应用的多线程服务，用Nginx承担静态文件等请求(Nginx还可承担安全任务，如反爬虫，限制IP访问等)，使用Nginx反向台历HTTP请求给Gunicorn，由Gunicorn再将请求交给web应用程序。
运行 `nohup gunicorn -w 2 -b unix:/tmp/growth_studio.sock growth_studio.wsgi:application&`(nohup..&后台运行)Gunicorn与Django为WSGI通信，与Nginx使用socket套接字通信。

1. Nginx,高性能的HTTP和反向代理服务器
 - 安装 `sudo apt-get install nginx`
 - 配置 `/etc/nginx/site-available/default`
 - 测试 `sudo nginx -t`
 - 启动 `/usr/sbin/nginx -c /etc/nginx/nginx.conf` 
 - 重启 `service nginx restart`
 - 停止 `service nginx stop`
2. Gunicorn, WSGI服务器(其他：Chaussette)
 - 安装 `pip install gunicorn`
 - 启动(项目根目录) `gunicorn -w 3 -b 127.0.0.1:8080 project.wsgi:application`(-w INT 开多个进程， -b ADDRESS)
 - 静态文件收集管理 `python manage.py collectstatic --noinput`(-l 软连接 --noinput 无需确认)
3. ~~Supervisor, 进程守护工具(Python 2.x编写)~~
4. Circus, 进程管理工具(Python3)
 - 安装(需退出虚拟环境) `pip install circus`
 - 添加配置文件 `circus.ini`
 - 启动 `circusd circus.ini` (后台参数 --daemon)
  
```
# circus.ini :

[watcher:growth_studio]
cmd = gunicorn --workers=2 --bind unix:/tmp/growth-studio.sock 
growth_studio.wsgi:application
working_dir = /home/myproject/growth-studio
copy_env = True
virtualenv = /home/myproject/venv
send_hup = True
```

nginx配合Circus和gunicor[配置方法](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html#configure-nginx-for-your-site)

> python使用django的collectstatic 方式收集静态文件需要注意的是settings下的STATIC_ROOT使用当前路径的情况，如果在/root/目录下，nginx设置的/static/在网页端会显示403 forbidden，权限问题，需要修改为非/root/目录才可正常显示，或在头部添加nginx配置文件添加use root;也可解决。


![supervisord配置方法](http://pbn1d3gdg.bkt.clouddn.com/supervisord%E9%85%8D%E7%BD%AE.png)
![Circus配置方法](http://pbn1d3gdg.bkt.clouddn.com/Circus%E9%83%A8%E7%BD%B2.png)



**开机启动web应用**：

使用`Upstart`替代传统init系统初始化程序。

```
# etc/init/circus.conf

description "circusd"
start on filesystem and net-device-up IFACE=lo
stop on runlevel [016]
exec /usr/local/bin/circusd /etc/circus/circusd.ini
```

`stat on`表示服务运行的时机：在文件系统和本地回环IP网络已经准备就绪后再执行。`stop on`说明服务将会在运行级别0、1、6（关机、无网络、重启）时停止。最后的`exec`才是我们的运行脚本。



**部署检查清单**：

部署工具检查使用[Deployment checklist](https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/) :
检测 `python manage.py check --deploy`
- 必须设置正确的安全级别
- 为不同的环境创建不同的配置
- 允许额外的安全功能
- 允许性能优化
- 提交错误报告

*关于HTTPS使用设置*(不适用不开启)：

1.COOKIE设置：

  ESSION_COOKIE_SECURE = True;

  CSRF_COOKIE_SECURE = True;

  CSRF_COOKIE_HTTPONLY= True;

2.安全设置：

  SECURE_HSTS_SECONDS = True;

  SECURE_SSL_REDIRECT = True;

  SECURE_CONTENT_TYPE_NOSNIFF = True;

  SECURE_BROWSER_XSS_FILTER = True;

  SECURE_HSTS_INCLUDE_SUBDOMAINS = True;


*deploy需注意危险内容*：
- 关闭调试模式。DEBUG=False
- 设置加密密钥，SECRET_KEY。重新生成

※ALOWED_HOSTS只有列表中的host才能访问，用于限定请求的host值，以防黑客构造包来发送请求。如ALLOWED_HOSTS = ['127.0.0.1']，如不限制为['*']

**配置管理**：

部署服务器有许多的配置文件内容是相互依赖的，如Gunicorn与Nginx、Nginx与Web应用的Static等。因此，我们需要使用版本控制来管理这些配置文件。可考虑用Git，但须考虑密钥、Token等内容的安全。
不同的环境里使用不同点的配置文件方法，可在代码库内为开发环境创建一个配置文件，在额外的安全环境里创建额外的配置文件，之后，在settings.py内引入。如下：
```
try
    from .local_settings import *
except ImportError as e:
    pass
```

而local_settings.py文件内可配置本地开发环境，在产品环境下配置不同项即可，保证便利和安全性。


## 自动化部署
可用框架：`Ansible、Fabric、SaltStack`
**基础设施即代码**,它是一种通过代码来定义计算和网络基础设施的方法，它可以应用于任何软件系统中。因对部署代码考虑：
- 使用描述文件
- 自文档化的系统和过程
- 版本化所有的代码
- 持续地测试系统和过程
- 小步前进
- 保证服务持续可用

现有配置改进：
- 将配置文件存放在项目代码里
- 使用Fabric来编写制动化脚本
- 更新配置都有相应的任务
- 每次修改配置应该做一次提交
- 考虑在测试环境时，使用UI自动化测试来测试部署脚本
- 对于大型的系统，采用蓝绿部署

**Fabric自动化部署**：

完成应用与环境的隔离，部署主要步骤：
- 安装应用运行的基础软件
- 下载指定版本的Web应用包
- 完成Web应用的初始化操作
- 复制Nginx、Circus配置文件
- 启动Nginx和Circus

※在远程服务器下执行命令，需要使用run函数`from fabric.api import run`，并可以导入env函数`from fabric.api import env`传入对应信息`env.hosts,env.user,env.password`(多个信息使用列表)达到自动登陆的效果。

**运行环境搭建**：

主要用到`fabric.api`下的sudo、run函数。
- 安装相应的Ubantu软件，如git、python3-pip、nginx等
- 安装virtualenv软件，并使用该软件来创建虚拟环境
- 安装circus
- 删除默认的Nginx配置

**编写自动化部署脚本**：

依据*自文档化的系统和过程*原则，用代码来标示文档，下面为手动部署过程的重构，完善对应代码即可。

```
app_path = "~"
@task
def deploy(version):
    """depoly app to cloud"""
    with cd(app_path):
        get_app(version)
        setup_app(version)
        config_app()
        
    nginx_config()
    nginx_enable_site('growth-studio.conf')
    
    circus_config()
    circus_upstart_config()
    
    circus_start()
    nginx_restart()
```

>with设置当前工作环境的上下文，如上面的cd(app_path)表示下面执行的每个脚本都在这个路径下执行。
>prefix设置命令执行的前缀，则每次都在执行run函数之前，先执行一次激活虚拟环境的操作。

其他方式：
1. [Ansible](http://www.ansible.com.cn/),使用方式为编写一个名为playbook的领域特定语言配置。编完脚本后，配置hosts以及Ansible配置文件ansible.cfg，执行如下命令即可安装`ansible-playbook playbook.yml --ask-become-pass`
2. Docker,一个基于操作系统的虚拟机，但性能和在正常服务器上运行相差无几。


**隔离与运行环境**：

确保运行环境独立使用的方法：
1. 隔离硬件：虚拟机
2. 隔离操作系统：容器虚拟化
3. 隔离底层：应用容器
4. 隔离依赖版本：虚拟环境
5. 隔离运行环境：语言虚拟机
6. 隔离语言：DSL


## 数据分析和性能优化

**数据分析**：
完成整个数据分析过程，需要的步骤：
- 识别需求
- 收集数据
- 存储数据
- 分析数据
- 展示数据

实用工具介绍：
- 使用Google Analytics/Piwik(基于PHP和MySQL)对网站流量进行统计
- 使用自定义的事件来追踪一些关键用户行为
- 分析网站的流量来源、受众概览、转化率

※开源日志管理方案Elasticsearch+Logstash+Kibana,Spark,Flume

**性能分析及优化**：
- PageSpeed、YSlow可以帮助改善网页速度
- New Relic可以帮助分析应用中的瓶颈，进行有针对性优化
- 了解前端常用的一些优化技巧
- 使用APM来对应用的瓶颈进行分析、优化
- 应用缓存来优化应用的性能

1. 使用PageSpeed Insights进行分析
Google的PageSpeed Insights分析工具有[网页版](https://developers.google.com/speed/pagespeed/insights/?hl=zh-CN)和插件版，推荐使用插件版不会受限于网络的影响。

使用分数来衡量网页性能(不关注网络连接问题)：
- 首屏加载时间：从用户请求新页面到浏览器呈现首屏内容所用的时间。
- 完整的网页加载时间：从用户请求新网页到浏览器完全呈现网页所用的时间。

2. 常见网站性能优化策略
优化措施：
- 减少HTTP请求。合并JaveScript和CSS(需评估)，CSS Sprites(一个页面设计的所有零星图片都包含到一张大图中，)，拆分初始化负载(将JavaScript文件分成两部分：渲染页面必需和其他。异步加载)，划分主域(将资源划分的请求划分到几个不同的域上)。
- 页面内部优化:*尽快渲染出页面*。将CSS放在顶部，将JavaScript放在底部(单页面应用，JS放顶部)，压缩HTML。
- 启用缓存。后台优化，页面缓存。
- 减少下载量:*减少对服务器请求*。使用CDN，使用外部JavaScript和CSS，使用gzip压缩，缓存(添加Expires头、配置ETag)。
- 网络连接优化:*域名到服务器优化*。DNS域名解析加速，减少DNS查找，使用HTTP2来加载HTTPS请求。

>为了较少时间花费，可以使用一些成熟的方案，如PageSpeed的HTTP服务器模块。

3. 使用自动优化工具

Google提供的PageSpeed服务器模块可直接用于自动优化，支持Nginx、Apache、IIS服务器，只需在编译时加入这个模块。

安装PageSpeed: `sudo apt-get install build-essential zlib1g-dev libpcre3 libpcre3-dev unzip libssl-dev`
Nginx服务器模块[ngx_pagespeed](https://www.modpagespeed.com/doc/build_ngx_pagespeed_from_source)安装：`bash <(curl -f -L -sS https://ngxpagespeed.com/install) --nginx-version latest`(如curl: (60) server certificate verification failed. 可增加 -k 忽略验证。)之后增加自定义配置`--sbin-path=/usr/sbin/nginx --conf_path=/etc/nginx/nginx.conf --with-http_ssl_module` 随后配置Nginx[配置文件](https://www.modpagespeed.com/doc/configuration)。重启服务器即可。

3.1 后台优化：应用性能管理工具(APM)
了解性能瓶颈最好方法：查看程序中运行*时间最长*的部分。
性能管理工具分析应用的五个维度：
- 终端用户体验监控
- 应用运行时架构
- 用户自定义的事物分析
- 应用组件监控
- 报告及应用数据分析

应用性能指数(Apdex)，定义了应用程序响应的最优时间T，同时定义了三种不同的性能表现。
- 满意：应用响应时间低于或等于目标时间(T秒)
- 可容忍：响应滞后，响应时间大于目标时间(T秒)
- 挫折：响应时间大于*四倍的目标时间(T秒)*

使用[New Relic](https://newrelic.com/)进行优化

登陆生成：`license key`

安装：`pip install newrelic`

使用Key生产配置文件：`newrelic-admin generate-config <your-key-goes-here> newrelic.ini`

设置环境变量，启动：`export NEW_RELIC_CONFIG_FILE=newrelic.ini`,`newrelic-admin run-program YOUR_COMMAND_OPTIONS`

设置好后等待几分钟可进入后台查看性能情况。

3.2 缓存

采用一些策略加速用户打开网页的速度。

**浏览器缓存**：静态资源缓存。可通过设置HTTP头的Cache-Control、Expires、Last-Modified/ETag等字段。

**应用缓存**：缓存数据库查询结果，磁盘文件数据、某个耗时的计算操作。
- [Memcached](https://docs.djangoproject.com/en/1.7/topics/cache/)，基于内存的缓存服务，位于应用层与数据库之间，可减少数据库读取负担，提供更快的读取速度。以上只需装好Memcached和python-memcached，然后在settings.py添加相关配置。
- 数据库缓存
- 文件缓存
- 本地内存缓存
- View缓存(不易控制)
```
# 页面缓存15s
@cache_page(60*15)
def blog_list(request):
    return render_to_response('blog/list.html'，{'blogs': Blog.objects.all()})
```
- 模板系统缓存
```
# 缓存时间600s，缓存名字blogcache
{％ load cache ％}

{％ cache 600 blogcache ％}
{％ for blog in blogs ％}
＜div class="col-sm-4"＞
＜h2＞＜a href="{{ blog.get_absolute_url }}"＞{{ blog.title }}＜/a＞＜/h2＞
    {{blog.body | slice:":80"}}
    {{blog.posted}} - By {{blog.author}}
＜/div＞
{％ endfor ％}
{％ endcache ％}
```
- 缓存API(只需对特别数据结果缓存时，可采用)

**缓存服务器**：运行在浏览器与原始服务器之间，可降低服务器负载。常见缓存服务器有：Varnish、Squid，HTTP服务器也可使用第三方模块扩展。


# 持续集成与持续交付

开发流程一般有开发环境、产品环境、测试环境(testing)、模拟环境(staging)。持续交付就是不断地生产出来，经过工人测试，测试合格后打包、发布。

**持续集成工具Jenkins**：

持续集成是当我们提交代码后，就自动按照设计的构建流程：执行CheckStyle、执行单元测试、执行功能测试等，通过它帮助找到代码中的问题。有以下关键因素：
- 版本管理工具
- 持续集成服务器
- 测试环境

为了保证持续集成的功能，需做到以下一系列实践：
- 维护同一个代码源
- 自动化构建
- 支持自动化测试
- 频繁提交代码，一天应该要提交一次，到多次。
- 每次提交都应该执行构建
- 让构建尽可能快
- 拥有接近产品环境的测试环境
- 团队成员可以轻松访问
- 团队成员都可以看到构建结果
- 支持自动化部署

**工具选择与Pipeline设计**：

持续集成服务器是一个运行着持续集成工具的服务器，由两部分组成：
- 主服务器(Master)：用于管理持续集成服务器、节点服务器、工具插件、设计流水线等。
- 从服务器(Slave)：用于运行流水线、返回运行结果等，接收Master分配和管理。

**持续集成工具**：

Jenkins开源，Bamboo收费，GO-CD(更适合复杂一些流程)，持续集成工具包含下列功能；
- 源代码控制系统
- 依赖管理工具
- 支持各种类型的测试
- 可以使用插件来扩展系统
- 支持流水线(Pipeline)
- 可视化结果

Jenkins Pipeline设计步骤：
- 签出代码
- 创建虚拟环境
- 搭建运行环境
- 执行单元测试
- 执行功能测试
- 部署应用(一般情况为部署到开发、测试环境)

一个好的Pipeline应具备以下特点：
- 适应能力强：可对住服务器重启。
- 可暂停：可等待开发人员输入或批准。
- 高效：可从已保存的检查点重新运行。
- 可视化：可提供仪表盘，并包含构建趋势。

在持续集成服务器上执行过程还需制定好一些规则，提交代码前，先在本地运行测试，测试未通过，或发现新Bug时，及时修复，如修复需时过长可考虑回滚代码。

**Jenkins搭建持续集成**：
1. 本地机器运行
- [官网](https://jenkins.io/)下载最新jenkins.war文件
- Java环境安装,Linux安装: `sudo apt-get install openjdk-8-jre`
- 运行：`java -jar jenkins.war`

2. 服务器安装
- 安装[方法](https://pkg.jenkins.io/debian/)，要确认Java版本
- 启动：`service jenkins start`
- 关闭：`service jenkins stop`
- 可选插件：Pipeline、BlueOcean(更好用户体验)

第一次'构建一个自由风格的软件项目'：
步骤如下：
- 配置源码管理，选择Git
- 创建构建触发条件，暂用Poll SCM，最好的选择是使用Build when a change is pushed to GitHub，当发生代码提交时，就会运行测试。因此，需要将服务器部署到外网，并与GitHub集成好。
- 按步骤创建shell脚本，选execute shell，如下。
- 添加构建完成的步骤
- 测试任务

*Poll SCM*：
使用五空格分隔值表示：分钟、小时、日期、月份、星期，对应如下：①分钟（0-59）②小时（0-23）③日期（1-31）④月份（1-12）⑤星期（0-6），可使用的特殊符号，"*"代表所有的取值范围内数字；"/"代表每的意思；"*/5"表示每5个单位；"-"代表从某个数字到某个数字；","分开几个离散的数字。例如：H/5 9-18 * * 1-5(工作日早9到晚6点每5分钟定时任务)

```
# 创建虚拟环境，激活并安装fabric3
# 可先填充下列Shell脚本，进行第一次测试使用
# 之后另建Ci文件夹，并push到github 之后可改为 sh './growth_studio/ci/setup.sh'
PATH=$WORKSPACE/py35env/bin:/usr/bin:$PATH
if [ ! -d "py35env" ]; then
      virtualenv --distribute -p /usr/local/bin/python3.5 py35env
fi
. py35env/bin/activate
pip3 install fabric3
```

可用fab 命令转化为不同的sh脚本，用于执行功能测试和单元测试。构建如：

```
# e2e.sh
. py35env/bin/activate
fab e2e
```

当我们使用独立的脚本时，就可以独立于持续集成工具，很容易切换到其他工具里。


**使用Jenkinsfile简化流程**：

[Jenkinsfile](https://jenkins.io/doc/book/pipeline/jenkinsfile/)是基于Groovy的DSL来定义作业的，是一个包含Pipeline脚本的容器，它详细说明了执行Jenkins作业所需要的特定步骤。

脚本式Pipeline使用`node`和`stage`定义构建流程。`node`用于为Jenkins住服务器指明持续集成的节点；`stage`是任务在执行时在逻辑上不同的步骤。执行步骤可每一步由一个简单的脚本构成，这样的好处在于，即使切换了不同的集成工具，也可以顺利地执行代码。

> 如使用`sh "./ci/test.sh"`构建途中遇到`.sh: Premission denied.`可使用`sh "bash ./ci/test.sh"`方式解决。

> Django IOError: No translation files found for default language zh-cn.检查/usr/local/lib/python3.5/dist-packages/django/conf/locale/下支持语言文件。


## 持续交付与持续部署

持续交付与持续部署的区别：持续交付中的部署是手动控制的、可选定版本的自动部署到产品环境，而持续部署则是完全自动部署到产品环境。

![持续部署](http://pbn1d3gdg.bkt.clouddn.com/%E6%8C%81%E7%BB%AD%E4%BA%A4%E4%BB%98.png)

**持续交付**：

从提交代码到自动发布软件的过程，在任何时候的修改都是可以在任何时候部署的。

1. 基于Jenkins与GitHub的自动发布

GitHub发布版本：
```
# 发布新版本
$ git tag v0.0.1
$ git push origin v0.0.1

# 撤销版本
$ git origin :refs/tags/v0.0.1
$ git push origin --tags
```

关于软件版本命名规则：主版本号.次版本号.修订号或者构建版本号。
- 主版本号：修改意味着重大修改，新的版本可能已经不兼容旧的API
- 次版本号：添加了新的功能
- 修订号：表示一些小的日常修改

其他方式是可以使用敏捷及迭代号进行事物管理，这里推荐版本做法是**迭代号.构建号**的命名方式。每个迭代结束时，我们都会发布一次。如迭代10，持续集成的软件版本号是100，则发布为10.100

持续集成工具在构建时，都会有对应的版本号，我们只需取出参数，同时迭代开发修改迭代号，就可实现版本软件管理。在Jenkins李，可以获取到一个BUILD_NUMBER的环境变量，这个环境变量就是当前构建号，只需在打标签时加上版本号即可，因，无法在shell脚本中获取相关的环境变量，因此添加到Jenkinsfile中，如：

```
stage('Release'){
  sh "git tag 'v1.${env.BUILD_NUMBER}'"
  sh "git push origin 'v1.${env.BUILD_NUMBER}'"
}
```

同样，Deploy发布版本也可进行更改，保证每次获取最新版本号：

```
stage('Deploy'){
  sh ". py35env/bin/activate"
  sh "fab deploy:'v1.${env.BUILD_NUMBER}'"
}
```

2. 验收测试

验收测试是以功能的角度对代码进行测试，集成测试专注于测试系统的集成。实际，这种测试和本地运行的集成测试相似，可以考虑直接使用———除了使用不同参数和测试连接。之前使用的是本地地址，对服务器测试时修改为服务器地址`self.selenium.get('http://10.211.55.2')`，同时其他方面也会有点区别，如下创建用户，还需准备好一份额外的数据库环境进行测试。

```
# 创建超级用户
@task
def prepare_ac():
    run('echo "from django.contrib.auth.models import User; User.objects.create_superuser(%s, %s, %s)" | python manage.py shell' % ('test', 'test@phodal.com', 'test'))
```

流程：单元测试完成后，运行集成测试，接着发布应用，然后部署，再运行验收测试。


**持续部署**：

完全自动化，从测试、打包、发布、部署等。

- 代码质量：编写测试的重要性，单元测试覆盖度要达到90%，且还要编写集成测试。
- 组织协同：康威定律
- 一些不足：操作系统配置，不同框架使用，数据库备份，蓝绿部署等。


## 移动Web与单页面应用

**单页面应用**：即Web应用运行一个页面集成了系统的大部分功能(JavaScript、CSS、HTML)，并提高了类似于桌面应用的用户体验。由JavaScript做主要交互，编写重心由后台转换到前台，也需要对后台进行扩展，以便拥有适合的API供前端调用。这样就需要掌握好前端技巧，还要懂设计后台API。

对采用移动Web版本与混合移动应用来构建产品的团队来说，会使用同样的技术栈来复用代码，如React和React Native，或者Angular及基于Angular的Ionic。

1. DOM与事件

DOM即文档对象模型，作为HTML和XML文档的编程接口而存在，且独立于平台，系统与语言。DOM是连接JavaScript和HTML的桥。

DOM是以节点树的形式而存在的，只需要知道这棵树一个叶子的存在，就能推导出整棵树。

![DOM树](http://pbn1d3gdg.bkt.clouddn.com/DOM%E6%A0%91.png)

在编写复杂的前端项目时，将会花费大量的时间在编写与DOM操作相关的功能。

2. 数据与模型

前端开发中所需要的数据都是通过API从后台获取的。通过Ajax请求(即通过XHR API)在浏览器的后台向服务器请求数据。当数据从服务器返回后，将根据数据的类型动态修改页面的内容。

为前台定义的模型应该会基于为后台定义的数据模型。后台定义的数据模型应该包含一个对象完整的字段，在前台去显示、获取相关的数据时，只关注所需要的字段。

3. 控制器与状态

当执行操作、获取数据后，需要让页面的内容做出相应的变化，这是需要控制器来进行处理。还需知道的一些概念：
- 单项绑定，数据只能从控制器向页面流动
- 双向绑定，数据的变更能及时显示到界面，界面上相应的操作也能变更到模型。更适合处理表单，如登陆操作。

4. 路由与页面

前端框架也有路由的概率，原理与后台MVC类似：使用对应的函数来处理对应的路由。不同点为，前端中的类MVC框架的路由变化中，不会发生实际的URL跳转，只会修改相应的URL，会切换控制器管理，以防混乱。

**API设计与框架选型**：

1. Web应用的API设计

API设计，在不同的业务模式下会有不同的API模式。

RESTful API即表述式状态转换，以资源的方式对API进行管理。它借助于HTTP1.1提出的四种HTTP方式(GET、POST、PUT、DELETE——RCUD）定义了一个规范，还需使用URI(统一资源定位符)定义好资源。表达资源的方式有两种：资源集合和单个资源。

RESTful架构风格的约束：

- 客户端。服务器分离，即划分客户端与服务端的职责，互不关心原则。
- 无状态，服务器不存储客户端请求的上下文信息。
- 可缓存，可提高应用性能。
- 统一接口
- 分层设计，用于提高系统各层次的独立性。
- 按需代码(可选)，允许对客户端的功能进行扩展。

2. JSON

JSON它的格式完全独立于语言，可用各种语言来解析，且现在已经作为后台与前端的数据交换标准。容易阅读，基于键值(Key-Value)的形式呈现。

3. 前端选型：单页面应用框架

- Angulaar 2，支持多平台构建，对后端人员写前端代码来说，是很好的选择。
- React，是一款JavaScript库，需搭配React Router、Redux才能完成应用开发。需学习一系列技术栈，学习成本较高。
- Vue，容易上手，更加灵活。

**移动应用**

需关注以下两点：

- 响应式设计，不同屏幕大小设计不同UI。
- 平台/设备特定代码，可调用一些原生插件提升用户体验，这些代码只在某个平台才运行。






















