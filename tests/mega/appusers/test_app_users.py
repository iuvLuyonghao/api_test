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

    def test_set_allot_admin(self):
        """设置分配管理员"""
        for allot_admin in[1,0]:
            resp = self.client.set_allot_admin(app_user_ids="[364128]",allot_admin=allot_admin)
            self.assertEqual(10000, resp.code)
            self.assertEqual('设置成功！',resp.message)

    def test_set_allot_admin1(self):
        """设置分配管理员-有一个免费账号"""
        for allot_admin in[1,0]:
            resp = self.client.set_allot_admin(app_user_ids="[364128,364364,364375]",allot_admin=allot_admin)
            self.assertEqual(10000, resp.code)
            self.assertEqual('设置成功2, 失败个数1',resp.message)

    def test_set_allot_admin2(self):
        """设置分配管理员-试用账号"""
        for allot_admin in[1,0]:
            resp = self.client.set_allot_admin(app_user_ids="[362537]",allot_admin=allot_admin)
            self.assertEqual(10000, resp.code)
            self.assertEqual('设置成功！',resp.message)

    def test_set_allot_admin3(self):
        """设置分配管理员-未认证账号"""
        for allot_admin in[1,0]:
            resp = self.client.set_allot_admin(app_user_ids="[363481]",allot_admin=allot_admin)
            self.assertEqual(10000, resp.code)
            self.assertEqual('未开通分配功能',resp.message)
