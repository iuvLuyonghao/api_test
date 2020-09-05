#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
class MyEncoder(json.JSONEncoder):
    """解码类，json转换时遇见byte强制转换str"""
    """使用方法：json.dumps(data,cls=MyEncoder,indent=4)"""
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)
