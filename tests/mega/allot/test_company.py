#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import pytest
from  apis.mega.company.company import CompanyClient
from apis.mega.login.login import Login
from config import services
from util import tag
from random import randint
from os.path import join, abspath
import qav5.log
from data import DataCenter as D, load_local_data


class BaseTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        print(services.mega)
        if "dev" in services.mega:
            file = abspath(join(__file__, "../../test.json"))
            load_local_data(data_file=file)
            resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        else:
            resp = login_client.get_token(username="info.test", password="j828803")
        cls.token = resp.data.session_id
        cls.client = CompanyClient(base_url=services.mega, access_token=cls.token)


    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass



@tag.smoke
class TestCompany(BaseTestCases):

    def test_leads_info(self):
        """获取账号分配权限信息"""
        resp = self.client.leads_info(id=255309)
        self.assertEqual(10000, resp.code)


