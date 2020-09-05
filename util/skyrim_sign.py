# -*- coding: utf-8 -*-

import hashlib
import time


def get_signature(params: dict, t):
    """新工外通用服务签名算法"""
    vars = params
    timestamp = t
    secret_key = 'fa1ed42387556e36e34bc7b3268974ef'
    _params_keys = '&'.join(sorted(vars.keys()))
    list = [secret_key, str(timestamp), _params_keys, secret_key]
    final_str = ('_').join(list)
    md5 = hashlib.md5()
    md5.update(final_str.encode('utf-8'))
    s = md5.hexdigest()
    return s


if __name__ == '__main__':
    dict = {'Name': 'Zara', 'Age': 7}
    t = int(time.time())
    dic = get_signature(dict, t)
    print(dic)
