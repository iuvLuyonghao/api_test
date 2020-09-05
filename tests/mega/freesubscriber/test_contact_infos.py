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


class TestContactInfos(BaseTestCase):

    def test_contact_infos(self):
        """
        联系人设置的信息
        :return:
        """
        resp = self.client.contact_infos(sub_firm_id=D.freesubscriber.sub_firm_id)
        self.assertEqual(10000,resp.code)
        self.assertEqual(919693,resp.data.contacts[0]["id"])

    def test_contact_infos1(self):
        """
        联系人设置的信息
        :return:
        """
        resp = self.client.contact_infos(sub_firm_id=D.freesubscriber.sub_firm_id1)
        self.assertEqual(101,resp.code)
        self.assertEqual("无效的ID",resp.message)


    def test_contact_infos2(self):
        """
        联系人设置的信息
        :return:
        """
        resp = self.client.contact_infos(sub_firm_id=D.freesubscriber.sub_firm_id2)
        self.assertEqual(101,resp.code)
        self.assertEqual("无效的ID",resp.message)


    def test_contact_infos3(self):
        """
        联系人设置的信息
        :return:
        """
        resp = self.client.contact_infos(sub_firm_id=D.freesubscriber.sub_firm_id3)
        self.assertEqual(10000,resp.code)




