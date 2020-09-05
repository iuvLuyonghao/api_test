# -*- coding: utf-8 -*-

import unittest
from apis.mega.company.leads import LeadsClient
from apis.mega.login.login import Login
from config import services
from const import RecallsBiz
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
from util.setroles import SetRoles

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username_irene, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = LeadsClient(base_url=services.mega, access_token=cls.token)
        # warnings.simplefilter('ignore',ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class BaseTestCase2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_allen_wang.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = LeadsClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestDelayLeads(BaseTestCase):
    def test_delay_leads_project_info(self):
        """延期leads-leads ID不存在"""
        SetRoles().mega(user="huimei.tao",job_title_id=10005,role_ids=[1,2,3,5,13,29,11,20,31,33])
        resp = self.client.delay_leads(leads_id=1, extend_months=1)
        self.assertEqual(RecallsBiz.ERROE_CODE_NO_DATA, resp.code)

    def test_delay_leads_project_info_invalid(self):
        """延期leads_超出三次"""
        SetRoles().mega(user="huimei.tao",job_title_id=10005,role_ids=[1,2,3,5,13,29,11,20,31,33])
        resp = self.client.delay_leads(leads_id=14705, extend_months=1)
        self.assertEqual(3999, resp.code)
        self.assertEqual(RecallsBiz.Delay_OverLimit, resp.message)


class TestApplyDealyLeads(BaseTestCase2):

    def test_apply_delay_leads_over_time_bid(self):
        """招采leads-申请延期leads-超过三次"""

        resp = self.client.apply_delay_leads(leads_id=17263, to_id=13703, apply_note="超过三次")
        print(resp)
        self.assertEqual(3998, resp.code)


    def test_apply_delay_leads_over_time_project_info(self):
        """招采leads-申请延期leads-超过四次"""
        resp = self.client.apply_delay_leads(leads_id=17263, to_id=13703, apply_note="超过4次")
        self.assertEqual(3998, resp.code)

