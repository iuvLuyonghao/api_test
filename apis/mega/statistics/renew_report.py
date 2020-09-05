# -*- coding: utf-8 -*-

# from qav5. http import api, BaseClient
from qav5.http.client import  BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class RenewReportClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/renew_reports/detail", is_json_req=True)
    def cce_renew_report(self,date_need_renew_max, date_need_renew_min,cce_need_renew,detail,stages,
                         product_type_id=None,renew_calculate_date=None,amount_need_renew_min=None,amount_need_renew_max=None,
                         renewed=None,next_renew_date_max=None,next_renew_date_min=None):
        """
        客服的续约统计
        :param need_renew_date_max:应续时间大于
        :param need_renew_data_min:应续时间小于
        :param branch_office_ids:分公司
        :param leader_ids:队长
        :param cce_need_renew:应续客服
        :param product_type_id:产品类型
        :param stage:订单阶段
        :param sales_date:销售日期/统计日期
        :param amount_need_renew_min:应续金额小于
        :param amount_need_renew_max:应续金额大于
        :param renewed:1: 已续约， 2: 未续约
        :return:
        """
        pass


    @api(rule="/renew_reports/list", is_json_req=True)
    def cce_renew_report_list(self,month_need_renew_max=None,month_need_renew_min=None,next_renew_date_max=None,next_renew_date_min=None,
                              branch_office_id=None,leader_id=None,cce_need_renew=None,product_type_id=None,stages=None,renew_calculate_date=None,
                              amount_need_renew_min=None,amount_need_renew_max=None,employee_active=None):
        pass
