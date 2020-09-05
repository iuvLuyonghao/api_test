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

    @api(rule="/leads/grab", is_json_req=True)
    def get_leads(self, new_sales_id: int, sub_firm_id: int, leads_type_id: int):
        """详情页获取、分配leads
        :param new_sales_id:获取人的id
        :param sub_firm_id:公司ID
        :param leads_type_id:leads类型

        :return:
        """
        pass

    @api(rule="/leads/batch_grab", is_json_req=True)
    def componylist_get_leads(self, batch_data, new_sales_id):
        """公司列表页获取、分配leads
        :return:
        """
        pass

    @api(rule="/leads/batch_grab", is_json_req=True)
    def componylist_get_leads(self, batch_data, new_sales_id):
        """公司列表页获取、分配leads
        :return:
        """
        pass

    @api(rule="/leads/ungrab/check", is_json_req=True)
    def check_release_leads(self, sub_firm_id: int = None):
        """
        检查是否可以释放leads
        :param sub_firm_id: 公司id
        :return:
        """
        pass

    @api(rule="/leads/ungrab/options", is_json_req=True)
    def options_for_vacancy_reason(self, sub_firm_id: int = None, leads_type_id: int = None):
        """
        空置原因的选项
        :param sub_firm_id: 公司id
        :param leads_type_id: leads类型
        :return:
        """
        pass

    @api(rule="/leads/ungrab", is_json_req=True)
    def release_leads(self, sub_firm_id: int, leads_type_id: int,
                      release_type_id: int,
                      release_reason_id: int,
                      give_up_reason_id: int = None, evaluate_type_id: int = None, evaluate_type_note: str = None,
                      give_up_reason_note: str = None):
        """
        空置leads
        :param sub_firm_id: 公司id 必填
        :param leads_type_id: leads类型 必填
        :param give_up_reason_id: 放弃原因的id
        :param give_up_reason_note: 放弃原因的备注
        :param release_type_id: 释放方式的id
        :param release_reason_id: 释放原因的id
        :param evaluate_type_id: 评定类别的id
        :param evaluate_type_note: 评定类别的备注
        :return:
        """
        pass

    def delay_leads(self, leads_id: int, extend_months: int = 3, web_source="auto_test", dist_version="V1.0"):
        """lead 延期
        :param leads_id: leads id
        :param extend_months: 延期时间，默认三个月
        :param web_source: 请求接口来源
        :param dist_version: 接口版本
        :return:
        """
        payload = {
            "id": leads_id,
            "extend_month": extend_months,
            "web_source": web_source,
            "dist_version": dist_version
        }
        return self._call_api(endpoint="leads/{}/delay".format(leads_id), req_kwargs=dict(json=payload))

    def apply_delay_leads(self, leads_id: int, to_id: int, apply_note="test", web_source="auto_test",
                          dist_version="v1.0"):
        """申请延期leads
        :param leads_id: 需要延期的leads id
        :param to_id: 审批主管的 ID
        :param apply_note: 申请说明
        :param web_source: 接口来源
        :param dist_version: 版本号
        :return:
        """
        payload = {
            "id": leads_id,
            "to_id": to_id,
            "apply_note": apply_note,
            "web_source": web_source,
            "dist_version": dist_version
        }
        return self._call_api(endpoint="leads/{}/delay_apply".format(leads_id), req_kwargs=dict(json=payload))

    @api(rule="leads/not_active_leads", remove_null=True, is_json_req=True)
    def query_inactive_leads_list(self, created_date: int, page: int = 1, perpage: int = 20, sales_id: int = 0,
                                  web_source="auto_test", sub_firm_name=None,
                                  leads_type_id=None):
        """不积极leads列表
        :param sales_id:  销售/客服ID exp.10243 irene.liu
        :param sub_firm_name: 公司名
        :param leads_type_id: leads 类型 [["工程信息", 1], ["市场调研", 4], ["信息加订", 5], ["协助跟进", 6], ["招采信息", 11], ["招采加订", 12],
        ["招采协助", 13], ["CRM/APP", 15]]
        :param created_date:检查不积极的时间戳s: 1577721600 2019-12-31
        :param page: 页数 1
        :param perpage 每页 默认20
        :param web_source 请求来源
        :return:
        """
        pass

    @api(rule="/leads/set_active")
    def set_active(self, sub_firm_id: int, leads_type_id: int):
        """设置为积极跟进接口
        :param sub_firm_id: 公司ID
        :param leads_type_id: lead类型ID
        :return:
        """
        pass
