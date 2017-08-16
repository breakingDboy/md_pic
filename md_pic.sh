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
