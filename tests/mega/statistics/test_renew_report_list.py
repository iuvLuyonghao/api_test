# -*- coding: utf-8 -*-

import unittest
from apis.mega.statistics.renew_report import RenewReportClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
import time,datetime
from const import RecallsBiz
import json
from qav5 import log

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)
mysql = None


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_allen_wang.username, password=D.user_allen_wang.password)
        cls.token = resp.data.session_id
        cls.client = RenewReportClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestRenewReport(BaseTestCase):

    def test_cce_renew_report_list(self):
        """公司的续约统计"""
        resp = self.client.cce_renew_report_list(branch_office_id=3,cce_need_renew=1,stages='[3,4,9]',next_renew_date_max=30,
                                                 next_renew_date_min=1,leader_id=27999)
        self.assertEqual(10000,resp.code)

