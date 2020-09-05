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
        cls.resp =cls.client.employee_firm_ids(signature="''",t=t,employee_id=1)
        cls.t=t
        cls.signature=cls.resp.data.signature

    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass


class TestEmployeeFirmIds(BaseTestCase):
    def test_employee_firm_ids(self):
        """无签名"""
        resp =self.client.employee_firm_ids(employee_id=1,signature="",t=self.t)
        self.assertEqual(-997,resp.code)
        self.assertEqual("没有签名",resp.message)
        self.assertEqual({},resp.data)

    def test_employee_firm_ids1(self):
        """签名验证不通过"""
        resp =self.client.employee_firm_ids(employee_id=1,signature="111",t=self.t)
        self.assertEqual(-997,resp.code)
        self.assertEqual("签名不匹配",resp.message)

    def test_employee_firm_ids2(self):
        """无时间戳"""
        resp =self.client.employee_firm_ids(signature="111",t="",employee_id="")
        self.assertEqual(-997,resp.code)
        self.assertEqual("没有时间戳",resp.message)

    def test_employee_firm_ids3(self):
        """正常"""
        resp =self.client.employee_firm_ids(signature=self.signature,t=self.t,employee_id=1)
        self.assertEqual(10000,resp.code)

    def test_employee_firm_ids4(self):
        """用户id不存在"""
        resp =self.client.employee_firm_ids(signature=self.signature,t=self.t,employee_id=100000000000000)
        self.assertEqual(10000,resp.code)
