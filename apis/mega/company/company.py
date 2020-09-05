# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class CompanyClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/sub_firms/simple_search", is_json_req=True)
    def simple_search(self, search_name):
        """simple search api
        :param search_name: 搜索的关键词
        :return:
        """
        pass

    @api(rule="/sub_firms/<id>/leads_info", method="get", is_json_req=False)
    def leads_info(self, id):
        """公司详情页lead 信息
        :param id: 公司ID
        :return:
        """
        pass

    @api(rule="/sub_firms", method="get", is_json_req=False)
    def sub_firms(self, firm_name_full_match):
        """获取公司
        :param firm_name_full_match: 公司名
        :return:
        """

        pass

    @api(rule="/sub_firms", method="post", is_json_req=True)
    def create_sub_firms(self, firm_names=None,home_country_id:str=None,country_id:str=None):
        """创建公司
        :param firm_name: 公司名
        :param home_country_id: 公司城市id
        :param country_id: 城市id
        :return:
        """

        pass

    @api(rule="/sub_firms/<id>", method="patch", is_json_req=True)
    def change_sub_firms(self, id:int,firm_names:str =None,home_country_id:str=None,country_id:str =None):
        """修改
        :param id: 公司id
        :param firm_name: 公司名
        :param home_country_id: 公司所在城市id
        :param country_id: 城市id
        :return:
        """

        pass


    @api(rule="/sub_firms/<firm_id>", method="get", is_json_req=False)
    def sub_firms_detail(self, firm_id=int):
        """
        获取公司详情
        :param firm_id: 公司ID
        :return:
        """
        pass

    @api(rule="/sub_firms/<firm_id>/permissions", method="get", is_json_req=False)
    def sub_firm_permissions(self, firm_id=int, permissions=""):
        """获取公司权限
        :param firm_id: 公司ID
        :param permissions: 权限列表json array
        :return:
        """
        pass

    @api(rule="/user_crms/apply_login", is_json_req=True)
    def crm_user_apply(self, sub_firm_id, apply_days):
        """
        客服助理申请登录CRM管理系统接口
        :param sub_firm_id: 公司ID
        :param apply_days: 申请天数
        :return:
        """
        pass

    @api(rule="/sub_firms/detail_search", is_json_req=True)
    def detail_search(self, ids : list = None, sales_ids: list =None,firm_name:list = None,register_capital_min: int=None):
        """
        详细搜索
        :param ids: 公司ID
        :param sales_ids: 跟进人id
        :return:
        """
        pass

    @api(rule="/sub_firms/options", is_json_req=True,method="get")
    def options(self, options: list = None):
        """
        取得选项
        :param options: 选项
        :return:
        """
        pass

    @api(rule="/sub_firms/<id>/firm_info", is_json_req=True,method="get")
    def firm_info(self, id: int):
        """
        获取企业顶部信息
        :param options: 选项
        :return:
        """
        pass

    @api(rule="/sub_firms/<id>/archive_renew_infos", method="get", is_json_req=False)
    def archive_renew_infos(self, id):
        """取得续约备注
        :param id: 公司ID
        :return:
        """
        pass

