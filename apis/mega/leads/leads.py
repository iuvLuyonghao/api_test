# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class LeadsClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/leads/types", method="get")
    def types(self):
        """取得leads类型
        :return:
        """
        pass

    @api(rule="/leads/search", is_json_req=True)
    def search(self, data):
        """leads列表搜索
        :param
        :return:
        """
        pass

    @api(rule="/leads/grab", is_json_req=True)
    def grab(self, new_sales_id: int, sub_firm_id: int, leads_type_id: int):
        """leads获取
        :param new_sales_id :获取人的ID
        :param sub_firm_id:公司ID
        :param leads_type_id:leads 类型 [["工程信息", 1], ["市场调研", 4], ["信息加订", 5], ["协助跟进", 6], ["招采信息", 11], ["招采加订", 12], ["招采协助", 13], ["CRM/APP", 15]]
        :return:
        """
        pass

    @api(rule="/leads/ungrab", is_json_req=True)
    def ungrab(self, new_sales_id: int, sub_firm_id: int, leads_type_id: int):
        """leads空置
        :param sub_firm_id:公司ID
        :param leads_type_id:leads 类型 [["工程信息", 1], ["市场调研", 4], ["信息加订", 5], ["协助跟进", 6], ["招采信息", 11], ["招采加订", 12], ["招采协助", 13], ["CRM/APP", 15]]
        :return:
        """
        pass

    @api(rule='blank_sub_firms/blank_search', remove_null=True)
    def blank_search(self, sub_firm_name=None, sales_id=None, province_ids=None, region_ids=None, potential_rank=None,
                     blank_reason=None, blank_continue_time=None,
                     change_to_blank_min=None, change_to_blank_max=None, contract_end_min=None, contract_end_max=None,
                     page=1, per_page=20, order=None):
        """
        空置公司搜索
        :param sub_firm_name:
        :param sales_id:
        :param province_ids:
        :param region_ids:
        :param potential_rank:
        :param blank_reason:空置原因 [[1, 销售跟进到期（销售跟进到期的工程信息leads）] [2, 客服未能续约（客服到期未能续约后掉出，在三个月内空置的工程信息leads）] ]
        :param blank_continue_time:
        :param change_to_blank_min:
        :param change_to_blank_max:
        :param contract_end_min:
        :param contract_end_max:
        :param page:
        :param per_page:
        :param order:排序方式,potential_rank： 业务覆盖范围，release_time: 空置时间 [{ potential_rank: asc },{"release_time": "asc" }]
        :return:
        """
        pass

    @api(rule='blank_sub_firms/employee_release_list', remove_null=True)
    def employee_release_list(self, sub_firm_name=None, blank_reason=None, sales_id=None, province_ids=None,
                              region_ids=None, potential_rank=None, blank_continue_time=None,
                              change_to_blank_min=None, change_to_blank_max=None, contract_end_min=None,
                              contract_end_max=None, page=1, per_page=20, order=None, release_type=2):
        """
        有效/无效空置列表
        :param sub_firm_name:公司名称
        :param blank_reason:空置原因
        :param sales_id:原销售
        :param province_ids:省份
        :param region_ids:区域
        :param potential_rank:覆盖范围 [["A（业务覆盖全国）", 1], ["B（业务覆盖多个省份）", 2], ["C（业务覆盖单个省份）", 3], ["未能确定", 4]]
        :param blank_continue_time:持续空置时间: [[1，3个月之内], [2，3个月到6个月], [3，6个月到1年], [4，1年以上]]
        :param change_to_blank_min:转为空置时间大于
        :param change_to_blank_max:转为空置时间小于
        :param contract_end_min:对手到期时间大于
        :param contract_end_max:对手到期时间小于
        :param page:页码
        :param per_page:每页条数
        :param order:排序方式,potential_rank： 业务覆盖范围，approved_at: 空置时间
        :param release_type:有效： 2 无效： 1
        :return:
        """
        pass
