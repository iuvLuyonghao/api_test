# -*- coding: utf-8 -*-

import unittest
from apis.mega.appusers.appusers import AppusersClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
import json

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = AppusersClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestContractUploadForUser(BaseTestCase):

    def test_contract_upload_for_user(self):
        """订单创建个人账号页信息"""
        contract_file = abspath(join(__file__, "../../../../data/files/ss.pdf"))
        resp = self.client.contract_upload_for_user(sub_firm_id="255309",contract_file=contract_file)
        self.assertTrue(10000, resp.code)
