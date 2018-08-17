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