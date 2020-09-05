# -*- coding: utf-8 -*-

import unittest
from apis.mega.company.company import CompanyClient
from apis.mega.modifyauth.auth import AuthClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5.conn import OracleClient
from qav5 import log

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_neko_zhou.username, password=D.user_neko_zhou.password)
        cls.token = resp.data.session_id
        cls.client = CompanyClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestLeadsType(BaseTestCase):

    def test_user_crm_apply(self):
        """客服助理申请CRM登录接口"""
        resp = self.client.crm_user_apply(sub_firm_id=40241, apply_days=1)
        self.assertEqual(10000, resp.code)
        self.assertEqual("success", resp.message)

    def test_user_crm_apply_invalid_firm_id(self):
        """客服助理申请CRM登录接口-无效公司ID"""
        resp = self.client.crm_user_apply(sub_firm_id=0, apply_days=1)
        self.assertEqual(-995, resp.code)
        self.assertEqual("无效的ID", resp.data.sub_firm_id)
