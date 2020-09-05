# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class JurisdictionClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/base/tree",method="get")
    def tree(self):
        """组织架构数据
        :return:
        """
        pass

    @api(rule="/base/right_roles",method="get",is_json_req=True)
    def right_roles(self,job_title_id:int):
        """职位对应的权限
        :param job_title_id :职位id
        :return:
        """
        pass

    @api(rule="/base/right_roles",is_json_req=True)
    def right_roles_connect(self,job_title_id:int,role_ids:list):
        """职位关联角色
        :param job_title_id :职位id
        :param role_ids:角色的id数组
        :return:
        """
        pass
