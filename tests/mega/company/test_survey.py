# -*- coding: utf-8 -*-

import unittest
from apis.mega.company.survey import SurveyClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
import json

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = SurveyClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestSurvey(BaseTestCase):

    def test_active_survey_list(self):
        """可用调研问卷列表 """
        resp = self.client.active_survey_list()
        self.assertEqual(resp.code, 10000)
        self.assertGreater(len(resp.data.list), 0)
        self.assertGreater(resp.data.total, 0)

    def test_firm_survey_url(self):
        """可用调研问卷列表 """
        resp = self.client.firm_survey_url(sub_firm_id=11446)
        self.assertEqual(resp.code, 10000)
        self.assertIsNotNone(resp.data.url)

    def test_firm_survey_url_all(self):
        """可用调研问卷列表-全部 """
        resp = self.client.firm_surveys_list()
        self.assertEqual(resp.code, 10000)
        self.assertGreater(resp.data.total, 1)

    def test_firm_survey_url_firm_id(self):
        """可用调研问卷列表-公司 """
        resp = self.client.firm_surveys_list(sub_firm_id=11446)
        self.assertEqual(resp.code, 10000)
        self.assertGreater(resp.data.total, 1)

    def test_firm_survey_url_firm_id_submit(self):
        """可用调研问卷列表-已提交 """
        resp = self.client.firm_surveys_list(sub_firm_id=11446)
        self.assertEqual(resp.code, 10000)
        self.assertGreater(resp.data.total, 1)

    def test_firm_survey_url_firm_id_(self):
        """所有调研问卷模板列表 """
        resp = self.client.firm_surveys_all()
        self.assertEqual(resp.code, 10000)
        self.assertGreaterEqual(resp.data.total, 1)
