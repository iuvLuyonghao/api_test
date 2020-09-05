# -*- coding: utf-8 -*-

from util.performance_tools.grpc_locust_client import GrpcUser
from locust import task, between


class BasicUser(GrpcUser):
    """
        压测任务类
        执行压测命令： locust -f  performance_tests/basic_services/demo.py -u 10 -r 3 --headless
        参数信息详见locust官方网站：https://docs.locust.io/en/latest/running-locust-without-web-ui.html
    """
    wait_time = between(2,
                        5)  # locust自带环境配置参数，详见 https://docs.locust.io/en/latest/api.html?highlight=between#locust

    # .wait_time.between

    @task  # task压测任务语法糖，可以task(n)设置权重，n越大，任务权重越高
    def test_batch_get_user(self):
        """获取未认证账号接口性能测试"""
        name = "未认证账号"  # 任务名称
        env = "account"  # 服务名称
        rule = "/person/search/batch_get_user"  # 服务path
        parms = {
            "person_user_ids": None,  # 参数
            "include_resign": None
        }
        self.client.connect(name=name, grpc_env=env, path=rule, my_data=parms)  # 调用重写后的connect方法，触发压测任务
