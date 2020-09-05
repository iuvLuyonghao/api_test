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
        cls.resp =cls.client.firm_leads_employee(source="sales",signature="''",t=t)
        cls.t=t
        cls.signature=cls.resp.data.signature

    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass


class TestFirmLeadsEmployee(BaseTestCase):
    def test_firm_leads_employee(self):
        """无签名"""
        resp =self.client.firm_leads_employee(source="sales",signature="",t=self.t)
        self.assertEqual(-997,resp.code)
        self.assertEqual("没有签名",resp.message)
        self.assertEqual({},resp.data)

    def test_firm_leads_employee1(self):
        """签名验证不通过"""
        resp =self.client.firm_leads_employee(source="sales",signature="111",t=self.t)
        self.assertEqual(-997,resp.code)
        self.assertEqual("签名不匹配",resp.message)

    def test_firm_leads_employee2(self):
        """无时间戳"""
        resp =self.client.firm_leads_employee(source="sales",signature="111",t="")
        self.assertEqual(-997,resp.code)
        self.assertEqual("没有时间戳",resp.message)

    def test_firm_leads_employee3(self):
        """不传source"""
        resp =self.client.firm_leads_employee(source="",signature=self.signature,t=self.t)
        self.assertEqual(-995,resp.code)
        self.assertEqual("参数错误！请检查必填项！",resp.message)

    def test_firm_leads_employee4(self):
        """无公司id"""
        resp =self.client.firm_leads_employee(source="sales",signature=self.signature,t=self.t)
        self.assertEqual(10000,resp.code)


    def test_firm_leads_employee5(self):
        """有公司id"""
        resp =self.client.firm_leads_employee(source="sales",signature=self.signature,t=self.t,sub_firm_ids=[255309])
        self.assertEqual(10000,resp.code)

    def test_firm_leads_employee6(self):
        """公司id不存在"""
        resp =self.client.firm_leads_employee(source="sales",signature=self.signature,t=self.t,sub_firm_ids=[25530000000000009])
        self.assertEqual(10000,resp.code)


