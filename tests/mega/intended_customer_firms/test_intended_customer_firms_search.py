# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.intended_customer_firms.intended_customer_firms import IntendedCustomerFirmsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
from qav5.utils.util import gen_rand_str

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_allen_wang.username, password=D.user_allen_wang.password)
        cls.token = resp.data.session_id
        cls.client = IntendedCustomerFirmsClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestIntendedCustomerFirmsSearch(BaseTestCase):

    def test_search_null(self):
        """意向客户-列表搜索"""
        resp = self.client.intended_customer_firms_search(status='[1]')
        self.assertEqual(resp.code,10000)


class TestIntendedCustomerFirmsCount(BaseTestCase):
    def test_intended_customer_firms_count(self):
        """意向公司统计"""
        resp = self.client.intended_customer_firms_count(branch_office_ids="[1]",leader_ids="[20034]",leads_type_id=None)
        self.assertEqual(resp.code,10000)