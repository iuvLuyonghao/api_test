# -*- coding: utf-8 -*-

import unittest
from config import services
from apis.mega.login.login import Login
from data import DataCenter as D, load_local_data
from apis.mega.lock.lock import LockClient
import json
from util.setroles import SetRoles
import pytest
from os.path import join, abspath

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)

import qav5.log

class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass


    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass

@unittest.skip("解锁现在走基础服务了，废弃")
class TestLockUnlock(BaseTestCase):
    @pytest.mark.scene
    def test_lock_unlock(self):
        #无角色解锁
        """设置权限->登录->解锁"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        resp = client.unlock(id=87684)
        respjson=json.loads(resp.text)
        self.assertEqual(-997,respjson["code"])
        self.assertEqual('error',respjson["message"])

    @pytest.mark.scene
    def test_lock_unlock1(self):
        #设置权限为高级解锁人，去设置非自己工程信息的leads的锁定
        """设置权限->登录->解锁"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])

    @pytest.mark.scene
    def test_lock_unlock2(self):
        #设置权限为高级解锁人，去设置非自己工程信息的leads的锁定
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])

    @pytest.mark.scene
    def test_lock_unlock3(self):
        #设置权限为高级解锁人，去设置自己工程信息的leads的锁定
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])
        #普通解锁，解锁自己工程信息的leads
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,26,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        resp = client.unlock(id=87684)
        respjson=json.loads(resp.text)
        self.assertEqual(-997,respjson["code"])
        self.assertEqual('error',resjson["message"])

    @pytest.mark.scene
    def test_lock_unlock4(self):
        #设置权限为高级解锁人，去设置非自己工程信息的leads的锁定
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])
        #基础解锁，解锁非自己工程信息的leads
        """设置权限->登录->解锁"""
        SetRoles().mega(user="sanmi.yi",job_title_id=10188,role_ids="[1,27,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        resp = client.unlock(id=87684)
        res=json.loads(resp.text)
        self.assertEqual(-997,res["code"])
        self.assertEqual('error',resjson["message"])

    @pytest.mark.scene
    def test_lock_unlock5(self):
        #设置权限为高级解锁人，去设置非自己工程信息的leads的锁定
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])
        #订阅解锁，解锁非自己工程信息的leads
        """设置权限->登录->解锁"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,28,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        resp = client.unlock(id=87684)
        respjson=json.loads(resp.text)
        self.assertEqual(-997,respjson["code"])
        self.assertEqual('error',resjson["message"])

    @pytest.mark.scene
    def test_lock_unlock7(self):
        #设置权限为高级解锁人，去设置非自己工程信息的leads的锁定
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])

    @pytest.mark.scene
    def test_lock_unlock8(self):
        #设置权限为高级解锁人，去设置非自己工程信息的leads的锁定
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])

    @pytest.mark.scene
    def test_lock_unlock9(self):
        #设置权限为高级解锁人，去设置非自己工程信息的leads的锁定
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])

    @pytest.mark.scene
    def test_lock_unlock10(self):
        #设置权限为高级解锁人，去设置非自己工程信息的leads的锁定
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])


    @pytest.mark.scene
    def test_lock_unlock11(self):
        #设置权限为高级解锁人，去设置非自己工程信息的leads的锁定
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,29,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        res=client.lock(id=87684)
        resjson=json.loads(res.text)
        self.assertEqual(-997,resjson["code"])
        self.assertEqual('error',resjson["message"])

    @pytest.mark.scene
    def test_lock_unlock999(self):
        #设置权限为特殊解锁人并锁定自己的工程信息leads
        """设置权限->登录->锁定"""
        r=SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,30,32,33,34,20]")
        self.assertEqual(10000,r.code)
        self.assertEqual(True,r.data.result)
        self.assertEqual('success',r.message)
        client=start_client()
        client.lock(id=1359)
        rolelist=[26,27,28,29]
        for role in rolelist:
            SetRoles().mega(user="huimei.tao",job_title_id=10188,role_ids="[1,%s]" %role)
            client=start_client()
            resp =client.unlock(id=1359)
            res=json.loads(resp.text)
            self.assertEqual(10000,res["code"])
            self.assertEqual('success',res["message"])

def start_client():
    login_clinet = Login(base_url=services.mega)
    resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
    token = resp.data.session_id
    client = LockClient(base_url=services.mega, access_token=token)
    return client
