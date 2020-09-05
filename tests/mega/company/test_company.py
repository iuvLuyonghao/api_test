# -*- coding: utf-8 -*-

import unittest, warnings
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
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestCompanySimpleSearch(BaseTestCase):

    def test_simple_search(self):
        """simple search valid """
        resp = self.client.simple_search(search_name="吴江")
        self.assertEqual(resp.code, 10000)
        self.assertTrue("吴江" in resp.data.sub_firms[0]['name'])

    def test_simple_search_key_null(self):
        """simple search key is null"""
        resp = self.client.simple_search(search_name="")
        self.assertEqual(resp.code, 10000)



class TestGetSubFirms(BaseTestCase):
    def test_get_sub_firms(self):
        """获取公司"""
        resp = self.client.sub_firms(firm_name_full_match=D.leads_154990.sub_firm_name)
        self.assertEqual(resp.code, 10000)
        self.assertEqual(resp.data.sub_firms[0]["id"], D.leads_154990.sub_firm_id)
        self.assertEqual(resp.data.sub_firms[0]["firm_name"], D.leads_154990.sub_firm_name)

    def test_sub_firm_detail(self):
        """获取公司详情"""
        resp = self.client.sub_firms_detail(firm_id=D.leads_154990.sub_firm_id)
        self.assertEqual(resp.code, 10000)
        self.assertEqual(resp.data.id, D.leads_154990.sub_firm_id)
        self.assertEqual(resp.data.firm_name, D.leads_154990.sub_firm_name)

    def test_sub_firm_permission(self):
        """获取公司权限"""
        permissions = ["can_create_sub_contact", "can_edit"]
        resp = self.client.sub_firm_permissions(firm_id=D.leads_154990.sub_firm_id, permissions=json.dumps(permissions))
        self.assertEqual(resp.code, 10000)
        self.assertEqual(resp.data[0], "can_create_sub_contact")
