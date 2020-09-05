# -*- coding: utf-8 -*-

import unittest
from apis.mega.company.empowers import EmpowersClient
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
        cls.client = EmpowersClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestEmpowers(BaseTestCase):

    def test_approve_users(self):
        """公司的可审批的人"""
        resp = self.client.approve_users(sub_firm_id=255309)
        self.assertEqual(resp.code, 10000)

    def test_firm_parts(self):
        """公司可以授权的模块"""
        resp = self.client.firm_parts()
        self.assertEqual(resp.code, 10000)
        self.assertEqual(resp.data[0]['id'], 31)
        self.assertEqual(resp.data[0]['title'], '跟进/联系人')

    def test_empower_users(self):
        """公司可以授权的人"""
        resp = self.client.empower_users()
        self.assertEqual(resp.code, 10000)


    def test_empowers(self):
        """申请授权/主动授权"""
        resp = self.client.empowers(operate_type=1,firm_part_ids="[32]",sub_firm_id=255309,employee_id=1,notes="123456")
        self.assertEqual(resp.code, 10000)

    def test_empowers1(self):
        """申请授权/主动授权"""
        resp = self.client.empowers(operate_type=2,firm_part_ids="[32]",sub_firm_id=255309,employee_id=1,notes="123456")
        if resp.code != 4011:
            self.assertEqual(resp.code, 10000)


