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

    def test_cce_renew_report(self):
        """客服的续约统计"""
        resp = self.client.cce_renew_report(renewed=1,next_renew_date_max=30,next_renew_date_min=1,date_need_renew_max=30,date_need_renew_min=1,cce_need_renew=1,detail=True,stages='[3,4,9]')
        self.assertEqual(10000,resp.code)

    def test_cce_renew_report1(self):
        """客服的续约统计"""
        date_need_renew_max=int(datetime.datetime.strptime('2020-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        date_need_renew_min=int(datetime.datetime.strptime('2019-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        resp = self.client.cce_renew_report(renewed=1,next_renew_date_max=30,next_renew_date_min=1,date_need_renew_max=date_need_renew_max,date_need_renew_min=date_need_renew_min,cce_need_renew="22449",detail=True,stages='[3,4,9]')
        self.assertEqual(10000,resp.code)

    def test_cce_renew_report2(self):
        """客服的续约统计"""
        date_need_renew_max=int(datetime.datetime.strptime('2020-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        date_need_renew_min=int(datetime.datetime.strptime('2019-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        resp = self.client.cce_renew_report(renewed=1,next_renew_date_max=30,next_renew_date_min=1,date_need_renew_max=date_need_renew_max,date_need_renew_min=date_need_renew_min,cce_need_renew="22449",detail=True,stages='[3,4,9]')
        self.assertEqual(10000,resp.code)
        self.assertEqual(resp.data[0]['need_renew_count']['employee_id'],22449)

    def test_cce_renew_report3(self):
        """客服的续约统计"""
        date_need_renew_max=int(datetime.datetime.strptime('2020-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        date_need_renew_min=int(datetime.datetime.strptime('2019-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        resp = self.client.cce_renew_report(renewed=1,next_renew_date_max=30,next_renew_date_min=1,date_need_renew_max=date_need_renew_max,date_need_renew_min=date_need_renew_min,cce_need_renew="22449",detail=False,stages='[3,4,9]')
        self.assertEqual(10000,resp.code)


    def test_cce_renew_report4(self):
        """客服的续约统计"""
        date_need_renew_max=int(datetime.datetime.strptime('2020-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        date_need_renew_min=int(datetime.datetime.strptime('2019-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        resp = self.client.cce_renew_report(renewed=1,next_renew_date_max=30,next_renew_date_min=1,date_need_renew_max=date_need_renew_max,date_need_renew_min=date_need_renew_min,cce_need_renew="22449",detail=True,stages='[]')
        self.assertEqual(10000,resp.code)

    def test_cce_renew_report5(self):
        """客服的续约统计"""
        resp = self.client.cce_renew_report(renewed=1,next_renew_date_max=30,next_renew_date_min=1,date_need_renew_max="",date_need_renew_min="",cce_need_renew="",detail=True,stages='[]')
        self.assertEqual(-995,resp.code)

    def test_cce_renew_report6(self):
        """客服的续约统计"""
        date_need_renew_max=int(datetime.datetime.strptime('2020-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        date_need_renew_min=int(datetime.datetime.strptime('2016-06-07 16:30:10','%Y-%m-%d %H:%M:%S').timestamp())
        resp = self.client.cce_renew_report(renewed=1,next_renew_date_max=30,next_renew_date_min=1,date_need_renew_max=date_need_renew_max,date_need_renew_min=date_need_renew_min,cce_need_renew="22449",detail=True,stages='[]')
        self.assertEqual(-994,resp.code)


