# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.monthly_reports.monthly_reports import MothlyReportsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
import qav5.log
file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = MothlyReportsClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestMonthlyReportsInfo(BaseTestCase):

    def test_monthly_reports_info(self):
        """
        月报详情页
        :return:
        """
        resp = self.client.monthly_reports_info(id=5885)
        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.data.report_info.id,5885)

    def test_monthly_reports_info1(self):
        """
        月报详情页
        :return:
        """
        resp = self.client.monthly_reports_info(id=588599999999)
        self.assertEqual(resp.code,-995)
        self.assertEqual(resp.data.id,588599999999)