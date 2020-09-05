# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class FreesubscriberClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/free_subscribers/delay", is_json_req=True)
    def free_delay(self, sub_firm_id: int, free_subscriber_ids: list, delay_day: int):
        """
        试用账号延期
        :param sub_firm_id:公司id
        :param free_subscriber_ids:试用账号的ids
        :param delay_day:延期天数
        :return:
        """
        pass

    @api(rule="/free_subscribers/repeat", is_json_req=True, method="get")
    def repeat(self, username: str):
        """
        试用账号查重
        :param username:试用账号姓名
        :return:
        """
        pass

    @api(rule="/free_subscribers/contact_infos", is_json_req=True, method="get")
    def contact_infos(self, sub_firm_id: int):
        """
        联系人设置的信息
        :param sub_firm_id:公司id
        :return:
        """
        pass

    @api(rule='/free_subscribers/<a_id>', method='get', is_json_req=False)
    def account_detail(self, a_id):
        """
        试用账号详情
        :param a_id: 试用账号ID
        :return:
        """
        pass

    @api(rule='/free_subscribers/<a_id>', method='delete')
    def account_del(self, a_id):
        """
        删除试用账号
        :param a_id: 试用账号ID
        :return:
        """
        pass

    @api(rule="/free_subscribers/options", method="get")
    def options(self):
        """
        创建试用账号options
        :return:
        """
        pass

    @api(rule='/free_subscribers/<a_id>', method='patch')
    def account_edit(self, a_id, sub_firm_id, free_subscribers=None, free_subscriber_setting=None, subscriptions=None):
        """
        编辑试用账号
        :param a_id: 试用账号ID
        :param sub_firm_id:
        :param free_subscribers:
        :param free_subscriber_setting:
        :param subscriptions:
        :return:
        """
        pass

    @api(rule='/free_subscribers')
    def account_create(self, sub_firm_id, free_subscribers=None, free_subscriber_setting=None, subscriptions=None
                       ):
        """
        创建企业试用账号
        :param sub_firm_id:
        :param free_subscribers:
        :param free_subscriber_setting:
        :param subscriptions:
        :return:
        """
        pass




