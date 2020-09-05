# -*- coding: utf-8 -*-

import unittest
from apis.mega.recalls.recalls import RecallsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from const import RecallsBiz
import json
from qav5 import log

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)
mysql = None


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_allen_wang.username, password=D.user_allen_wang.password)
        cls.token = resp.data.session_id
        cls.client = RecallsClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestRecallSearchStatement(BaseTestCase):

    def test_search_statement_valid(self):
        """员工recall 报告"""
        resp = self.client.search_statement(department_ids=D.search_stat.department_ids,
                                            branch_office_ids=D.search_stat.branch_office_ids,
                                            employee_ids=D.search_stat.employee_ids,
                                            appt_date_min=D.search_stat.appt_date_min,
                                            appt_date_max=D.search_stat.appt_date_max)
        self.assertEqual(RecallsBiz.SUCCESS_CODE, resp.code)
        self.assertEqual(440212, resp.data[0]['employee_id'])

    def test_search_statement_department_ids_null(self):
        """员工recall 报告"""
        resp = self.client.search_statement(department_ids='',
                                            branch_office_ids=D.search_stat.branch_office_ids,
                                            employee_ids=D.search_stat.employee_ids,
                                            appt_date_min=D.search_stat.appt_date_min,
                                            appt_date_max=D.search_stat.appt_date_max)
        self.assertEqual(RecallsBiz.ERROE_CODE, resp.code)
        self.assertEqual(['is invalid'], resp.data.department_ids)

    def test_search_statement_branch_ids_null(self):
        """员工recall 报告"""
        resp = self.client.search_statement(department_ids=D.search_stat.department_ids,
                                            branch_office_ids='',
                                            employee_ids=D.search_stat.employee_ids,
                                            appt_date_min=D.search_stat.appt_date_min,
                                            appt_date_max=D.search_stat.appt_date_max)
        self.assertEqual(RecallsBiz.ERROE_CODE, resp.code)
        self.assertEqual(['is invalid'], resp.data.branch_office_ids)

    def test_search_statement_appt_date_min(self):
        """员工recall 报告"""
        resp = self.client.search_statement(department_ids=D.search_stat.department_ids,
                                            branch_office_ids=D.search_stat.branch_office_ids,
                                            employee_ids=D.search_stat.employee_ids,
                                            appt_date_min=0,
                                            appt_date_max=D.search_stat.appt_date_max)
        self.assertEqual(RecallsBiz.ERROE_CODE_DATE, resp.code)
        self.assertEqual("搜的时间段太长了", resp.message)

class TestRecallSearch(BaseTestCase):
    def test_recall_search(self):
        resp=self.client.search_recall(sub_firm_ids=json.dumps([255309]))
        self.assertEqual(10000,resp.code)
