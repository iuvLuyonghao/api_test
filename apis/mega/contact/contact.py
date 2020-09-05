# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class ContactClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/base_options/contact_departments_positions",method="get")
    def contact_departments_positions(self):
        """contact_departments_positions api
        :param province_id: 省份idlist
        :param city_id: 城市idlist
        :return:
        """
        pass

    @api(rule="/sub_contacts/options",method="get",is_json_req=True)
    def options(self,options:list=None,sub_firm_id:str=None):
        """新建联系人选项
        :param options: 选项列表
        :param sub_firm_id: 公司id
        :return:
        """
        pass

    @api(rule="/sub_contacts/set_resign",is_json_req=True)
    def set_resign(self,sub_contact_id:str=None,resign:str=None):
        """设置联系人离职
        :param sub_contact_id: 联系人id
        :param resign:设置离职固定为1
        :return:
        """
        pass


