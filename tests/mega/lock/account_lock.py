# -*- coding: utf-8 -*-

import unittest
from apis.basic_services.httpgrpc.account.account import AccountClient
from config import services
from util.rcc_phone import creat_phone as cp
from util.client_database import QureySqls
import datetime


class BaseTestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = AccountClient(base_url=services.httprpc)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass


class Account:

    def __init__(self):
        self.client = AccountClient(base_url=services.httprpc)

    def account_lock(self, person_user_id,lock_count):
        """锁定账号"""
        resp = self.client.account_lock(person_user_id=person_user_id, lock_count=lock_count, lock_reason="test lock")
        return resp
    def account_unlock(self,person_user_id,unlock_by):
        resp = self.client.account_unlock(person_user_id=person_user_id, unlock_by=unlock_by)
        return resp

account = Account()
class TestAccountLock(BaseTestCases):
    def test_lock30(self):
        """15711110023"""
        account.account_lock(364126,30)
    def test_lock35(self):
        account.account_lock(364126,35)
    def test_lock36(self):
        account.account_lock(364126,36)
    def test_lock37(self):
        account.account_lock(364126,37)
    def test_lock999(self):
        account.account_lock(364126,999)
    def test_unlock(self):
        account.account_unlock(364126,4)

