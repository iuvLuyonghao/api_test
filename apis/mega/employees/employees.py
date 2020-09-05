# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class EmployeesClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/rcc_auth/employees", is_json_req=True,method="get")
    def employees_auth(self, scope: str=None):
        """
        取得员工
        :param scope: all 全部 self 自己以及下属
        """
        pass

    @api(rule="/employees/<id>", is_json_req=True,method="get")
    def employees(self, id: int):
        """
        员工信息
        :param id: 员工id
        """
        pass
