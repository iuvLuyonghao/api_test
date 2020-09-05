# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.company.company import CompanyClient
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
        cls.client = CompanyClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestChangeSubFirms(BaseTestCase):

    def test_change_sub_firms(self):
        """修改公司信息"""
        resp = self.client.change_sub_firms(id=D.change_sub_firms.id,
                                            firm_names='[{"name":"上海小飞侠公司","remark":1,"reason":2}]',
                                            home_country_id=9,
                                            country_id=9)
        print(resp)
        self.assertIn("上海小飞侠公司",resp.data.firm_name)
        self.assertEqual(9,resp.data.home_country_id)

