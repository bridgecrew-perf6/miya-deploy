# 使用tornado和redis构建任务系统，实现定时任务和异步任务．演示分布式定时任务．

在演示代码中， 每隔10秒启动hello函数.

在演示代码中，当调用长任务时，使用异步方式执行．

#环境需求

macOS 12.3

python 3.9

#安装项目依赖模块

``` 
安装包
$ brew install virtualenv
创建环境
$ virtualenv --python=python3.9 ~/miya-env39
进入环境
$ source ~/miya-env39/bin/activate 
安装依赖
$ pip3 install -r requirements.txt
#退出环境
$ deactivate
```

#配置参数

配置项目中config.py文件

#开启web服务

/bin/bash run_server.sh

#开启celery的worker

/bin/bash run_worker.sh

#测试

1、在浏览器输入

curl -X GET http://127.0.0.1:9999/hello

curl -X GET http://127.0.0.1:9999/long

curl -X GET http://127.0.0.1:9999/test

2、在终端观察输出
