# -*- coding: utf-8 -*-

import logging
import functools
import config
from os.path import abspath, join, dirname, splitext, isfile, split
from qav5.datastore import DataStore, DataFactory

try:
    import simplejson as json
except (ImportError, SyntaxError):
    import json

DataCenter = DataStore()
DataHelper = DataFactory(DataCenter)


def load_data(data_file):
    """从json文件中读取测试数据存储到DataCenter"""
    with open(data_file, encoding="utf-8") as f:
        content = json.load(f)

    for each in content['data']:
        DataHelper.create_data_inst(each)


def load_framework_data(data_file=None):
    """加载全局的测试数据"""
    if data_file is None:
        data_file = abspath(join(dirname(__file__), "{}.json".format(config.environment)))
    if not isfile(data_file):
        logging.root.warning("cannot found data file: {}".format(data_file))
        logging.root.warning("loading test.json")
        data_file = abspath(join(dirname(__file__), "test.json"))
    return load_data(data_file)


def load_local_data(data_file=None, py_file=None):
    """从用例目录加载额外的测试数据

    当传入py_file，用搜索py_file所在目录的json文件，优先搜索<pyFileName>_<env>.json文件，然后搜索<pyFileName>.json文件
    """
    if data_file:
        load_data(data_file)
    if py_file:
        prefix, postfix = splitext(abspath(py_file))
        file_with_env = "{}_{}.json".format(prefix, config.environment)
        file_without_env = "{}.json".format(prefix)
        if isfile(file_with_env):
            data_file = file_with_env
        elif isfile(file_without_env):
            data_file = file_without_env
        load_data(data_file)


def run_once(func):
    cached = {}

    @functools.wraps(func)
    def wrapper(pkg):
        if pkg in cached:
            return cached[pkg]
        ret = func(pkg)
        cached[pkg] = ret
        return ret

    return wrapper


@run_once
def _load_package_data(pkg):
    """pkg目录"""
    pkg_name = split(pkg)[1]
    path = join(pkg, pkg_name)
    data_file_with_env = "{}_{}.json".format(path, config.environment)
    data_file_without_env = "{}.json".format(path)
    if isfile(data_file_with_env):
        data_file = data_file_with_env
    else:
        data_file = data_file_without_env
    load_data(data_file)


def load_package_data(py_file):
    """从用例目录加载作用于该用例目录下的测试数据"""
    pkg = dirname(py_file)
    _load_package_data(pkg)
