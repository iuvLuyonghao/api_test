# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class AppusersClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/app_users/app_order_create_info", method="get", is_json_req=True)
    def app_order_create_info(self,order_id:int=None):
        """
        订单创建个人账号页信息
        :return:
        """

    def contract_upload_for_user(self, sub_firm_id, contract_file):
        """
        单个创建账号的合同文件
        :param contract_file: 合同文件
        :param sub_firm_id: 公司id
        :return:
        """
        return self._call_api("/app_users/contract_upload", method='POST',
                              req_kwargs=dict(data={"sub_firm_id": sub_firm_id},
                                              files=dict(contract_file=open(contract_file, 'rb'))),
                              disable_log=True)

    @api(rule="/app_users/setting", is_json_req=True)
    def app_users_setting(self,id):
        """
        账号编辑设置
        :param id: 个人账号id
        :return:
        """

    @api(rule="/app_users/set_allot_admin", is_json_req=True, remove_null=True)
    def set_allot_admin(self, app_user_ids, allot_admin):
        """
        设置分配管理员
        :param app_user_ids:个人账号IDs 的数组
        :param allot_admin:设置分配管理员,(0:否|1:是)
        :return:
        """
        pass
