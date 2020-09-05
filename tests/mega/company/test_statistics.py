# -*- coding:utf-8 -*-
import random
import time
import unittest
import warnings
from apis.mega.company.statistics import StatisticsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5.conn import OracleClient
from qav5 import log
import json

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)

global t, fid
list1 = [1, 2, 3, 5, 8, 255309, 369023, 369725, 99204, 300989, 304275]
fid = random.choice(list1)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = StatisticsClient(base_url=services.mega, access_token=cls.token)
        # cls.oracle_client = OracleClient(services.oracle['username'], services.oracle['password'],
        #                                  services.oracle['conn_str'])
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestStatisticsClient(BaseTestCase):

    def test_statistics_a_info(self):
        """页面基本信息"""
        # cursor = self.oracle_client.execute_query(
        #    """SELECT sub_firm_id FROM sub_firms WHERE RONUM <= 20"""
        # )
        # row = cursor.fetchone()
        # print(type(row), row)
        resp = self.client.statistics_a_info(firm_id=fid)
        self.assertEqual(10000, resp.code)

    def test_statistics_calculate(self):
        """申请开始统计"""
        resp = self.client.statistics_calculate(calculate_begin='2019/9/9', calculate_end='2020/2/2',
                                                modules=json.dumps(['user_module']),
                                                categories=json.dumps(["subscriber_login_percent",
                                                                       "subscriber_login_top"]),
                                                active_times=3, pl_style=0,
                                                firm_id=fid)
        self.assertEqual(10000, resp.code)
        global t
        t = resp['data']['token']

    def test_statistics_info_err01(self):
        """页面基本信息-冷却时间未到"""
        resp = self.client.statistics_a_info(firm_id=fid)
        self.assertEqual(1600, resp.code)
    time.sleep(20)

    def test_statistics_calculate_err01(self):
        """申请开始统计-不选择时间"""
        resp = self.client.statistics_calculate(calculate_begin='', calculate_end='',
                                                modules=json.dumps(['user_module']),
                                                categories=json.dumps(["subscriber_login_percent",
                                                                       "subscriber_login_top"]),
                                                active_times=3, pl_style=0,
                                                firm_id=1)
        self.assertEqual(-995, resp.code)

    def test_statistics_calculate_err02(self):
        """申请开始统计-不选择模块(接口没有做限制)"""
        resp = self.client.statistics_calculate(calculate_begin='2020/1/1', calculate_end='2020/2/2',
                                                modules=json.dumps([]),
                                                categories=json.dumps([]),
                                                active_times=3, pl_style=0,
                                                firm_id=fid)
        self.assertEqual(1600, resp.code)

    def test_statistics_calculate_err03(self):
        """申请开始统计-活跃次数为0"""
        resp = self.client.statistics_calculate(calculate_begin='2020/1/1', calculate_end='2020/2/2',
                                                modules=json.dumps([]),
                                                categories=json.dumps([]),
                                                active_times=0, pl_style=0,
                                                firm_id=3)
        self.assertEqual(-995, resp.code)

    def test_statistics_calculate_err04(self):
        """申请开始统计-冷却中"""
        resp = self.client.statistics_calculate(calculate_begin='2019/9/9', calculate_end='2020/2/2',
                                                modules=json.dumps(['user_module']),
                                                categories=json.dumps(["subscriber_login_percent",
                                                                       "subscriber_login_top"]),
                                                active_times=3, pl_style=0,
                                                firm_id=fid)
        self.assertEqual(1600, resp.code)

    @unittest.skip('接口仅返回一个PDF文件')
    def test_statistics_export(self):
        """申请导出文件"""
        resp = self.client.statistics_export(token=t)
        self.assertEqual(10000, resp.code)

    def test_statistics_calculate_a_retrieve(self):
        """获取渲染信息-未计算完毕，数据不完整"""
        resp = self.client.statistics_retrieve(token=t, only_basic=False)
        self.assertEqual(1602, resp.code)

    def test_statistics_retrieve02(self):
        """获取渲染信息-获取基本信息"""
        resp = self.client.statistics_retrieve(token=t, only_basic=True)
        self.assertEqual(10000, resp.code)
        self.assertEqual(D.user_mega.username, resp.data.username)

    def test_statistics_retrieve_err01(self):
        """获取渲染信息-token错误"""
        resp = self.client.statistics_retrieve(token=2333, only_basic=False)
        self.assertEqual(-995, resp.code)

    @unittest.skip('如果请求的时候未计算完成，就会1602')
    def test_statistics_retrieve_suc(self):
        """获取渲染信息-获取所有信息"""
        resp = self.client.statistics_retrieve(token=t, only_basic=False)
        self.assertEqual(10000, resp.code)
        self.assertEqual(1000, resp.data.status)
