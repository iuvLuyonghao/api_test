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


class TestArchive(BaseTestCase):

    def test_archive_renew_infos(self):
        """获取企业顶部信息"""
        resp = self.client.archive_renew_infos(id=D.firm_info.id)
        self.assertEqual(resp.code, 10000)

    def test_archive_renew_infos1(self):
        """获取企业顶部信息"""
        resp = self.client.archive_renew_infos(id=D.firm_info.id1)
        self.assertEqual(resp.code, 101)
