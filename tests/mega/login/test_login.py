# -*- coding: utf-8 -*-
import unittest
from apis.mega.login.login import Login
from config import services
import qav5.log


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = Login(base_url=services.mega)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestLogin(BaseTestCase):

    def test_login(self):
        resp = self.client.get_token(username='w.deng', password='it_test123')
        # self.assertEqual()
        self.assertEqual(10000, resp.code)
        self.assertEqual("login success", resp.message)
