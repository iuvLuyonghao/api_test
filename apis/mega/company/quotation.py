# -*- coding:utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class QuotationClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/sub_firms/<firm_id>/quotation/info", is_json_req=True)
    def quotation_a_info(self, token, firm_id=None):
        """报价方案书-页面基本信息
        :param token:
        :param firm_id:
        :return:
        """
        pass

    @api(rule="/sub_firms/<firm_id>/quotation/calculate", is_json_req=True)
    def quotation_calculate(self, token, user_options, firm_id=None):
        """报价方案书-处理方案信息
        :param firm_id:
        :param token: 初次访问生成，之后用此进行数据读取访问
        :param user_options: 具体用户设置
        :return:
        """
        pass

    @api(rule='/quotation/settings', method='get')
    def quotation_settings(self, employee_ids, order, page, per_page):
        """报价方案书列表
        :param employee_ids:
        :param order:
        :param page:
        :param per_page:
        :return:
        """
        pass

    @api(rule='/quotation/settings')
    def quotation_settings_create(self, employee_id, setting_name, setting_payload):
        """
        创建配置
        :param employee_id:
        :param setting_name:
        :param setting_payload:
        :return:
        """
        pass

    @api(rule='/quotation/settings/<s_id>', method='patch')
    def quotation_setting_edit(self, s_id, payload):
        """
        更新配置
        :param s_id:
        :param payload:
        :return:
        """
        pass

    @api(rule='/quotation/settings/<id>', method='delete')
    def quotation_delete(self, id):
        """
        删除配置
        :param id:
        :return:
        """
        pass
