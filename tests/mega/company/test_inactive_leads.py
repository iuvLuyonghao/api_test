# -*- coding: utf-8 -*-

import unittest
from apis.mega.company.leads import LeadsClient
from apis.mega.login.login import Login
from apis.mega.recalls.recalls import RecallsClient
from apis.mega.company.company import CompanyClient
from apis.mega.contact.search import SearchClient
from config import services
from const import RecallsBiz
from data import DataCenter as D, load_local_data
from os.path import join, abspath
import json
import time
from qav5 import log

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = LeadsClient(base_url=services.mega, access_token=cls.token)
        cls.recall_client = RecallsClient(base_url=services.mega, access_token=cls.token)
        cls.company_client = CompanyClient(base_url=services.mega, access_token=cls.token)
        cls.contact_client = SearchClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestInactiveLeads(BaseTestCase):
    def test_inactive_leads(self):
        """检查不积极leads"""
        ts = int(time.time()-60*60*24)
        resp = self.client.query_inactive_leads_list(sales_id=D.user_irene_liu.employee_id, created_date=ts)
        self.assertEqual(RecallsBiz.SUCCESS_CODE, resp.code)
        self.assertEqual(20, resp.data.per_page)
        self.assertEqual(1, resp.data.page)
        resp = self.client.query_inactive_leads_list(sales_id=D.user_irene_liu.employee_id, created_date=ts, page=2)
        self.assertEqual(2, resp.data.page)

    def test_inactive_leads_to_active(self):
        """不积极leads变为积极"""
        ts = int(time.time()-60*60*24)
        # 查询不积极leads列表
        resp = self.client.query_inactive_leads_list(sales_id=D.user_irene_liu.employee_id, created_date=ts,
                                                     sub_firm_name=D.leads_154990.sub_firm_name,
                                                     leads_type_id=D.leads_154990.leads_type_id)

        self.assertEqual(RecallsBiz.SUCCESS_CODE, resp.code)
        if len(resp.data.leads) != 0:
            sub_firm_id = resp.data.leads[0]["sub_firm_id"]
            # 添加跟进-触发积极条件
            contact = self.contact_client.contacts_list(sub_firm_id=sub_firm_id)
            contact_id = contact.data.sub_contacts[0]["id"]
            resp2 = self.recall_client.create_recall(completed_at=int(time.time()),
                                                     completed_by=D.user_irene_liu.employee_id,
                                                     appt_date=int(time.time() - 30 * 60),
                                                     employee_id=D.user_irene_liu.employee_id,
                                                     contact_by_value="phone", stage_id=14,
                                                     sub_contact_id=contact_id, sub_firm_id=sub_firm_id,
                                                    sub_stage_ids='[1,2,3]')
            self.assertEqual(10000,resp2.code)


            # 查询公司详情-leads接口
            resp3 = self.company_client.leads_info(id=sub_firm_id)
            self.assertEqual(RecallsBiz.SUCCESS_CODE, resp3.code)
            self.assertEqual(sub_firm_id, resp3.data[0]["sub_firm_id"])
            self.assertEqual(True, resp3.data[0]["active"])
