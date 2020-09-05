# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.company.company import CompanyClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from util.setroles import SetRoles

import time
import pytest
from util.setroles import SetRoles
import qav5.log
import json
from util.myencoder import MyEncoder

file = abspath(join(__file__, "../../test.json"))
print(file)
load_local_data(data_file=file)
class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = CompanyClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestCreateSubFirms(BaseTestCase):

    @pytest.mark.scene
    def test_create_sub_firms(self):
        """设置权限->创建公司->搜索是否创建成功"""
        firm_names='[{"name":"内蒙古小飞侠公司","remark":"1111","reason":"","repeated":"false"}]'
        SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,8,29,35,36]")
        respfirms=self.client.create_sub_firms(firm_names=firm_names,home_country_id=D.create_sub_firms.home_country_id,country_id=D.create_sub_firms.country_id)
        self.assertEqual(10000,respfirms.code)
        self.assertEqual("内蒙古小飞侠公司(1111)",respfirms.data.firm_name)
        respsearch=self.client.simple_search(search_name=respfirms.data.firm_name)
        self.assertEqual(10000,respsearch.code)
        self.assertEqual(1,respsearch.data.page)
        self.assertEqual(10,respsearch.data.per_page)

    @pytest.mark.scene
    def test_get_firms_info(self):
        """设置权限->创建公司->获取公司详情"""
        firm_names='[{"name":"内蒙古小飞侠公司","remark":"1111","reason":"","repeated":"false"}]'
        SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,8,29,35,36]")
        respfirms=self.client.create_sub_firms(firm_names=firm_names,home_country_id=D.create_sub_firms.home_country_id,country_id=D.create_sub_firms.country_id)
        self.assertEqual(10000,respfirms.code)
        self.assertEqual("内蒙古小飞侠公司(1111)",respfirms.data.firm_name)
        respfirmsinfo=self.client.sub_firms_detail(firm_id=respfirms.data.id)
        self.assertEqual(10000,respfirmsinfo.code)
        self.assertEqual("内蒙古小飞侠公司(1111)",respfirmsinfo.data.firm_name)
        self.assertEqual(respfirms.data.id,respfirmsinfo.data.id)



