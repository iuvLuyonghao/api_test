# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.generalmodule.generalmodule import GeneralmoduleClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestEmployees(BaseTestCase):

    def test_employees(self):
        """普通员工"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username="celine.zhang", password=D.user_mega.password)
        token = resp.data.session_id
        client = GeneralmoduleClient(base_url=services.mega, access_token=token)
        resp = client.employees()
        self.assertEqual(10000,resp.code)


    def test_employees1(self):
        """销售主管"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username="tony.hong", password=D.user_mega.password)
        token = resp.data.session_id
        client = GeneralmoduleClient(base_url=services.mega, access_token=token)
        resp = client.employees()
        self.assertEqual(10000,resp.code)
        self.assertEqual("sanmi.yi",resp.data[0]['leader_name'])

    def test_employees2(self):
        """客服经理"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username="tansy.zhu", password=D.user_mega.password)
        token = resp.data.session_id
        client = GeneralmoduleClient(base_url=services.mega, access_token=token)
        resp = client.employees()
        self.assertEqual(10000,resp.code)


    def test_employees3(self):
        """总监"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username="randy.zhang", password=D.user_mega.password)
        token = resp.data.session_id
        client = GeneralmoduleClient(base_url=services.mega, access_token=token)
        resp = client.employees()
        self.assertEqual(10000,resp.code)
