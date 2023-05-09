# 环境
gadget服务器给处理器提供了一个执行环境，处理器可以引用环境提供的模块，变量，函数等资源来完成处理器等处理任务

## 请求相关环境

### request
服务器接收到的服务请求对象，具体内容请参考[AioHttp](https://github.com/aiohttp/aiohttp)

### params_kw
服务器接收到浏览器发送过来的参数，支持各种http（s）方法过来的数据

### get_user()
获得用户id, get_user（）是一个协程

#### 例子
```
uid = await get_user()
```
#### 返回值
null 或者当前登录用户id

### remember_user()
#### 例子
```
db = DBPools()
async with db.sqlorContext(dbname) as sor:
	pwd = password(params_kw.password)
	ns = {
		"password":pwd,
		"name":params_kw.get('name')
	}

	sql = "select * from users where name=${name}$ and password=${pwd}"
	x = await sor.sqlExe(sql, ns)
	if len(x) < 1:
		return Error(msg="user or password error")
	userid = x[0].['id']
	await remember_user(userid)
```
从前台接收用户名和密码，密码加密后从数据库检索符合名字和密码与参数重相同的用户记录，如果没有找到提示前提错误，否则用户登录成功，服务器记住登录用户的ID

#### 参数说明
##### userid
用户id

##### 返回值
无

### entire_url(url)
获得参数URL的绝对url

#### 例子
dspy
```
url = entire_url('insert.dspy')
```
template
```
{
	"widgettype":"urlwidget",
	"options":{
		"url":"{{entire_url('insert.dspy')}}"
	}
}
```
#### 参数说明
##### url
相对路径或绝对路径
可以上一下形式
* http://.....
* https://......
* /abc/lerltg.tmpl
* abc/gggg.html

##### 返回值
带http的路径

