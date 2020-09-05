# -*- coding: utf-8 -*-

# from qav5. http import api, BaseClient
from qav5.http.client import  BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class MothlyReportsClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/monthly_reports/list", is_json_req=True)
    def monthly_reports_list(self, year=None,month=None,status=None,leader_ids=None,submitter_ids=None,branch_office_ids=None,type=None):
        """
        月报列表页
        :param year: 年份
        :param month: 月份
        :param status: 月报状态
        :param leader_ids: 团队
        :param submitter_ids: 提交人
        :param branch_office_ids: 分公司
        :param type: 月报类型
        :return:
        """
        pass

    @api(rule="/monthly_reports/<id>",method="GET")
    def monthly_reports_info(self,id):
        """
        月报详情页
        :param id:
        :return:
        """
        pass

    @api(rule="/monthly_reports/monthly_statistics", is_json_req=True)
    def monthly_reports_statistics(self,id):
        """
        月报详情-统计
        :param id:
        :return:
        """
        pass


    @api(rule="/monthly_reports/edit", is_json_req=True)
    def monthly_reports_edit(self,submit_type,id=None,type=None,branch_office_id=None,personal_target=None,bid_personal_target=None,
                             order_income_target=None,order_income_bid_target=None,pre_month_summary=None,plan_text=None,current_month_work_part=None,
                             last_month_work_part=None,last_month_personnel_part=None,current_month_personnel_part=None,last_month_team_part=None,
                             current_month_team_part=None,promote=None,last_month_executive_part=None,current_month_executive_part=None,
                             personal_part=None,other_part=None):
        """
        月报编辑页面
        :param submit_type:1: 保存 2：提交 3：设置当月填写 4：设置当月不填写
        :param id:月报id（如果没有则为新建，否则为编辑）
        :param type:月报类型：1：员工月报, 2： 团队月报, 3： 分公司月报
        :param branch_office_id:分公司id
        :param personal_target:个人销售目标
        :param bid_personal_target:个人招采销售目标
        :param order_income_target:团队销售目标
        :param order_income_bid_target:团队招采销售目标
        :param pre_month_summary:月前总结（团队：工作业绩以及完成情况）
        :param plan_text:未来计划（团队：本月或未来的计划）
        :param current_month_work_part:
        :param last_month_work_part:
        :param last_month_personnel_part:下月人才培养部分
        :param current_month_personnel_part:当前月人才培养部分
        :param last_month_team_part:下月团队稳定性分析
        :param current_month_team_part:当月团队在宣传公司价值观方面的提升
        :param promote:工作流程的优化及创新
        :param last_month_executive_part:上个月执行力
        :param current_month_executive_part:当月执行力
        :param personal_part:个人成长
        :param other_part:其他
        :return:
        """
        pass

    @api(rule="/monthly_reports/check_save", is_json_req=True)
    def monthly_reports_check_save(self,id):
        """
        月报编辑保存校验
        :param id:
        :return:
        """
        pass

    @api(rule="/monthly_reports/audit", is_json_req=True)
    def monthly_reports_audit(self,id,status,note):
        """
        月报审核
        :param id:
        :param status:
        :param note:
        :return:
        """
        pass

    @api(rule="/monthly_reports/interested_customer", is_json_req=True)
    def monthly_reports_interested_customer(self,monthly_report_id,interested_customer):
        """
        添加预计到账客户
        :param monthly_report_id:
        :param interested_customer:
        :return:
        """
        pass

    @api(rule="/monthly_reports/interested_customer/update", is_json_req=True)
    def monthly_reports_interested_customer_update(self,id,sales_date_expect,sales_date_expect_min):
        """
        编辑预计到账客户
        :param monthly_report_id:
        :param interested_customer:
        :return:
        """
        pass

    @api(rule="/monthly_reports/interested_customer/<id>",method="delete")
    def monthly_reports_interested_customer_delete(self,id):
        """
        删除预计到账客户
        :param monthly_report_id:
        :param interested_customer:
        :return:
        """
        pass


