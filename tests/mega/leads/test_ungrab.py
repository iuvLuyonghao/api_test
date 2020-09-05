# -*- coding: utf-8 -*-
import json
import unittest, warnings
from apis.mega.leads.leads import LeadsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from util.setroles import SetRoles
import qav5.log
from qav5.conn import OracleClient

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = LeadsClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestBlankLeads(BaseTestCase):

    def test_blank_search_blank_reason(self):
        """空置公司搜索-空置原因"""
        resp = self.client.blank_search(sales_id=1, blank_reason=1)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 1)


class TestEmployeeBlankLeads(BaseTestCase):
    def test_valid_blank_list_name(self):
        """有效空置列表"""
        resp = self.client.employee_release_list(sub_firm_name='宜兴')
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 1)

    def test_invalid_blank_blank_reason(self):
        """无效空置原因"""
        resp = self.client.employee_release_list(blank_reason=101, release_type=1)
        self.assertEqual(10000, resp.code)

    def test_valid_blank_list_order_asc(self):
        """有效空置列表-排序升序"""
        order = [{'potential_rank': 'asc'}, {'approved_at': 'asc'}]
        resp = self.client.employee_release_list(order=json.dumps(order))
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 1)

    def test_valid_blank_list(self):
        """有效空置列表"""
        resp = self.client.employee_release_list(page=100)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 1)

    def test_invalid_blank_list(self):
        """无效空置列表"""
        resp = self.client.employee_release_list(release_type=1)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 1)
