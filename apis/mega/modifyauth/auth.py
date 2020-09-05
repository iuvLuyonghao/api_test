# -*- coding: utf-8 -*-

from qav5.http.client import  BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class AuthClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/base/right_roles", is_json_req=True)
    def right_roles(self, job_title_id:int,role_ids:list):
        """设置权限
        :param job_title_id: 职位id
        :param role_ids: 权限list
        :return:
        """
        pass
