# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class PersonalAccountClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/sub_contacts/sub_contacts_options", is_json_req=True, remove_null=True)
    def sub_contacts_options(self, sub_firm_id: int, search_name=None, sub_contact_id: int = None):
        """
        联系人搜索选项
        :param sub_firm_id:公司ID
        :param search_name: 搜索的关键词，电话或者姓名（模糊）
        :param sub_contact_id:联系人ID
        :return:
        """
        pass

    @api(rule="/app_users/search", method="get", is_json_req=True, remove_null=True)
    def sub_user_search(self, mobile, sub_firm_id: int = None):
        """
        账号查询
        :param mobile:
        :param sub_firm_id:
        :return:
        """
        pass

    @api(rule="/app_users", is_json_req=True, remove_null=True)
    def app_users_create(self, mobile, name, user_department, email, sub_start: int, sub_end: int, sub_firm_id: int,
                         sub_contact_id: int, login_start: int, login_end: int, package_type: int, subs: dict = None,
                         web_source="reach", dist_version="v1.0"):
        """
        创建个人账号
        :param mobile:
        :param name:
        :param user_department:
        :param email:
        :param sub_start:
        :param sub_end:
        :param sub_firm_id:
        :param sub_contact_id:
        :param login_start:
        :param login_end:
        :param package_type:
        :param subs:
        :param web_source:
        :param dist_version:
        :return:
        exa: {
    "subs":{
        "allot":{
            "allot_admin":0
        },
        "crm":{
            "allot_admin":0
        },
        "project":{
            "category_val":"["2_0","201_2","202_2","203_2","3_0"]",
            "project_stage_val":"[1,2,3]",
            "province_ids":"[3,5]",
            "region_ids":"[13]"
        },
        "bid":{
            "product_category_ids":"[10001,10002,11242,10049,10050,10051,10052,10053]",
            "purchase_category_ids":"[11512,10354,10353,11574,14945,11185]",
            "province_ids":"[3,5,4,11]",
            "region_ids":"[13,26]"
        }
    },
    "mobile":"13701761991",
    "name":"仲健",
    "email":"zhongjian@jwac.net jianweicom@263.net",
    "user_department":"",
    "sub_firm_id":26231,
    "sub_contact_id":40188,
    "sub_start":1580486400000,
    "sub_end":1582905600000,
    "login_start":1581436800000,
    "login_end":1582646400000,
    "package_type":11,
    "web_source":"reach",
    "dist_version":"v1.0"
}
        """
        pass

    @api(rule="/app_users/list", is_json_req=True, remove_null=True)
    def app_user_list(self, package_types: int = None, sub_firm_id: int = None, search_name=None, sub_contact_id=None,
                      page=None, per_page=None, orders: list = []):
        """
        个人账号列表
        :param orders:[{"last_login_at": "desc"}]
        :param package_type: 套餐类型（账号类型）1-免费账号 2-基础账号 3-高级账号 13-试用账号
        :param sub_firm_id: 公司ID
        :param search_name: 账号名-模糊查询；手机号码-模糊匹配
        :param sub_contact_id: 联系人ID，联系人页面必传
        :param page:
        :param per_page:
        :return:
        """
        pass

    @api(rule='/app_users/delay', remove_null=True)
    def app_users_delay(self, app_user_ids=None, delay_days=1, free_subscriber_delay=True, sub_contact_ids=None):
        """
        试用账号延期
        :param app_user_ids:账号ID数组
        :param delay_days:延期天数 ；延期天数，如果填小于1的就会初始化成1，如果大于7，会覆盖成7
        :param free_subscriber_delay:试用的企业账号是否延期
        :param sub_contact_ids:账号的属于的联系人ID
        :return:
        """
        pass

    @api(rule='/app_users/set_admin', remove_null=True)
    def app_users_set_admin(self, app_user_id: int = 0, user_main_admin: int = 1):
        """
        账号设置主管理员-试用和正式只能设置一个主管理员
        :param app_user_id: 账号ID
        :param user_main_admin:设置用户系统主系统管理员,(0:否|1:是)
        :return:
        """
        pass

    @api(rule='/app_users/set_dac_view', remove_null=True)
    def app_users_set_dac_view(self, app_user_id=0, dac_view_leader=0):
        """
        账号开通数据统计权限
        :param app_user_id:账号ID
        :param dac_view_leader:设置dac数据统计管理员,(0:否|1:是)
        :return:
        """
        pass

    @api(rule='/app_users/set_view_limit')
    def app_users_set_view_limit(self, app_user_id=0, limit_open_count=0, limit_open_count_bid=0):
        """
        设置可查看项目/公告数
        :param app_user_id: 账号ID
        :param limit_open_count:设置查看项目数量限制
        :param limit_open_count_bid:设置招采每日查看数量限制
        :return:
        """
        pass

    def app_users_uses_file_upload(self, app_users_file, sub_firm_id: int):
        """
        批量创建账号上传文件
        :param app_users_file:app使用人表格 最多500条数据 .excel 文件
        :param sub_firm_id:公司ID
        :return:
        """
        return self._call_api("/app_users/uses_file_upload", method='POST',
                              req_kwargs=dict(data={"sub_firm_id": sub_firm_id},
                                              files=dict(app_users_file=open(app_users_file, 'rb'))),
                              disable_log=True)

    def app_users_contract_upload(self, batch_id, contract_file):
        """
        批量创建账号的合同文件
        :param batch_id:excel 上传的生成批次ID
        :param contract_file:合同文件 支持pdf
        :return:
        """
        return self._call_api("/app_users/contract_upload", method='POST',
                              req_kwargs=dict(data={"batch_id": batch_id},
                                              files=dict(contract_file=open(contract_file, 'rb'))),
                              disable_log=True)

    @api(rule='/app_users/batch_create_preview', method='get')
    def app_users_batch_create_preview(self, batch_id):
        """
        批量创建的校验页面
        :param batch_id:
        :return:
        """
        pass

    @api(rule='/app_users/batch_create', remove_null=True)
    def app_users_batch_create(self, batch_id=None, temp_id=None):
        """
        批量创建个人账号
        :param batch_id:一个批次的创建（二选一）
        :param temp_id:单一个账号创建
        :return:
        """

    @api(rule="/app_users/sub_create", is_json_req=True)
    def app_users_sub_create(self, name=None, mobile=None, package_type=None, pl_style=None, sub_firm_id=None):
        """

        @param name:
        @param mobile:
        @param package_type:
        @param pl_style:
        @param sub_firm_id:
        """
        pass

    def app_users_contract_upload_for_user(self, sub_firm_id, contract_file):
        """
        批量创建账号的合同文件
        :param sub_firm_id:
        :param contract_file:合同文件 支持pdf
        :return:
        """
        return self._call_api("/app_users/contract_upload_for_user", method='POST',
                              req_kwargs=dict(data={"sub_firm_id": sub_firm_id},
                                              files=dict(contract_file=open(contract_file, 'rb'))),
                              disable_log=True)

    @api(rule="/app_users/<id>/show", method="get")
    def app_users_id_show(self, id: int):
        """

        @param id:
        """
        pass

    @api(rule="/app_users/setting", remove_null=True)
    def app_users_setting(self, id: int, crm=None, pl_style=None, allot_admin=None, allot_region_ids=None,
                          allot_province_ids=None, allot_city_ids=None):
        """

        @param id:
        @param crm:
        @param pl_style:
        @param allot_admin:
        @param allot_region_ids:
        @param allot_province_ids:
        @param allot_city_ids:
        """
        pass

    @api(rule="/app_users/dms_subscription", remove_null=True)
    def app_users_dms_subscription(self,order_id,id=None):
        """
        dms订阅详情、经销商/项目包订阅信息详情
        :param order_id:订单id
        :param id:dms 订阅id
        :return:
        """
        pass

    @api(rule="/app_users/dms_subscription_update", remove_null=True)
    def app_users_dms_subscription_update(self,sub_firm_id,order_id,dealer_num,project_package,sub_start,sub_end,id=None):
        """
        dms订阅详情、经销商/项目包订阅信息编辑或创建
        :param sub_firm_id:公司id
        :param order_id:订单id
        :param dealer_num:经销商账号数
        :param project_package:项目包数
        :param sub_start:开始时间
        :param sub_end:结束时间
        :param id:若传id则为更新
        :return:
        """
        pass

    @api(rule="/app_users/replace_apply_list", remove_null=True,method="GET")
    def app_users_replace_apply_list(self,page=None,apply_at_min=None,apply_at_max=None,status=None,package_type=None,sub_firm_ids=None):
        """
        更换使用人申请列表
        :param page:
        :param apply_at_min:申请时间最小值
        :param apply_at_max:申请时间最大值
        :param status:{'1' => '未审核', '2' => '已审核', '3' => '已退回客户', '4' => '已退回客服'}
        :param package_type:1:免费， 2：基础 3：高级
        :param sub_firm_ids:公司id
        :return:
        """
        pass

    @api(rule="/app_users/replace_apply_pass", remove_null=True)
    def app_users_replace_apply_pass(self,id,operate_type):
        """
        审核通过
        :param id:申请记录的id
        :param operate_type:{1: 通过， 2: 手动通过}
        :return:
        """
        pass

    @api(rule="/app_users/replace_apply_back", remove_null=True)
    def app_users_replace_apply_back(self,reject_reason,id,sub_firm_id,person_user_id):
        """
        审核退回
        :param reject_reason:退回原因
        :param id:申请记录得ID
        :param sub_firm_id:公司ID
        :param person_user_id:app id
        :return:
        """
        pass

    @api(rule="/app_users/replace_user_info", remove_null=True,method="GET")
    def app_users_replace_user_info(self,id):
        """
        更换使用人申请详情
        :param id:
        :return:
        """
        pass

    @api(rule="/app_users/replace_user_update", remove_null=True)
    def app_users_replace_user_update(self,id,card_path):
        """
        更换人替换名片
        :param id:记录ID
        :param card_path:名片链接
        :return:
        """
        pass