# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class IntendedSubFirmClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/intended_sub_firms/search", remove_null=True)
    def search(self, branch_office_id: int = None, leader_id: int = None, sales_id: int = None,
               leads_type_id: int = None, stage_id: int = None, status: list = None,
               stage_change_at_max: int = None, stage_change_at_min: int = None, recent_call_at_max: int = None,
               recent_call_at_min: int = None,
               level: int = None, expect_order_years: int = None, expect_amount_max: int = None,
               expect_amount_min: int = None, notes=None,
               province_ids: list = None, region_ids=None, page=None, branch_office_ids: list = None,
               leader_ids: list = None, sales_ids: list = None):
        """
        意向客户列表
        :param branch_office_id:分公司id
        :param leader_id:队长id
        :param sales_id:员工id
        :param leads_type_id:leads类型id
        :param stage_id:跟单阶段
        :param status [1] 正常
        :param stage_change_at_max:最新阶段变更时间最大值
        :param stage_change_at_min:最新阶段变更时间最小值
        :param recent_call_at_max:近期有效沟通时间最大值
        :param recent_call_at_min:近期有效沟通时间最小值
        :param level:客户级别
        :param expect_order_years:预计签单年限
        :param expect_amount_max:预计签单金额最大值
        :param expect_amount_min:预计签单金额最小值
        :param notes:其他备注
        :param province_ids:省份数组
        :param region_ids:
        :param page:
        :param branch_office_ids:分公司的ids 数组
        :param leader_ids:员工队长的ids
        :param sales_ids:员工的ids
        :return:
        """
        pass

    @api(rule='/intended_sub_firms/<i_id>', method='patch', remove_null=True)
    def intended_sub_firms_edit(self, i_id, stage_id=None, level_id=None, province_ids: list = None,
                                region_ids: list = None,
                                expect_order_years=None, expect_amount=None, expect_bid_amount=None, next_plan=None,
                                notes=None):
        """
        意向客户编辑
        :param i_id 要更新的数据ID
        :param stage_id:跟单阶段
        :param level_id:客户级别
        :param province_ids:省份数组
        :param region_ids:区域的ids
        :param expect_order_years:预计合作年限
        :param expect_amount:预计签单金额
        :param expect_bid_amount:招采金额
        :param next_plan:下一步行动方案
        :param notes:其他备注
        :return:

        {
            "stage_id": 1,
            "level_id": 1,
            "province_ids": [],
            "region_ids": [],
            "expect_order_years": 1,
            "expect_amount": 1,
            "expect_bid_amount": 1,
            "next_plan": 1,
            "notes": ""
        }
        """
        pass

    @api(rule='/intended_sub_firms/<i_id>/get_next_plan', method='get')
    def get_next_plan(self, i_id):
        """
        获取下一步方案
        :param i_id:
        :return:
        """
        pass

    @api(rule='/intended_sub_firms/<i_id>/give_up', remove_null=True)
    def give_up(self, i_id, give_up_reason=None, give_up_reason_note=None):
        """
        删除（申请放弃）
        :param i_id 要删除的ID
        :param give_up_reason:
        :param give_up_reason_note:
        :return:
        """
        pass

    @api(rule='/intended_sub_firms/<i_id>/approval')
    def approval(self, i_id, approval: int = 3):
        """
        审批接口
        :param i_id
        :param approval: 3: 不通过 4: 通过，
        :return:
        """
        pass

    @api(rule='/intended_sub_firms/count', remove_null=True)
    def count(self, branch_office_ids=None, branch_office_id=None, leader_ids=None, leader_id=None, sales_id=None,
              free_subscriber_login=90, visit_contact_user=90, rcc_share=90, quotation=60, confirm_order=30, give_up=90,
              leads_type_id=1, contact_login_count=90, rcc_share_count=90):
        """
        意向客户统计接口
        :return:
        {
  "branch_office_ids": [],
  "branch_office_id": 1,
  "leader_ids": [],
  "leader_id": 1,
  "sales_id": 1,
  "sales_ids": [],
  "free_subscriber_login": 90,
  "visit_contact_user": 90,
  "rcc_share": 90,
  "quotation": 60,
  "confirm_order": 30,
  "give_up": 90,
  "leads_type_id": 1
}
        """
        pass
