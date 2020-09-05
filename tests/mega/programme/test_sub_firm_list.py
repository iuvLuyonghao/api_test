# -*- coding: utf-8 -*-

import unittest
from config import services
from apis.mega.login.login import Login
from data import DataCenter as D
from apis.mega.programme.programme import ProgrammeClient
import json
import time
import qav5.log

class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        t=int(time.time())
        cls.client = ProgrammeClient(base_url=services.mega)
        cls.resp =cls.client.sub_firm_list(source="sales",signature="''",t=t)
        cls.t=t
        cls.signature=cls.resp.data.signature

    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass


class TestSubFirmList(BaseTestCase):
    def test_sub_firm_list(self):
        """无签名"""
        resp =self.client.sub_firm_list(source="sales",signature="",t=self.t)
        self.assertEqual(-997,resp.code)
        self.assertEqual("没有签名",resp.message)
        self.assertEqual({},resp.data)

    def test_sub_firm_list1(self):
        """签名验证不通过"""
        resp =self.client.sub_firm_list(source="sales",signature="111",t=self.t)
        self.assertEqual(-997,resp.code)
        self.assertEqual("签名不匹配",resp.message)

    def test_sub_firm_list1(self):
        """无时间戳"""
        resp =self.client.sub_firm_list(source="sales",signature="111",t="")
        self.assertEqual(-997,resp.code)
        self.assertEqual("没有时间戳",resp.message)

    def test_sub_firm_list2(self):
        """不传source"""
        resp =self.client.sub_firm_list(source="",signature=self.signature,t=self.t)
        self.assertEqual(-995,resp.code)
        self.assertEqual("参数错误！请检查必填项！",resp.message)

    def test_sub_firm_list3(self):
        """页码、数量空"""
        resp =self.client.sub_firm_list(source="sales",signature=self.signature,t=self.t)
        self.assertEqual(10000,resp.code)
        self.assertEqual(1,resp.data.page_infos.page)
        self.assertEqual(100,resp.data.page_infos.per_page)

    def test_sub_firm_list4(self):
        """页码、数量1"""
        resp =self.client.sub_firm_list(source="sales",signature=self.signature,t=self.t,page=1,per_page=1)
        self.assertEqual(10000,resp.code)
        self.assertEqual(1,resp.data.page_infos.page)
        self.assertEqual(1,resp.data.page_infos.per_page)

    def test_sub_firm_list5(self):
        """页码、数量50000"""
        resp =self.client.sub_firm_list(source="sales",signature=self.signature,t=self.t,page=50000,per_page=50000)
        self.assertEqual(10000,resp.code)
        self.assertEqual(50000,resp.data.page_infos.page)
        self.assertEqual(1000,resp.data.page_infos.per_page)

    def test_sub_firm_list6(self):
        """开始时间的最大值<结束时间"""
        resp =self.client.sub_firm_list(source="sales",signature=self.signature,t=self.t,start_at="2029-03-05",end_at="2019-03-05")
        self.assertEqual(10000,resp.code)
        self.assertEqual([],resp.data.firms)
        self.assertEqual(0,resp.data.page_infos.total)

    def test_sub_firm_list7(self):
        """开始时间的最大值=结束时间"""
        resp =self.client.sub_firm_list(source="sales",signature=self.signature,t=self.t,start_at="2020-03-05",end_at="2020-03-05")
        self.assertEqual(10000,resp.code)
        self.assertEqual([],resp.data.firms)
        self.assertEqual(0,resp.data.page_infos.total)

    def test_sub_firm_list8(self):
        """开始时间与结束时间包含所有数据"""
        resp =self.client.sub_firm_list(source="sales",signature=self.signature,t=self.t,start_at="1990-03-05",end_at="2029-03-05")
        self.assertEqual(10000,resp.code)
        self.assertNotEqual([],resp.data.firms)

    def test_sub_firm_list9(self):
        """公司id存在"""
        resp =self.client.sub_firm_list(source="sales",signature=self.signature,t=self.t,firm_ids=[255309,000000000000])
        self.assertEqual(10000,resp.code)

    def test_sub_firm_list10(self):
        """公司id不存在"""
        resp =self.client.sub_firm_list(source="sales",signature=self.signature,t=self.t,firm_ids=[33333333333333,000000000000])
        self.assertEqual(10000,resp.code)
        self.assertEqual([],resp.data.firms)
