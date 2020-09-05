# -*- coding: utf-8 -*-

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

    def test_grab(self):
        """
        leads获取
        :return:
        """
        resp = self.client.grab(new_sales_id=D.grab.new_sales_id,sub_firm_id=D.grab.sub_firm_id,leads_type_id=D.grab.leads_type_id)
        self.assertEqual(resp.code, -995)

    def test_grab1(self):
        """
        leads获取
        :return:
        """
        resp = self.client.grab(new_sales_id=D.grab.new_sales_id1,sub_firm_id=D.grab.sub_firm_id,leads_type_id=D.grab.leads_type_id)
        self.assertEqual(resp.code, -995)

    def test_grab2(self):
        """
        leads获取
        :return:
        """
        resp = self.client.grab(new_sales_id=D.grab.new_sales_id1,sub_firm_id=D.grab.sub_firm_id1,leads_type_id=D.grab.leads_type_id)
        self.assertEqual(resp.code, -995)

    def test_grab3(self):
        """
        leads获取
        :return:
        """
        resp = self.client.grab(new_sales_id=D.grab.new_sales_id1,sub_firm_id=D.grab.sub_firm_id1,leads_type_id=D.grab.leads_type_id1)
        self.assertEqual(resp.code, 10000)

    def test_grab4(self):
        """
        leads获取 多人同时获取
        :return:
        """
        rolesres=SetRoles().mega(user="w.deng", job_title_id=10188, role_ids="[1,4,5,6,8,13,30,26,27,28,29,9,10,11,12,14,15,16,18,19,20,21,31,22,23,24,25,35,36,37,32,33,34]")
        self.assertEqual(rolesres.code,10000)
        new_sales_ids=[39206,440212]
        for new_sales_id in new_sales_ids:
            resp = self.client.grab(new_sales_id=new_sales_id,sub_firm_id=255309,leads_type_id=1)
            self.assertEqual(resp.code, 10000)