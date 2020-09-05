# -*- coding: utf-8 -*-

# from qav5. http import api, BaseClient
from qav5.http.client import  BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class RecallsClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="sales_recalls/search_statement", is_json_req=True)
    def search_statement(self, department_ids: list, branch_office_ids: list, employee_ids: list, appt_date_min: int,
                         appt_date_max: int, web_source="reach", dist_version='v1.0'):
        """
        员工recall报告接口
        :param department_ids: 部门ID数组
        :param branch_office_ids: 分公司ID数组
        :param employee_ids: 员工ID数组
        :param appt_date_min: 开始时间 时间戳 exp. 1577807999
        :param appt_date_max: 结束时间
        :param web_source: reach
        :param dist_version: 接口版本
        :return:
        """
        pass

    @api(rule="sales_recalls", is_json_req=True)
    def create_recall(self, completed_at: int, completed_by, appt_date: int, employee_id: int, contact_by_value,
                      stage_id: int, sub_contact_id: int, sub_firm_id: int, sub_stage_ids="",
                      leads_type_value="project_info",
                      important_value="common"):
        """生成跟进记录

        :param completed_at: 完成时间戳
        :param completed_by: 完成人
        :param appt_date: 安排时间戳
        :param employee_id: 员工ID
        :param contact_by_value: 联系方式value，电话，email，rcc演示等
        :param stage_id: 阶段ID
        :param sub_stage_ids: 二级类别IDS，Json数组，初始值【1，2，3】
        :param sub_contact_id: 联系人ID
        :param sub_firm_id: 公司ID
        :param leads_type_value: leads类型value
        :param important_value: 重要程度value
        :return:
        """

    @api(rule="sales_recalls/search", is_json_req=True)
    def search_recall(self,  sub_firm_ids: list=None):
        """搜索recall

        :param sub_firm_ids: 公司id
        :return:
        """

