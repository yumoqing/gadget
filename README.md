# gadget
a light wight web server base on aiohttp

## Dependent
* [ahserver](https://github.com/yumoqing/ahserver)
* [sqlor](https://github.com/yumoqing/sqlor) if you want to use database
* [apppublic](https://github.com/yumoqing/apppublic)

## Download
```
git clone git@github.com:yumoqing/gadget.git
```

## Configuration
please look [ahserver](https://github.com/yumoqing/ahserver) to learn how to configure 

### support https
under "website" in the conf/config.json file, identify ssl with "crtfile" and "keyfile" 
like this.
```
	"website":{
		"ssl":{
			"crtfile":"$[workdir]$/conf/www.bsppo.com.pem",
			"keyfile":"$[workdir]$/conf/www.bsppo.com.key"
		}
	}
```
### log configure
In the conf/config.json, need to config log, you need to identify "name", "levelname" and "logfile"


```
	"logger":{
		"name":"gadget",
		"levelname":"debug",
		"logfile":"$[workdir]$/logs/gadget.log"
	}
```
## Test
the test folder contains everything need for a base test.

please to go test folder and run
```
python ../src/gadget.py
```
