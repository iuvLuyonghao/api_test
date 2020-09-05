# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class AccountClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/free_subscribers/search", is_json_req=True, remove_null=True)
    def free_subscribers_search(self, sub_firm_ids, sub_contact_ids=None, order=None, ids=None, contact_info=None,
                                dist_version="v1.0", web_source="automation", page=1, per_page=10):
        """ 试用账号搜索接口
        :param sub_firm_ids: 公司IDs [307823]
        :param sub_contact_ids: 联系人数组
        :param order 排序
        :param ids:
        :param contact_info: 手机号或姓名模糊搜索
        :param dist_version: 版本号
        :param web_source: 调用平台
        :param page: 第几页 1
        :param per_page: 每页个数 10
        :return:
        """
        pass

    @api(rule="/free_subscribers/<account_id>/msg", method="get", is_json_req=False)
    def free_subscribers_info(self, account_id):
        """
        获取试用账号的内容
        :param account_id: 试用账号ID
        :return:
        """
        pass

    @api(rule='/subscribers/show/<a_id>', method='get')
    def subscribers_show(self, a_id=None):
        """
        企业账号详情页
        :param a_id: 账号ID
        :return:
        """
        pass

    @api(rule='subscribers/viewed_project_count', method='get')
    def subscribers_view_project(self, id, user_type):
        """
        账号已查看项目数
        :param a_id: 账号ID
        :param user_type:账号类型 试用账号 0 ， 正式账号 2
        :return:
        """
        pass

    @api(rule='subscribers/viewed_bid_count', method='get')
    def subscribers_view_bid(self, id, user_type):
        """
        账号已查看公告数
        :param a_id: 账号ID
        :param user_type:账号类型 试用账号 0 ， 正式账号 2
        :return:
        """
        pass

    @api(rule='/subscribers/bid_view_histories', method='get', remove_null=True)
    def subscribers_view_bid_history(self, user_id, user_type, view_date_min, view_date_max=None, page=1, per_page=20):
        """
        账号查看招采信息记录
        :param user_id:
        :param user_type: 2 正式 1试用
        :param view_date_min:
        :param view_date_max:
        :param page:
        :param per_page:
        :return:
        """
        pass

    @api(rule='/subscribers/search_history', method='get', remove_null=True)
    def subscribers_search_histories(self, user_id, user_type, search_date_min, search_date_max=None, page=1,
                                         per_page=20, device_type=3):
        """
        账号查看慧招采搜索记录
        :param user_id:
        :param user_type: 2 正式 0试用
        :param search_date_min:
        :param search_date_max:
        :param page:
        :param per_page:
        :param device_type 数据平台： 0 - leads-web， 1 - app， 2 - 阅读器， 3： bid， 4：reach
        :return:
        """
        pass
