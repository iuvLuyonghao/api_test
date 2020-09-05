# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class IntendedCustomerFirmsClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)


    @api(rule='/price/intended_customer_firms/search')
    def intended_customer_firms_search(self, status):
       """

       :param status:
       :return:
       """
       pass


    @api(rule='/price/intended_customer_firms/count')
    def intended_customer_firms_count(self, branch_office_ids,leader_ids,leads_type_id):
        """
        意向公司统计
        :param branch_office_ids:
        :param leader_ids:
        :param leads_type_id:
        :return:
        """
        pass