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


class TestDetailSearch(BaseTestCase):

    def test_detail_search(self):
        """详细搜索"""
        resp = self.client.detail_search(ids=D.detail_search.ids,sales_ids=D.detail_search.sales_ids)
        self.assertEqual(resp.code, 10000)
        self.assertEqual(resp.data.sub_firms[0]["id"], 304140)

    def test_detail_search1(self):
        """详细搜索"""
        resp = self.client.detail_search(ids=D.detail_search.ids1,sales_ids=D.detail_search.sales_ids)
        self.assertEqual(resp.code, 10000)

    def test_detail_search2(self):
        """详细搜索"""
        resp = self.client.detail_search(ids=D.detail_search.ids2,sales_ids=D.detail_search.sales_ids)
        self.assertEqual(resp.code, -995)

    def test_detail_search3(self):
        """详细搜索"""
        resp = self.client.detail_search(ids=D.detail_search.ids1,sales_ids=D.detail_search.sales_ids,firm_name=D.detail_search.firm_name)
        self.assertEqual(resp.code, 10000)
        self.assertIn("测试",resp.data.sub_firms[0]["name"])

    def test_detail_search4(self):
        """详细搜索"""
        resp = self.client.detail_search(ids=D.detail_search.ids1,sales_ids=D.detail_search.sales_ids,register_capital_min=D.detail_search.register_capital_min)
        self.assertEqual(resp.code, 10000)

    def test_detail_search5(self):
        """详细搜索"""
        resp = self.client.detail_search(ids=D.detail_search.ids1,sales_ids=D.detail_search.sales_ids,register_capital_min=D.detail_search.register_capital_min1)
        self.assertEqual(resp.code, -995)


