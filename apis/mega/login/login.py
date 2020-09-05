# -*- coding: utf-8 -*-

# from qav5.http import api, BaseClient
from qav5.http.client import  BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch


class Login(BaseClient):
    def __init__(self, base_url, **kwargs):
        super().__init__(base_url, kwargs)
        self.interceptor = lambda r, j: Bunch(j)

    @api("/login", is_json_req=True)
    def get_token(self, username, password):
        """
        login
        :param username:
        :param password:
        :return:
        """
        pass

    def login(self, username, password):
        """login api get session_id
        :param username:
        :param password:
        :return:
        """
        data = {
            "username": username,
            "password": password
        }
        return self._call_api(endpoint="/login", req_kwargs=dict(json=data))
