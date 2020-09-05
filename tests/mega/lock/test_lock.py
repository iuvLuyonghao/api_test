# -*- coding: utf-8 -*-

import unittest
from config import services
from os.path import join, abspath
from apis.mega.login.login import Login
from data import DataCenter as D, load_local_data
from apis.mega.lock.lock import LockClient
import json
from util.setroles import SetRoles
import qav5.log
from os.path import join, abspath

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)

class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass


    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass


@unittest.skip("这是mega的锁与解锁，已经废弃了")
class TestApplyUnlock(BaseTestCase):
    def test_apply_unlock(self):
        """

        :return:
        """
        client=start_client()
        resp = client.apply_unlock(id=70974)
        res=json.loads(resp.text)
        self.assertEqual(7003,res["code"])
@unittest.skip("这是mega的锁与解锁，已经废弃了")
class TestOptionAndCheck(BaseTestCase):
    def test_options_and_check(self):
        """

        :return:
        """
        client=start_client()
        resp = client.options_and_check(id=10068)
        res=json.loads(resp.text)
        self.assertEqual(10000,res["code"])


def start_client():
    login_clinet = Login(base_url=services.mega)
    resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
    token = resp.data.session_id
    client = LockClient(base_url=services.mega, access_token=token)
    return client
