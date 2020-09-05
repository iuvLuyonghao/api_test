# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.contact.contact import ContactClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = ContactClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestSetResign(BaseTestCase):

    def test_set_resign(self):
        """
        存在的联系人设为离职
        :return:
        """
        resp = self.client.set_resign(sub_contact_id=D.set_resign.sub_contact_id,resign=D.set_resign.resign)
        self.assertEqual(resp.code, 10000)

    def test_set_resign1(self):
        """
        不传参数
        :return:
        """
        resp = self.client.set_resign()
        self.assertEqual(resp.code, -995)

    def test_set_resign2(self):
        """
        id不存在
        :return:
        """
        resp = self.client.set_resign(sub_contact_id=D.set_resign.sub_contact_id*100,resign=D.set_resign.resign)
        self.assertEqual(resp.code, 101)

