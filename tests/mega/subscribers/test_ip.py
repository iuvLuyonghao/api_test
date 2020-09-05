# -*- coding: utf-8 -*-

import unittest
from apis.mega.subscribers.subscribers import SubscribersClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from const import RecallsBiz
import json
from qav5 import log

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)
mysql = None


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = SubscribersClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestIp(BaseTestCase):

    def test_blocked_ip_list(self):
        """被锁IP列表"""
        resp = self.client.blocked_ip_list()
        self.assertEqual(resp.code,10000)

    def test_blocked_ip_list1(self):
        """被锁IP列表"""
        resp = self.client.blocked_ip_list(ip="180.184.97.13")
        self.assertEqual(resp.code,10000)

    def test_blocked_ip_list2(self):
        """被锁IP列表"""
        resp = self.client.blocked_ip_list(unlock=0)
        self.assertEqual(resp.code,10000)
        self.assertIsNotNone(resp.data.list[0]['unlock_date'])

    def test_unblock_ip(self):
        blocked_ip_id=self.client.blocked_ip_list(unlock=1).data.list[0]['id']
        resp=self.client.unblocked_ip(blocked_ip_id=blocked_ip_id,customer_check=1,unlock_reason="接口测试")
        self.assertEqual(resp.code,10000)

