
## ubuntu14.04下截图外链脚本
### 工具：bash xclip python python-pip 七牛空间的账号
- 以上软件没有的可以直接安装`$sudo apt-get install xclip`
- 申请七牛账号，完成个人身份验证以后可以开通一个10G的免费云存储。
- 在七牛密匙管理，获取自己的access key and secret key.
- 然后pip 安装七牛SDK。`$sudo pip install qiniu`


### 脚本代码：
python 上传路径图片，并获取外链地址
```Python
#!/usr/bin/env python
# encoding: utf-8

import os
import sys
from qiniu import Auth, put_file

access_key = '你的accese key' # AK
secret_key = '你的secret key' # SK
bucket_name = '你的七牛空间名' # 七牛空间名
q = Auth(access_key, secret_key)

def upload_qiniu(path):
    ''' upload file to qiniu'''
    dirname, filename = os.path.split(path)
    key = 'markdown/%s' % filename # upload to qiniu's markdown dir
    token = q.upload_token(bucket_name, key)
    ret, info = put_file(token, key, path)
    if ret != None and ret['key'] == key:
        return '你的默认外链网址/'+key
    else:
        return 0

print upload_qiniu(sys.argv[1])
```
shell 脚本：
```bash
#!/bin/bash

#获取当前系统时间作为文件名
picName=$(date +%s)
path=~/Pictures/$picName.png
#自由截屏并存储
gnome-screenshot -a -f $path
#运行python脚本上传至七牛空间，并且返回超链接到剪贴板
python upload_qiniu.py $path |xclip
#删除本地截图文件
rm $path
```
### 快捷键启动
- 在`全部设置-》键盘-》快捷键`中自定义快捷键，命令为启动该脚本的命令，例如`sh ~/md_pic.sh`
- 自定义一个习惯的快捷键。按下快捷键后，截屏，随后在剪贴板中就有了相应的图片外链。鼠标中键粘贴。
