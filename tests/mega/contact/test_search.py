# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.contact.search import SearchClient
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
        cls.client = SearchClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestContactSimpleSearch(BaseTestCase):

    def test_search_name(self):
        """
        姓名详细搜索
        :return:
        """
        resp = self.client.search(contact_name=D.search_data.contact_name)
        self.assertEqual(resp.code, 10000)
        self.assertTrue("测试" in resp.data.sub_contacts[0]['sub_contact_name'])

    def test_search_salutation(self):
        """
        称呼详细搜索
        :return:
        """
        resp = self.client.search(contact_name=None, salutation=D.search_data.salutation)
        self.assertEqual(resp.code, 10000)
        self.assertTrue("先生" in resp.data.sub_contacts[0]['sub_contact_name'])

    def test_simple_search(self):
        """
        简单搜索结果页
        :return:
        """
        resp = self.client.simple_search(province_id=D.simple_search_data.province_id,
                                         city_id=D.simple_search_data.city_id)
        self.assertEqual(resp.code, 10000)
