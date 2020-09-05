# -*- coding: utf-8 -*-

import unittest
from apis.mega.zoom.zoom import ZoomClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from qav5.conn import OracleClient, MySQLConnectionMgr, PostGreSQLClient


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = ZoomClient(base_url=services.mega, access_token=cls.token)
        cls.oracle_client = OracleClient(services.oracle['username'], services.oracle['password'],
                                         services.oracle['conn_str'])

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestNoticeRccReader(BaseTestCase):

    def test_notice_rcc_reader(self):
        """通知阅读器,发起zoom会议"""
        resp = self.client.notice_rcc_reader(employee_id=1, join_url="12312", sub_contact_id=1)
        self.assertGreaterEqual(resp.code, 10000)
