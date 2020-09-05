# -*- coding: utf-8 -*-
import time
from util.grpctools.grpc_client import run, get_env
from locust import events, User


class GrpcClient(object):
    """重写self.client"""
    _locust_environment = None

    def connect(self, name, grpc_env, path, my_data):
        """重写connect方法"""

        start_time = int(time.time())
        try:
            # 记录开始时间
            env = get_env(grpc_env)
            res = run(env, path, my_data)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type='grpc',
                name=name,
                response_time=total_time,
                exception=e
            )
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(
                request_type='grpc',
                name=name,
                response_time=total_time,
                response_length=0
            )
        return res


class GrpcUser(User):
    abstract = True

    def __init__(self, *args, **kwargs):
        super(GrpcUser, self).__init__(*args, **kwargs)
        self.client = GrpcClient()
