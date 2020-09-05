# -*- coding: utf-8 -*-

# from qav5. http import api, BaseClient
from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class ZoomClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/rcc_share/notice_rcc_reader", is_json_req=True)
    def notice_rcc_reader(self, employee_id: int, join_url: str, sub_contact_id: int):
        """

        @param employee_id:
        @param join_url:
        @param sub_contact_id:
        """
        pass
