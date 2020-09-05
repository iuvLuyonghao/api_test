# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class ProjectClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/projects/stages", method="get", is_json_req=True)
    def project_stages(self):
        """
        取得项目阶段
        :return:
        """

    @api(rule="/projects/categories", method="get", is_json_req=True)
    def project_categories(self):
        """
        取得项目一级分类
        :return:
        """

    @api(rule="/projects/sub_categories", method="get", is_json_req=True)
    def project_sub_categories(self):
        """
        取得项目二级分类
        :return:
        """

    @api(rule="/projects/bid_categories", method="get", is_json_req=True)
    def project_bid_categories(self):
        """
        采购信息类别
        :return:
        """

    @api(rule="/projects/product_categories", method="get", is_json_req=True)
    def project_product_categories(self):
        """
        产品及服务类别
        :return:
        """