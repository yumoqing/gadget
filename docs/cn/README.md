# gadget
一个python开发的基于aiohttp的异步应用服务器，集成了1）用户认证与权健，2）数据库操作，3）后台开发必须的包和函数

gadget支持多进程，或多主机部署（需安装redis），在nginx后面提供负载均衡，可按照业务需求动态扩展，提升系统处理能力。

功能拓展能力，提供两种扩展方法，gadget源码级扩展，或在工作目录的plugins目录下部署扩展的源码

gadget运行需要指定一个工作目录，在工作目录中需有以下文件或目录：
* conf目录 - 配置文件目录
* logs目录 - 日志文件目录
* plugins目录 - 扩展目录
* i18n目录 - 国际化支持
* files目录（可在conf/config.json文件中指定其他位置）
* wwwroot目录（可在conf/config.json文件中指定其他位置）

## 运行环境和依赖
* 操作系统支持Windows， MacOS， linux
* 数据库支持：sqlite3，mysql， mariadb， postgresql，sqlserver， oracle， teradata，华为的guass等（源码方式运行时需提供相应数据库的驱动包）
* python 3.7以上版本
* redis 当使用redis_storage时需要
* [apppublic](https://github.com/yumoqing/appPublic)
* [sqlor](https://github.com/yumoqing/sqlor)
* [ahserver](https://github.com/yumoqing/ahserver)
* [dataui](https://github.com/yumoqing/dataui)
* 以及apppublic， sqlor， ahserver和dataui包所依赖的包或模块

## 运行gadget
运行gadget的步骤
1 转到工作目录
2 gadget [ -p port ]

## 配置
gadget的配置信息需放在工作目录的conf/config.json文件中，有关配置相关内容请看[config.json](config.md)
## 模版
gadget支持jinja2模版，模版中可以使用gadget定义的所有模块，变量和函数

## 数据库操作
gadget为每个请求提供数据库操作， gadget不提供跨请求的数据库操作，请求中的数据库操作要么整体成功，要么整体失败，gadget使用[sqlor](https://github/yumoqing/sqlor)提供数据库支持。 请看[数据库操作说明](sql.md)

## 脚本
gadget支持在后台使用受限的python脚本，后缀为“.dspy”

## 用户认证和授权
gadget在缺少状态下不做用户认证和权健，要提供此功能需在plugins目录下放一个如下形式的脚本
```
# auth.py
from ahserver.auth_api import AuthAPI
from sqlor.dbpools import DBPools

async def checkUserPermission(self, user, path):
	“”“
	user：用户id，None代表没有登录
	path：访问目录， path等于URL（“http(s)://x.com/ll/ll”） 中的“/ll/ll"部分
	返回值：True，有权限
	       False，无权限
	如果返回False并且user为None，返回前端401，否则403
	”“”
	self.info(f'checkUserPermission():{user} access to {path} ..')
	# 这里做实际的判断，看看user是否有访问path的权限
	
	return True

AuthAPI.checkUserPermission = checkUserPermission
```

