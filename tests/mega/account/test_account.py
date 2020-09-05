# -*- coding: utf-8 -*-

import unittest
from apis.mega.account.account import AccountClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
import json
import time
from util.setroles import SetRoles

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = AccountClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestFreeSubscribersSearch(BaseTestCase):

    def test_free_subs_search_default(self):
        """
        free subscribes search
        :return:
        """
        resp = self.client.free_subscribers_search(sub_firm_ids="[307823]")
        self.assertEqual(resp.code, 10000)
        self.assertEqual(1, resp.data.page)
        self.assertEqual(10, resp.data.per_page)
        self.assertEqual("desc", resp.data.order[0]["updated_at"])
        self.assertGreater(resp.data.total, 0)
        self.assertIsNotNone(resp.data.list)

    def test_free_subs_search_like(self):
        """
        free subscribes keyword or name like search
        :return:
        """
        # 扬州楚门机电设备制造有限公司
        resp = self.client.free_subscribers_search(sub_firm_ids="[307823]", contact_info="151")
        self.assertEqual(resp.code, 10000)
        self.assertEqual(1, resp.data.page)
        self.assertEqual(10, resp.data.per_page)
        self.assertEqual("desc", resp.data.order[0]["updated_at"])
        self.assertGreater(resp.data.total, 0)
        self.assertIsNotNone(resp.data.list)

    def test_free_subs_search_order(self):
        """
        free subscribes search order
        :return:
        """
        # 扬州楚门机电设备制造有限公司
        resp = self.client.free_subscribers_search(sub_firm_ids="[307823]",
                                                   order="[{\"last_login_at\":\"asc\"}]")
        self.assertEqual(resp.code, 10000)
        self.assertEqual(1, resp.data.page)
        self.assertEqual(10, resp.data.per_page)
        self.assertEqual("asc", resp.data.order[0]["last_login_at"])
        self.assertGreater(resp.data.total, 0)
        self.assertIsNotNone(resp.data.list)


class TestFreeSubscribersGetMsg(BaseTestCase):
    def test_get_free_account_msg(self):
        """获取试用账号信息ID=10939，公司ID=11446"""
        resp = self.client.free_subscribers_info(account_id=10939)
        self.assertEqual(10000, resp.code)
        self.assertEqual(11446, resp.data.sub_firm_id)
        self.assertIsNotNone(resp.data.msg_content)


class TestSubscribersDetails(BaseTestCase):
    def test_get_account_detail(self):
        """获取企业正式账号详情"""

        SetRoles().mega(user="huimei.tao", job_title_id=10188, role_ids="[1,29,19,33]")
        resp = self.client.subscribers_show(a_id=D.sub_firm_id_255309.a_id)
        self.assertEqual(10000, resp.code)
        self.assertEqual(D.sub_firm_id_255309.sub_firm_id, resp.data.sub_firm_id)
        self.assertGreaterEqual(len(resp.data.subscriptions), 1)
        self.assertEqual(D.sub_firm_id_255309.created_by_name, resp.data.created_by_name)

    def test_get_account_project_view(self):
        """账号已查看项目数"""
        resp = self.client.subscribers_view_project(id=D.sub_firm_id_255309.a_id, user_type=2)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data, 0)

    def test_get_account_bid_view(self):
        """账号已查看公告数"""
        resp = self.client.subscribers_view_bid(id=D.sub_firm_id_255309.a_id, user_type=2)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data, 0)


class TestSubscribersHistory(BaseTestCase):
    def test_bid_view_history(self):
        """查看招采信息历史记录"""
        date = 1586448000
        resp = self.client.subscribers_view_bid_history(user_id=64222, user_type=2, view_date_min=date)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 1)

    def test_bid_view_history_type2(self):
        """查看招采信息历史记录"""
        date = 1586448000
        resp = self.client.subscribers_view_bid_history(user_id=64222, user_type=1, view_date_min=date)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 0)

    def test_bid_search_history_free(self):
        """查看招采搜索历史"""
        date = 1586448000
        resp = self.client.subscribers_search_histories(user_id=64222, user_type=0, search_date_min=date)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 0)

    def test_bid_search_history_fee(self):
        """查看招采搜索历史"""
        date = 1586448000
        resp = self.client.subscribers_search_histories(user_id=64222, user_type=2, search_date_min=date)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 1)
        self.assertGreaterEqual(resp.data.list[0].get("result_num"), 0)

    def test_project_search_history_fee(self):
        """查看工程信息搜索历史"""
        date = 1586448000
        resp = self.client.subscribers_search_histories(user_id=87743, user_type=2, search_date_min=date, device_type=0)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 1)
        self.assertGreaterEqual(resp.data.list[0].get("result_num"), 0)
