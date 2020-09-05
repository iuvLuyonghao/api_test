# -*- coding: utf-8 -*-

import unittest
from apis.mega.employees.employees import EmployeesClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
# from qav5 import log



class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = EmployeesClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class Employee(BaseTestCase):

    def test_employees_auth(self):
        """
        取得员工
        :return:
        """
        resp = self.client.employees_auth(scope="all")
        self.assertEqual(resp.code, 10000)

    def test_employees(self):
        """
        员工信息
        :return:
        """
        resp = self.client.employees(id=18430)
        self.assertEqual(resp.code, 10000)
        self.assertEqual("sanmi.yi",resp.data.username)

