# -*- coding: utf-8 -*-

import unittest
from apis.mega.company.company import CompanyClient
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
        cls.client = CompanyClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestOptions(BaseTestCase):

    def test_options(self):
        """取得选项"""
        resp = self.client.options(D.options.options)
        self.assertEqual(resp.code, 10000)

    def test_options1(self):
        """取得选项"""
        resp = self.client.options(D.options.options1)
        self.assertEqual(resp.code, -995)

    def test_options2(self):
        resp = self.client.options(options='["intended_sub_firm_stage"]')
        self.assertEqual(resp.code, 10000)
        self.assertIsNotNone(resp.data.intended_sub_firm_stage)

    @unittest.skip("skip")
    def test_options3(self):
        """取得选项"""
        resp = self.client.options(D.options.options2)
        self.assertEqual(resp.code, 10000)


