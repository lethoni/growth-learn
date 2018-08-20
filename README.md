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
> PS: 如路径错误( selenium.common.exceptions.WebDriverException: Message: ‘ChromeDriver executable needs to be available in the path.)则配置chromedriver路径：`driver = webdriver.Chrome('/path/to/chromedriver')`

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
 - 行为测试（针对执行过程）(不仅测试提供的服务，也测试依赖第三方提供的服务)

 



