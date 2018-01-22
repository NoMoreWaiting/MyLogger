# MyLogger
封装一个 python 日志库, 完善中...

目前直接使用 logger.py 文件, 使用时:
```
导入大小切割log
```
> from logger import sizeLog as log 
```
导入时间切割log
```
> from logger import timeLog as log

日志生成在上一级文件夹下 log 文件夹中.

还未详细的测试过, 慎用


以后再继续完善...

想增加的功能:
1. ok  日志分级输出 
2. ok  日志按大小分割 或者 按时间分割(可以选择)
3. 懒  可以从配置文件读取配置
4. 懒  打包
5. ok  日志可以输出调用信息, 堆栈消息. (远期目标). 现在可以打印调用函数所在的文件, 行号和函数名
