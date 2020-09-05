# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.monthly_reports.monthly_reports import MothlyReportsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from util.setroles import SetRoles
import qav5.log
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
        cls.client = MothlyReportsClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestMonthlyReportsList(BaseTestCase):

    def test_monthly_reports_list(self):
        """
        获取月报列表
        :return:
        """
        resp = self.client.monthly_reports_list()
        self.assertEqual(resp.code,10000)

    def test_monthly_reports_list1(self):
        """
        获取月报列表
        :return:
        """
        resp = self.client.monthly_reports_list(month=5)
        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.data.list[0]['monthly_report_time'],"2020-5")

    def test_monthly_reports_list2(self):
        """
        获取月报列表
        :return:
        """
        resp = self.client.monthly_reports_list(year=2020)
        self.assertEqual(resp.code,10000)
        self.assertIn("2020",resp.data.list[0]['monthly_report_time'])

    def test_monthly_reports_list3(self):
        """
        获取月报列表
        :return:
        """
        resp = self.client.monthly_reports_list(status=4)
        self.assertEqual(resp.code,10000)
        self.assertIn("审核通过",resp.data.list[0]['monthly_report_status'])

    def test_monthly_reports_list4(self):
        """
        获取月报列表
        :return:
        """
        resp = self.client.monthly_reports_list(leader_ids="[33274]")
        self.assertEqual(resp.code,10000)


    def test_monthly_reports_list5(self):
        """
        获取月报列表
        :return:
        """
        resp = self.client.monthly_reports_list(branch_office_ids="[1]")
        self.assertEqual(resp.code,10000)


    def test_monthly_reports_list6(self):
        """
        获取月报列表
        :return:
        """
        resp = self.client.monthly_reports_list(type=1)
        self.assertEqual(resp.code,10000)
