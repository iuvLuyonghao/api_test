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


class TestFreeDelay(BaseTestCase):

    def test_free_delay_1(self):
        """
        试用账号延期-无效的试用账号
        :return:
        """
        resp = self.client.free_delay(sub_firm_id=D.delay.sub_firm_id,free_subscriber_ids=D.delay.free_subscriber_ids1,delay_day=D.delay.delay_day)
        self.assertEqual(resp.code, -995)
        self.assertTrue("is invalid" in resp.data.free_subscriber_ids[0])

    def test_free_delay_2(self):
        """
        试用账号延期
        :return:
        """
        resp = self.client.free_delay(sub_firm_id=D.delay.sub_firm_id,free_subscriber_ids=D.delay.free_subscriber_ids2,delay_day=D.delay.delay_day)
        self.assertEqual(resp.code, 10000)
        self.assertEqual(resp.message, "success")

    def test_free_delay_3(self):
        """
        试用账号延期99天
        :return:
        """
        resp = self.client.free_delay(sub_firm_id=D.delay.sub_firm_id,free_subscriber_ids=D.delay.free_subscriber_ids2,delay_day=D.delay.delay_day99)
        self.assertEqual(resp.code, -995)
        self.assertEqual(resp.data["delay_day"][0], "does not have a valid value")


    def test_free_delay_4(self):
        """
        试用账号延期9999999天
        :return:
        """
        resp = self.client.free_delay(sub_firm_id=D.delay.sub_firm_id,free_subscriber_ids=D.delay.free_subscriber_ids2,delay_day=D.delay.delay_day9999999)
        self.assertEqual(resp.code, -995)
        self.assertEqual(resp.data["delay_day"][0], "does not have a valid value")

    def test_free_delay_5(self):
        """
        批量延期
        :return:
        """
        resp = self.client.free_delay(sub_firm_id=D.delay.sub_firm_id,free_subscriber_ids=D.delay.free_subscriber_ids3,delay_day=D.delay.delay_day)
        self.assertEqual(resp.code, 10000)
        self.assertEqual(resp.message, "success")

