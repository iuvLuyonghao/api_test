# -*- coding: utf-8 -*-

import pytest
import unittest, warnings
from apis.mega.leads.leads import LeadsClient
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
        cls.client = LeadsClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestGrab(BaseTestCase):

    @pytest.mark.scene
    def test_grab(self):
        """
        leads获取 多人同时获取
        设置权限->登录allen->登录tony->同时获取
        :return:
        """
        rolesres=SetRoles().mega(user="huimei.tao", job_title_id=10005, role_ids="[1,4,5,6,8,13,30,26,27,28,29,9,10,11,12,14,15,16,18,19,20,21,31,22,23,24,25,35,36,37,32,33,34]")
        self.assertEqual(rolesres.code,10000)
        self.assertEqual(rolesres.message,"success")
        login_client = Login(base_url=services.mega)
        respallen = login_client.get_token(username="allen.wang", password="it_test123")
        resptony = login_client.get_token(username="tony.hong", password="it_test123")
        self.allentoken = respallen.data.session_id
        self.allenclient = LeadsClient(base_url=services.mega, access_token=self.allentoken)
        self.tonytoken = resptony.data.session_id
        self.tonyclient = LeadsClient(base_url=services.mega, access_token=self.tonytoken)
        resp = self.tonyclient.grab(new_sales_id=39206,sub_firm_id=255309,leads_type_id=1)
        self.assertEqual(resp.code,10000)
        #跳过禁止不积极的时间
        if resp.code !=3514:
            self.assertIn(resp.code,[10000,3515,3517])
            resp1 = self.allenclient.grab(new_sales_id=440212,sub_firm_id=255309,leads_type_id=1)
            self.assertIn(resp1.code,[10000,3515,3517])
