# -*- coding: utf-8 -*-

import sys
import os
import pytest
import argparse
import config
from data import DataCenter, load_framework_data
from os.path import isdir, join
from const import Framework
from _pytest.mark import MarkDecorator


def list_dirs(path):
    """列出path目录下的文件夹"""
    ret = []
    for ele in os.listdir(path):
        p = ele if path == "." else join(path, ele)
        if isdir(p) and not ele.startswith(".") and not ele.startswith("_"):
            ret.append(p)
    return ret


def ignores(parent, *sub):
    """生成需要忽略的目录"""
    len_max = max([len(su) for su in sub])  # 路径深度
    for i in range(len_max):
        dirs_v2 = set()  # 当前层级下的路径集合
        remove_list = set()  # 需要移出的路径
        for su in sub:
            if i + 1 <= len(su):
                dirs_v2 = dirs_v2 | set(list_dirs(join(parent, *su[:i])))
                remove_list.add(join(parent, *su[:i + 1]))
        for remove_path in remove_list:
            try:
                dirs_v2.remove(remove_path)
            except KeyError as e:
                raise KeyError("check your path: %s" % e)
        yield dirs_v2


def dpath_to_lists(dpath):
    """将目录字符串转换成list对象"""
    return list(map(lambda s: s.strip().strip("/").split("/"), dpath.split(",")))


parser = argparse.ArgumentParser()
parser.add_argument("--env", dest="env", action="store", default=config.environment, type=str,
                    help="用于指定不同的测试环境")
parser.add_argument("--data-file", dest="datafile", action="store", type=str,
                    help="用于指定加载额外的测试数据文件,将会覆盖默认的测试数据")
parser.add_argument("--suites", dest="suites", action="store", type=str,
                    help="用于指定执行哪些目录下的用例（可包含子目录），多个目录用`,`分割, eg: --suites app,infrastructure")
parser.add_argument("--tag", dest="tag", action="store_true", help="打印已知的用例tag")

args, other_args = parser.parse_known_args()

if args.tag:
    print("{:16} \t{}".format("Tag", "Remark"))
    print("=" * 36)
    for key, value in args.tag.__dict__.items():
        if not isinstance(value, MarkDecorator):
            continue
        print("{:16} \t{}".format(value.markname, value.mark.kwargs.get("help", "没有备注")))
    print("")
    print("usage: runsuite.py -m smoke -m clearance")
    sys.exit(0)

if args.env != config.environment:  # 设置测试环境
    config.environment = args.env
    DataCenter.reset()
    load_framework_data()

if args.datafile:  # 加载自定义的测试数据文件,格式请参考data/*.json
    DataCenter.reset()
    load_framework_data(args.datafile)

sys.argv = [sys.argv[0]]
sys.argv.extend(other_args)

if args.suites:
    for d in args.suites.split(","):
        sys.argv.append(os.path.join(Framework.CASE_DIR, *d.strip().strip("/").split("/")))

exit(pytest.main())
