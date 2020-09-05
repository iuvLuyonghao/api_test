# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase

class LockClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})

    @api(rule="/subscribers/<id>/lock")
    def lock(self, id):
        """
        账号锁定
        :param id:订阅帐号id
        :return:
        """
        pass

    @api(rule="/subscribers/<id>/unlock")
    def unlock(self, id):
        """
        账号解锁
        :param id:订阅帐号id
        :return:
        """
        pass

    @api(rule="/subscribers/<id>/apply_unlock")
    def apply_unlock(self, id,apply_to=None,reason_id=None,reason_text=None,user_locked_history_id=None):
        """
        申请解锁
        :param id:订阅帐号id
        :return:
        """
        pass

    @api(rule="/subscribers/<id>/options_and_check")
    def options_and_check(self, id):
        """
        检查是否申请过锁定
        :param id:订阅帐号id
        :return:
        """
        pass