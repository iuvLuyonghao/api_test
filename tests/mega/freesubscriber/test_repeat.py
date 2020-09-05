# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.freesubscriber.freesubscriber import FreesubscriberClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = FreesubscriberClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestRepeat(BaseTestCase):

    def test_repeat(self):
        """
        试用账号查重
        :return:
        """
        resp = self.client.repeat(username=D.freesubscriber.username)
        self.assertEqual(10000,resp.code)
        self.assertEqual(False,resp.data.repeat)

    def test_repeat1(self):
        """
        试用账号查重
        :return:
        """
        resp = self.client.repeat(username=D.freesubscriber.username1)
        self.assertEqual(10000,resp.code)
        self.assertEqual(True,resp.data.repeat)

    def test_repeat2(self):
        """
        试用账号查重
        :return:
        """
        resp = self.client.repeat(username=D.freesubscriber.username2)
        self.assertEqual(10000,resp.code)
        self.assertEqual(False,resp.data.repeat)


