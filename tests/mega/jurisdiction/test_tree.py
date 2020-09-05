# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.jurisdiction.jurisdiction import JurisdictionClient
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
        cls.client = JurisdictionClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestTree(BaseTestCase):

    def test_tree(self):
        """
        组织架构
        :return:
        """
        resp = self.client.tree()
        self.assertEqual(resp.code, 10000)
