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


class TestMonthlyReportsEdit(BaseTestCase):

    def test_monthly_reports_edit(self):
        """
        月报编辑页面
        :return:
        """
        resp = self.client.monthly_reports_edit(id=5885,submit_type=2,personal_target=9999,bid_personal_target=888.22,order_income_target=4545.11,
                                                order_income_bid_target=1111.9999999999)
        print(resp)
        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.data.status,2)
        self.assertEqual(resp.data.order_income_target,'4545.11')

    def test_monthly_reports_edit1(self):
        """
        月报编辑页面
        :return:
        """
        resp = self.client.monthly_reports_edit(id=5885,submit_type=1,personal_target=9999,bid_personal_target=888.22,order_income_target=4545.11,
                                                order_income_bid_target=1111.9999999999)
        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.data.status,1)
        self.assertEqual(resp.data.order_income_target,'4545.11')

    def test_monthly_reports_edit2(self):
        """
        月报编辑页面
        :return:
        """
        resp = self.client.monthly_reports_edit(id=5885,submit_type=3,personal_target=9999,bid_personal_target=888.22,order_income_target=4545.11,
                                                order_income_bid_target=1111.9999999999)
        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.data.order_income_target,'4545.11')

    def test_monthly_reports_edit3(self):
        """
        月报编辑页面
        :return:
        """
        resp = self.client.monthly_reports_edit(id=5885,submit_type=4,personal_target=9999,bid_personal_target=888.22,order_income_target=4545.11,
                                                order_income_bid_target=1111.9999999999)
        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.data.order_income_target,'4545.11')

    def test_monthly_reports_edit4(self):
        """
        月报编辑页面
        :return:
        """
        resp = self.client.monthly_reports_edit(id=5885,submit_type=44,personal_target=9999,bid_personal_target=888.22,order_income_target=4545.11,
                                                order_income_bid_target=1111.9999999999)
        self.assertEqual(resp.code,-995)

    def test_monthly_reports_edit5(self):
        """
        月报编辑页面
        :return:
        """
        resp = self.client.monthly_reports_edit(id=5885,submit_type=4,personal_target="哈哈哈",bid_personal_target=888.22,order_income_target=4545.11,
                                                order_income_bid_target=1111.9999999999)
        self.assertEqual(resp.code,-995)
