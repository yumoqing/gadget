# DspyProcessor
dspy处理器处理受限py脚本，应用服务器规定了dspy脚本可以引用的模块，变量，和函数

## 环境
环境是dspy脚本可以引用的一个资源集合，gadget服务器给dspy脚本给定了一个特定的执行环境

dspy环境请参看[环境](environment.md)

## 返回
dspy 需要使用return 显式给应用服务器返回内容，
可以返回的数据类型有：
* dict
* array
* string
* RESPONSE 对象及其衍生对象


