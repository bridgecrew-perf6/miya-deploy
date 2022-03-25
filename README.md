# 使用tornado和redis构建任务系统，实现定时任务和异步任务．演示分布式定时任务．

在演示代码中， 每隔10秒启动hello函数.

在演示代码中，当调用长任务时，使用异步方式执行．

#环境需求

macOS 12.3

python 3.9

#安装项目依赖模块

``` 
下载安装包
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
$ chmod 755 Miniconda3-latest-MacOSX-x86_64.sh
$ ./Miniconda3-latest-MacOSX-x86_64.sh
创建环境
$ conda create -n miya-env39 python=3.9
进入环境
$ conda activate miya-env39
安装依赖
$ pip3 install -r requirements.txt
#退出环境
$ conda deactivate
```

#配置参数

配置项目中config.py文件

#开启web服务

/bin/bash run.sh

#开启celery的worker

/bin/bash run_worker.sh

#测试

1、在浏览器输入

curl -X GET http://127.0.0.1:9999

curl -X GET http://127.0.0.1:9999/long

2、在终端观察输出
