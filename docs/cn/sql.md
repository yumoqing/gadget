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

## sor 方法

### C(tablename, ns)
向添加表中添加一条记录
#### 例子
```
db = DBPools()
async with db.sqlorContext(dbname) as sor:
	await sor.C(tablename, ns)
```
#### 参数说明

##### tablename
数据库表名称

##### ns
字典类型的数据，字典的key为自发段名，字典的value是字段值，至少表主键和必须项要求数据

#### 返回值
无

### R(tablename, ns, filters=None)
按要求检索数据，支持分页数据检索和全部数据检索
#### 例子
```
db = DBPools()
ns = params_kw.copy()
async with db.sqlorContext(dbname) as sor:
	r = await sor.R(tablename, ns)
```

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
#### 例子
```
db = DBPools()
ns = params_kw.copy()
async with db.sqlorContext(dbname) as sor:
	await sor.U(tablename, ns)
```
#### 参数说明

##### tablename
数据表名
##### ns
字典类型的数据，字典的key为自发段名，字典的value是字段值，至少表主键和必须项要求数据
#### 返回值
无

### D(tablename, ns)
删除数据记录，ns中的keys必须包含数据表的primary字段，按照primary字段数据删除数据表记录
#### 例子
```
db = DBPools()
ns = params_kw.copy()
async with db.sqlorContext(dbname) as sor:
	await sor.D(tablename, ns)
```
#### 参数说明

##### tablename
数据表名
##### ns
字典类型的数据，字典的key为自发段名，字典的value是字段值，至少表主键数据
#### 返回值
无

### tables()

### I(tablename)
获得表的建表信息
#### 例子
```
db = DBPools()
async with db.sqlorContext(dbname) as sor:
	r = await sor.I(tablename)
```

#### 参数说明
##### tablename
数据表名

### 返回值
如果数据表不存在，返回None，否则返回字典类型，

返回值例子
```
{
    "summary": [
        {
            "name": "user",
            "title": "\u7528\u6237\u89d2\u8272",
            "primary": [
                "id",
                "id"
            ]
        }
    ],
    "fields": [
        {
            "name": "id",
            "type": "str",
            "length": 32,
            "dec": null,
            "nullable": "no",
            "title": "\u7528\u6237id",
            "table_name": "user"
        },
        {
            "name": "userid",
            "type": "str",
            "length": 32,
            "dec": null,
            "nullable": "yes",
            "title": "\u7528\u6237id",
            "table_name": "user"
        },
        {
            "name": "rolerd",
            "type": "str",
            "length": 32,
            "dec": null,
            "nullable": "yes",
            "title": "\u89d2\u8272id",
            "table_name": "user"
        }
    ],
    "indexes": []
}
```

### sqlExe(sql,ns)
执行SQL语句
#### 例子
```
db = DBPools()
sql = "select * from mytable id=${id} country=${country}"
ns = params_kw.copy()
async with db.sqlorContext(dbname) as sor:
	r = await sor.sqlExe(sql, ns)
```
sql中支持使用参数，sqlor使用$[x}$引用变量，sql中的变量需要在ns中能够找到

#### 参数说明
##### sql
字符串， 一个合法的sql语句字符串，支持变量，变量用${x}$格式引用ns中的属性.

##### ns
sql语句所需参数字典，如果在ns中找不到sql中引用的变量，将出错

#### 返回值
如果是“select” 语句，返回数组变量，包含所有找到的数据记录
其他类型的sql执行结果没有定义

如果出错，返回None

### sqlPaging(sql, ns)
执行sql，并分页返回数据

#### 例子
```
db = DBPools()
sql = "select * from mytable id=${id} country=${country}"
ns = params_kw.copy()
async with db.sqlorContext(dbname) as sor:
	r = await sor.sqlPaging(sql, ns)
```

#### 参数说明
##### sql
字符串， 一个合法的sql语句字符串，支持变量，变量用${x}$格式引用ns中的属性.

##### ns
ns中必须包含一个sort属性，说明sql结果数据的排序字段，如果不指定，函数将出错，page参数如果不存在，自动设置为1

##### 返回值
如果sql是一个select语句，返回如下结构数据
```
{
	"total":总记录数
	"rows":[一页的数据]
}
```

