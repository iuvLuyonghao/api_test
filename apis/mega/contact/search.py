# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class SearchClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/sub_contacts/simple_search", is_json_req=True)
    def simple_search(self, province_id=None, city_id=None):
        """simple_search api
        :param province_id: 省份idlist
        :param city_id: 城市idlist
        :return:
        """
        pass

    @api(rule="/sub_contacts/search", is_json_req=True)
    def search(self, contact_name=None, salutation=None):
        """search api
        :param contact_name 联系人姓名
        :param salutation 联系人称呼
        :return:
        """
        pass

    @api(rule="/sub_contacts/list")
    def contacts_list(self, sub_firm_id: int):
        """联系人list
        :param sub_firm_id 公司ID
        """
