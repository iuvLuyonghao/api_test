# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.jurisdiction.jurisdiction import JurisdictionClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = JurisdictionClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestRightRoles(BaseTestCase):

    def test_right_roles(self):
        """
        职位对应的权限
        :return:
        """
        resp = self.client.right_roles(job_title_id=D.right_roles.job_title_id)
        self.assertEqual(resp.code, 10000)

    def test_right_roles1(self):
        """
        职位对应的权限
        :return:
        """
        resp = self.client.right_roles(job_title_id=D.right_roles.job_title_id1)
        self.assertEqual(resp.code, 10000)

    def test_right_roles2(self):
        """
        职位对应的权限
        :return:
        """
        resp = self.client.right_roles(job_title_id=D.right_roles.job_title_id2)
        self.assertEqual(resp.code, -995)

    def test_right_roles3(self):
        """
        职位对应的权限
        :return:
        """
        resp = self.client.right_roles(job_title_id=D.right_roles.job_title_id3)
        self.assertEqual(resp.code, 10000)