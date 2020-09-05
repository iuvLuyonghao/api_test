# -*- coding: utf-8 -*-

import unittest
from apis.mega.appusers.appusers import AppusersClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
import json

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = AppusersClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestAppUsersSetting(BaseTestCase):

    def test_app_users_setting(self):
        """账号编辑设置"""
        resp = self.client.app_users_setting(id="117827")
        self.assertEqual(10000, resp.code)
        self.assertEqual('success',resp.message)

    def test_app_users_setting1(self):
        """账号编辑设置"""
        resp = self.client.app_users_setting(id="1016")
        print(resp)
        self.assertEqual(5001, resp.code)
        self.assertEqual('账号不存在',resp.message)