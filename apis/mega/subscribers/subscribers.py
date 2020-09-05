# -*- coding: utf-8 -*-

# from qav5. http import api, BaseClient
from qav5.http.client import  BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class SubscribersClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/subscribers/blocked_ip_list",method="get",is_json_req=False)
    def blocked_ip_list(self,ip=None, unlock=None,lock_at_max=None,lock_at_min=None,page=None,per_page=None):
        """
        被锁IP列表
        :param ip:
        :param unlock:
        :param lock_at_max:
        :param lock_at_min:
        :param page:
        :param per_page:
        :return:
        """
        pass

    @api(rule="/subscribers/unblocked_ip", is_json_req=True)
    def unblocked_ip(self,unlock_reason,customer_check,blocked_ip_id):
        """
        解锁IP
        :param unlock_reason:
        :param customer_check:
        :param blocked_ip_id:
        :return:
        """
        pass