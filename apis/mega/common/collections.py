# -*- coding: utf-8 -*-

from qav5.http.client import  BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class CommonClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/my/collections",method="GET")
    def get_collections(self):
        """get collections api
        :return:
        """
        pass

    @api(rule="/my/collections", is_json_req=True)
    def add_collections(self, router_name=None):
        """add collections api
        :param add_collections: 路由名
        :return:
        """
        pass

    @api(rule="/my/collections/<id>/",method="DELETE")
    def delete_collections(self,id):
        """delete collections api
        : param id :收藏id
        :return:
        """
        pass
        # return self._call_api(endpoint="/my/collections/:id/", req_kwargs=dict(json=id))
