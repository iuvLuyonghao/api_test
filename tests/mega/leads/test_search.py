# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.leads.leads import LeadsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
import json
from util.myencoder import MyEncoder
file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = LeadsClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestSearch(BaseTestCase):

    def test_search(self):
        """
        leads列表搜索
        :return:
        """
        resp = self.client.search(data=json.dumps(D.searchdata.data,cls=MyEncoder,indent=4))
        self.assertEqual(resp.code, 10000)

    def test_search1(self):
        """
        leads列表搜索
        :return:
        """
        resp = self.client.search(data=json.dumps(D.searchdata.data1,cls=MyEncoder,indent=4))
        self.assertEqual(resp.code, 10000)
