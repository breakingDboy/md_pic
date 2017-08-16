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
