# -*- coding: utf-8 -*-

import unittest
from apis.mega.appusers.appusers import AppusersClient
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
        cls.client = AppusersClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestAppOrderCreateInfo(BaseTestCase):

    def test_app_order_create_info(self):
        """订单创建个人账号页信息"""
        resp = self.client.app_order_create_info(order_id="117827")
        self.assertTrue(10000, resp.code)
        self.assertEqual(117827,resp.data.order_id)

    def test_app_order_create_info1(self):
        """订单创建个人账号页信息"""
        resp = self.client.app_order_create_info(order_id="1178270000000")
        self.assertTrue(5001, resp.code)
        self.assertEqual('app订单不存在',resp.message)

    def test_app_order_create_info2(self):
        """订单创建个人账号页信息"""
        resp = self.client.app_order_create_info(order_id="")
        self.assertTrue(5001, resp.code)
        self.assertEqual('app订单不存在',resp.message)

    def test_app_order_create_info3(self):
        """订单创建个人账号页信息"""
        resp = self.client.app_order_create_info(order_id="'")
        self.assertTrue(-995, resp.code)