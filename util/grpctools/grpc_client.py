# -*- coding: utf-8 -*-

'''
@Time    : 2020-04-09
@Author  : Dean
@Mail    : dean.qian@rccchina.com
'''

import grpc
import json
import logging
from util.grpctools import call_pb2, call_pb2_grpc
from functools import wraps
from config import gRpcSever, environment
from qav5.http import smart_payload
from util import get_datas
import sys

logger = logging.getLogger(__name__)
system = sys.platform


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def dict_to_object(dict_objct):
    if not isinstance(dict_objct, dict):
        return dict_objct
    instance = Dict()
    for k, v in dict_objct.items():
        instance[k] = dict_to_object(v)
    return instance


def run(grpc_env, path, my_data):
    try:
        with grpc.insecure_channel(grpc_env) as channel:
            stub = call_pb2_grpc.SrvStub(channel)  # 调用 grpc 服务
            response = stub.Call(call_pb2.Req(path=path, params=json.dumps(my_data)))
            rep = opr_code(response)
            if system == "darwin" or system == "linux":
                logger.info(rep)
            else:
                print(rep)
            return rep
    except AttributeError:
        logging.error("连接服务器失败，请检查错误:"
                      "1，检查config中服务地址是否正确；"
                      "2，检查api中grpc_server_name是否设置正确；"
                      "3，检查服务器是否可用；")


def opr_code(response):
    d_dic = json.loads(response.data.decode("utf-8"))
    dict_rep = {"code": response.code,
                "message": response.message,
                "data": d_dic
                }
    j_object = (dict_to_object(dict_rep))
    return j_object


def grpc_api(grpc_server_name, rule, dic_name=None, itf_id=None, file_path=None):
    """
    @param file_path:
    @param itf_id: Rap2中itf_id，目前rap2上很多mock的数据其实不可用或不准确，不推荐使用此方法
    @param grpc_server_name: 当前服务的名称，用于获取env地址
    @param rule: api路由地址
    @param dic_name: 使用该参数时，只需要写上必填参数和**kwargs，如果加上此参数，则取data_template中接口数据，
    例如：
        文件中：
            {"$account_search$": {
            "mobile": null,}}
        使用时：
            @grpc_api(rule="/in_crm_search", grpc_server_name=grpc_server_name, dic_name="account_search")
    @return: function run
    """

    def wrapper(fun):
        @wraps(fun)
        def _wrapper(self, *fargs, **fkwargs):
            genv = get_env(grpc_server_name)
            if dic_name:
                if file_path:
                    path = get_datas.get_path(file_path)  # 复用grpc_server_name，因为json命名方式以当前服务名称命名，与获取env一致
                    my_data = get_datas.get_data(path, dic_name)
                    data = smart_payload(fun)(self, *fargs, **fkwargs)
                    my_data.update(data)
                else:
                    raise FileNotFoundError("使用dic_name的同时需要传参数file_path=__file__")
            elif itf_id:
                my_data = get_datas.get_net_data(itf_id)
                data = smart_payload(fun)(self, **fkwargs)
                my_data.update(data)
            else:
                my_data = smart_payload(fun)(self, *fargs, **fkwargs)
            logging.info(my_data)
            return run(genv, rule, my_data)

        return _wrapper

    return wrapper


def get_env(grpc_server_name: str):
    if environment:
        if hasattr(gRpcSever, 'env_%s' % environment):
            genv = eval(("gRpcSever.env_%s.get('%s')" % (environment, grpc_server_name)))
            return genv
