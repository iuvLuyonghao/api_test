# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch


class ProgrammeClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)


    @api(rule="/external_calls/sub_firm_list")
    def sub_firm_list(self, source:str,signature:str,t:str=None,page:int=None,per_page:int=None,start_at:str=None,end_at:str=None,only_total:int=None,firm_ids:list=None):
        """
        公司库统一方案--获取公司
        :param source: 工程信息部'research' 慧讯网销售部'cost_sales' 慧讯网信息部'cost_info' 慧讯网信息部关联'cost_alias' 销售客服'sales' 招采信息部'bid_info'
        :param page:页码
        :param per_page:分页数
        :param start_at:修改时间最小区间。 取当天的起始时间
        :param end_at:修改时间最大区间。 取当天的结束时间
        :param only_total:是否只返回总数量（0：否；1：是）
        :param firm_ids:公司id数组，用于搜索返回指定公司id的数据
        :return:
        """
        pass

    @api(rule="/external_calls/firm_leads_employee", is_json_req=True)
    def firm_leads_employee(self,t:int,signature:str,source:str=None,sub_firm_ids=None):
        """
        统一公司库获取公司跟进人
        :param t:时间戳
        :param signature:签名
        :param sub_firm_ids:sub_firm_id 的数组
        :param source:
        :return:
        """
        pass

    @api(rule="/external_calls/employee_firm_ids",method="get")
    def employee_firm_ids(self,employee_id:int,t:int,signature:str):
        """
        统一公司库 员工获取跟进的公司IDs
        :param employee_id:员工ID
        :param t:时间戳
        :param signature:签名
        :return:
        """
        pass