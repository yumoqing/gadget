# sqlor


sqlor为web应用提供数据库接口支持， 目前支持的数据库有：
* sqlite3
* mysql（mariadb）
* postgresql
* gauss
* oracle
* sql server

本模块支持异步DBAPI接口，目前测试过的有aiomysql， aiopg

## sqlor 优点

* 支持多种数据库
* 支持异步，减少了thread的开销
* 自动游标管理
* 自动事务管理

## 典型的应用模式
```
db = DBPools()
async with db.sqlorContext(dbname) as sor:
	await sor.C(tablename, ns)
```

## sor 方法

### C(tablename, ns)
向添加表中添加一条记录

#### 参数说明

##### tablename
数据库表名称

##### ns
字典类型的数据，字典的key为自发段名，字典的value是字段值，至少表主键和必须项要求数据

#### 返回值
无

### R(tablename, ns, filters=None)
按要求检索数据，支持分页数据检索和全部数据检索

#### 参数说明
##### tablename
数据表名
##### ns
字典数据，参数
##### filters
缺省为None， 无过滤对象
否则是一个字典类型的过滤定义对象
#### 返回值
* 当ns中没有page属性时，说明返回全部数据，返回数组类型的数据列表
* 当ns中有page属性时，返回
```
{
	"total":记录数,
	"rows":[一页的数据记录]
}
```
字典数据

### U(tablename, ns)
修改数据记录，ns中的keys必须包含数据表的primary字段，按照primary字段数据检索并修改数据记录
#### 参数说明
