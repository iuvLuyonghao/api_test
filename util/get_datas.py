# -*- coding: utf-8 -*-

import jsonpath
import json
import logging
import os
import requests


def get_data(filepath, code):
    try:
        with open(filepath, 'r') as load_f:
            load_dict = json.load(load_f)
        par = "$" + code + "$"
        res = jsonpath.jsonpath(load_dict, '$..%s' % par)
        for child in res:
            if isinstance(child, dict):
                return child
    except FileNotFoundError:
        logging.error("文件不存在！")
    except TypeError:
        logging.error("错误的参数！")


def get_path(file):
    try:
        a = os.path.split(file)
        all_name = a[0].split("/")[-1] + "_data.json"
        path_list = a[0].split("/")
        index = path_list.index("apis")
        path_list.insert(index + 2, "data_template")
        path = "/".join(path_list[0:index + 3])
        data_path = os.path.join(path, all_name)
        logging.info(data_path)
        if os.path.exists(data_path):
            return data_path
    except ValueError:
        raise FileExistsError("文件%s或目录%s不存在"
                              % (all_name, "data_template"))


def get_net_data(itf_id):
    try:
        url = "http://rap2-api.rccchina.com/app/mock/data/%s?scope=request" % itf_id
        response = requests.get(url)
        return response.json()
    except requests.exceptions.ConnectionError:
        logging.error("Rap2服务连接异常")


def deal_with_json(response: dict):
    for k, v in response.items():
        if v == "":
            response[k] = None
    str_dic = json.dumps(response)
    str_dic.replace("None", "null")
    return json.dumps(str_dic)
