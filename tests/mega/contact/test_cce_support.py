# -*- coding: utf-8 -*-

import unittest
from apis.mega.contact.cce_support import CCESupportClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log

from util.setroles import SetRoles

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = CCESupportClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestCCESupport(BaseTestCase):

    @unittest.skip("这个接口太慢了先跳过")
    def test_cce_support(self):
        """
        提交cce support task
        """
        SetRoles().mega("huimei.tao", job_title_id=10188, role_ids="[5]")
        resp = self.client.cce_support_url(contact_id=97583, sub_firm_id=14621)
        self.assertEqual(resp.code, 10000)
        self.assertIsNotNone(resp.data.url)
