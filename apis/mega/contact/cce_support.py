# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class CCESupportClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/base/cce_support_url",method="get")
    def cce_support_url(self, task_type="basic_training", contact_id=None, sub_firm_id=None):
        """
        提交助理系统任务
        :param task_type: basic_training 默认
        :param contact_id: 联系人ID
        :param sub_firm_id: 公司ID
        :return:
        """
        pass

