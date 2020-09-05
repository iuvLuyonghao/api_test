# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class EmpowersClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/empowers/approve_users", method="get")
    def approve_users(self, sub_firm_id):
        """
        公司的可审批的人
        :param sub_firm_id:公司id
        :return:
        """
        pass

    @api(rule="/empowers", is_json_req=True)
    def empowers(self, operate_type,firm_part_ids,sub_firm_id,employee_id=None,notes=None):
        """
        申请授权/ 主动授权
        :param operate_type:操作， 申请授权 1 主动授权： 2
        :param firm_part_ids:勾选的权限模块
        :param sub_firm_id:公司
        :param employee_id:员工ID，如果是特殊人可以不传
        :param notes:备注/ 申请原因
        :return:
        """
        pass

    @api(rule="/empowers/firm_parts", method="get")
    def firm_parts(self):
        """
        公司可以授权的模块
        :return:
        """
        pass

    @api(rule="/empowers/empower_users", method="get")
    def empower_users(self):
        """
        公司可以授权的人
        :return:
        """
        pass
