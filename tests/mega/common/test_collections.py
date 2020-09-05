# -*- coding: utf-8 -*-

import unittest,warnings
from apis.mega.common.collections import CommonClient
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
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = CommonClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestCommonCollections(BaseTestCase):


    def test_get_collections(self):
        """
        get_collections
        :return:
        """
        resp = self.client.get_collections()
        self.assertEqual(resp.code, 10000)

    def test_add_collections_is_none_point(self):
        """
        add_collections
        :return:
        """
        resp = self.client.add_collections()
        self.assertEqual(resp.code, 0)
        self.assertTrue("can\'t be blank" in resp.data.router_name)

    def test_add_delete_collections(self):

        """
        add_collections
        :return:
        """
        datalist= self.client.get_collections()
        for data in datalist.data:
            self.client.delete_collections(id=data['id'])
        resp = self.client.add_collections(router_name=D.collection_data.router_name)
        self.assertEqual(resp.code, 10000)
        self.assertTrue("352652" in resp.data.router_name)

    def test_delete_collections(self):
        """
        delete_collections
        :return:
        """
        resp1 = self.client.add_collections(router_name=3456)
        self.assertEqual(resp1.code, 10000)
        resp = self.client.delete_collections(id=resp1.data['id'])
        self.assertEqual(resp.code, 10000)

