# -*- coding:utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class StatisticsClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/sub_firms/<firm_id>/statistics/info", is_json_req=True)
    def statistics_a_info(self, firm_id=None):
        """用户行为统计-页面基本信息
        :param :
        :return:
        """
        pass

    @api(rule="/sub_firms/<firm_id>/statistics/calculate", is_json_req=True)
    def statistics_calculate(self, calculate_begin, calculate_end, modules, categories,
                             active_times, pl_style, firm_id=None):
        """用户行为统计-申请开始统计
        :param firm_id:
        :param calculate_begin: 统计的起始日期
        :param calculate_end: 统计的终结日期
        :param modules: 选择要统计的模块
        :param categories: 一个保存了被勾选的项所需要包含运算的category的数组
        :param active_times: 活跃次数
        :param pl_style:
        :return:
        """
        pass

    @api(rule="/statistics/export", method='get', is_json_req=False)
    def statistics_export(self, token):
        """用户行为统计-申请导出文件
        :param token:
        :return:
        """
        pass

    @api(rule="/statistics/retrieve", is_json_req=True)
    def statistics_retrieve(self, token, only_basic):
        """用户行为统计-获取渲染信息
        :param token:
        :param only_basic: 是否只获取基本信息。默认false即获取所有信息
        :return:
        """
        pass



