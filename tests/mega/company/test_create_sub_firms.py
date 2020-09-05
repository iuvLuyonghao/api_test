# -*- coding: utf-8 -*-

import unittest
from apis.mega.company.company import CompanyClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from util.setroles import SetRoles
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


class TestCreateSubFirms(BaseTestCase):

    def test_create_sub_firms(self):
        """创建公司"""
        SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,8,29,35,36]")
        resp = self.client.create_sub_firms(firm_names='[{"name":"内蒙古小飞侠公司","remark":1,"reason":2}]',home_country_id=D.create_sub_firms.home_country_id,country_id=D.create_sub_firms.country_id)
        self.assertEqual(resp.code, 10000)

    def test_create_sub_firms1(self):
        """创建公司"""
        SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,8,29,35,36]")
        resp = self.client.create_sub_firms(firm_names='[{"name":"内蒙古小飞侠公司","remark":1,"reason":2}]',home_country_id=D.create_sub_firms.home_country_id1,country_id=D.create_sub_firms.country_id1)
        self.assertEqual(resp.code, 0)
