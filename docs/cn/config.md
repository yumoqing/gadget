# 

## 宏
使用$[x]$来引用宏，目前config.json文件中支持两个宏
### workdir
工作目录，gadget程序启动时的目录
### ProgramPath
gadget程序所在目录

例子
```
    "logger":{
        "name":"iptvserver",
        "levelname":"debug",
        "logfile":"$[workdir]$/logs/iptv.log"
    }
```
上述例子定义了logfile为工作目录下的logs/iptv.log

## logger
定义日志

例子
```
    "logger":{
        "name":"iptvserver",
        "levelname":"debug",
        "logfile":"$[workdir]$/logs/iptv.log"
    },  
```
### name
日志名称
### levelname
日志级别名称
* debug
* info
* error
### logfile
日志文件路径

## databases
字典类型，每个key定义一个数据库定义， 支持链接多个数据库，可以同时定义多个不同类型的数据库

例子
```
	“databases”:{
        "kboss":{
            "driver":"aiomysql",
            "async_mode":true,
            "coding":"utf8",
            "dbname":"kboss",
            "maxconn":100,
            "kwargs":{
                "user":"test",
                "db":"kboss",
                "password":"QUZVcXg5V1p1STMybG5Ia6mX9D0v7+g=",
                "host":"localhost"
            }
        }
	}

```
上述定义了一个名为“kboss”的数据库，使用aiomysql“模块操作数据库
异步模式
最大支持100个链接，链接参数等

## website
字典类型，定义website属性
### port
端口号

### host
定义网站主机ip地址，通常设置为”0.0.0.0“， 内网外网都能访问

### ssl
定义网站使用https访问，格式如下
```
	"ssl":{
		"crtfile":证书绝对路径,
		"keyfile":证书密码文件绝对路径
	}
```

### coding
定义网站编码，建议使用”utf-8“编码

### processors
数组，定义文件后缀网站路由，每一个元素定义一个后缀

例子
```
        "processors":[
            [".proxy","proxy"],
            [".xlsxds","xlsxds"],
            [".sqlds","sqlds"],
            [".tmpl.js","tmpl"],
            [".tmpl.css","tmpl"],
            [".tmpl.html","tmpl"],
            [".bcrud", "bricks_crud"],
            [".tmpl","tmpl"],
            [".ui","tmpl"],
            [".dspy","dspy"],
            [".md","md"]

```
上述例子定义：
* .proxy 后缀的路径，使用ProxyProcessor来处理
* .xlsxds后缀的路径，使用XlsxdsProcessor处理器来处理
* .sqlds后缀的路径，采用SqldsProcessor处理器来处理
* .tmpl.js后缀的路径，使用TmplProcessor处理器来处理
* .tmpl.css后缀的路径，使用TmplProcessor处理器来处理
* .tmpl.html后缀的路径，使用TmplProcessor处理器来处理
* .bcrud后缀的路径，使用BricksCrudProcessor处理器来处理
* .tmpl后缀的路径，使用TmplProcessor处理器来处理
* .ui后缀的路径，使用TmplProcessor处理器来处理
* .dspy后缀的路径，使用DspyProcessor处理器来处理
* .md后缀的路径，使用MarkdownProcessor处理器来处理

### startswiths
数组类型，定义网站的前缀路由，前缀路由使用注册函数实现

例子
```
        "startswiths":[
            {
                "leading":"/public/publickey",
                "registerfunction":"getPublicKey"
            },
            {
                "leading":"/public/i18n",
                "registerfunction":"getI18nMapping"
            },
            {
                "leading":"/idfile",
                "registerfunction":"idFileDownload"
            },
            {
                "leading":"/thumb",
                "registerfunction":"makeThumb",
                "width":512,
                "quality":50,
                "keep_ratio":1
            }
        ],
```
上述定义了4个前缀路由，除“leading”，”registerfunction“外的属性均被当作参数传递给注册函数

### rsakey
支持rsa公开密钥加密，在这个属性下提供rsa的私钥和公钥
例子
```
        "rsakey":{
            "privatekey":"$[workdir]$/conf/rsa_private_key.pem",
            "publickey":"$[workdir]$/conf/rsa_public_key.pem"
        }

```

## 登录控制

在config.json文件对website属性下
### authpaths
authpaths是一个数组， 每个元素定义一个路径或路径的起始字符串，在authpaths中定义的路径，用户访问的URL的起始字符串与其相同时需要登录

例子1
```
	"authpaths":[
		"/"
	]
```
上面的例子整个网站都需要登录后才能访问，这种情况需要设置例外，放出登录界面让用户访问

例子2
```
	"authparhs":[
		"/scrent",
		"/private"
	]
```
以上例子定义了需要登录后才能访问的路径，所以以上述两个字符串开始的路径的访问都需要登录

### whitelist
白名单，数组，每项定义一个例外
例子1
```
	"whitelist":[
		"/login",
		"/login"
	]
```
以上例子将根目录下所有以“login”开始的路径都设置成例外，不用登录也可以访问

## langMapping
语言对照
不同的浏览器和操作系统，向后台船队的语言差异挺大，这里定义了一个映射

例子
```
    "langMapping":{
        "zh-Hans-CN":"zh-cn",
        "zh-CN":"zh-cn",
        "en-us":"en",
        "en-US":"en"
    }

```
