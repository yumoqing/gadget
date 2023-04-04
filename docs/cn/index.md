# gadget
一个python的应用服务器，需要在工作目录中有一下目录和文件

## 配置
gadget的配置信息需放在工作目录的conf/config.json文件中，有关配置相关内容请看[config.json](config.md)
## 模版
## 数据库操作
gadget为每个请求提供数据库操作， gadget不提供跨请求的数据库操作，请求中的数据库操作要么整体成功，要么整体失败，gadget使用[sqlor](https://github/yumoqing/sqlor)提供数据库支持。 请看[数据库操作说明](sql.md)

## 脚本
## 用户认证和授权
## 消息
