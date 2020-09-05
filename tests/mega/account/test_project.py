# -*- coding: utf-8 -*-

import unittest
from apis.mega.account.project import ProjectClient
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
        cls.client = ProjectClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestProject(BaseTestCase):

    def test_project_stages(self):
        """取得项目阶段"""
        resp = self.client.project_stages()
        self.assertTrue(10000, resp.code)
        self.assertTrue("success", resp.message)

    def test_project_categories(self):
        """取得项目一级分类"""
        resp = self.client.project_categories()
        self.assertTrue(10000, resp.code)
        self.assertTrue("success", resp.message)

    def test_project_subs_categories(self):
        """取得项目二级分类"""
        resp = self.client.project_sub_categories()
        self.assertTrue(10000, resp.code)
        self.assertTrue("success", resp.message)

    def test_project_bid_categories(self):
        """采购信息类别"""
        resp = self.client.project_bid_categories()
        self.assertTrue(10000, resp.code)
        self.assertTrue("success", resp.message)

    def test_project_product_categories(self):
        """产品及服务类别"""
        resp = self.client.project_product_categories()
        self.assertTrue(10000, resp.code)
        self.assertTrue("success", resp.message)
