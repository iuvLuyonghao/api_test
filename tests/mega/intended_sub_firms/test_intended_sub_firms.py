# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.intended_sub_firms.intended_sub_firms import IntendedSubFirmClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
from qav5.utils.util import gen_rand_str

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_allen_wang.username, password=D.user_allen_wang.password)
        cls.token = resp.data.session_id
        cls.client = IntendedSubFirmClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestIntendedSubFirmsSearch(BaseTestCase):

    def test_search_null(self):
        """意向客户-列表搜索"""
        resp = self.client.search(status='[]')
        self.assertEqual(10000, resp.code)
        self.assertEqual(1, resp.data.page)
        self.assertEqual(20, resp.data.per_page)
        self.assertGreaterEqual(resp.data.total, 0)
        self.assertIsNotNone(resp.data.expect_amount_total)
        self.assertIsNotNone(resp.data.expect_bid_amount_total)

    def test_search_sales_id(self):
        """意向客户-列表搜索"""
        resp = self.client.search(sales_id=D.user_allen_wang.employee_id, status='[1]')
        self.assertEqual(10000, resp.code)
        self.assertEqual(1, resp.data.page)
        self.assertEqual(20, resp.data.per_page)
        self.assertGreaterEqual(len(resp.data.list), 1)
        self.assertGreaterEqual(resp.data.total, 1)
        self.assertEqual(D.user_allen_wang.username, resp.data.list[0].get('sales_username'))
        self.assertEqual(D.user_allen_wang.employee_id, str(resp.data.list[0].get('sales_id')))
        self.assertIsNotNone(resp.data.expect_amount_total)
        self.assertIsNotNone(resp.data.expect_bid_amount_total)

    def test_edit_stage(self):
        """意向客户-编辑"""
        resp = self.client.search(sales_id=D.user_allen_wang.employee_id, status='[1]')
        i_id = resp.data.list[0].get('id')
        self.assertIsNotNone(resp.data.expect_amount_total)
        self.assertIsNotNone(resp.data.expect_bid_amount_total)
        resp = self.client.intended_sub_firms_edit(i_id=i_id, stage_id=5, level_id="1")
        self.assertEqual(10000, resp.code)


    def test_edit_other(self):
        """意向客户-编辑"""
        resp = self.client.search(sales_id=D.user_allen_wang.employee_id, status='[1]')
        i_id = resp.data.list[0].get('id')
        resp = self.client.intended_sub_firms_edit(i_id=i_id, stage_id=3, level_id=1,
                                                   expect_amount=gen_rand_str(length=5, s_type='digit'),
                                                   expect_bid_amount=gen_rand_str(length=4, s_type='digit'),
                                                   next_plan=gen_rand_str(prefix='next_'), province_ids='[3,21]',
                                                   region_ids='[13,15]', notes=gen_rand_str())
        self.assertEqual(10000, resp.code)
        self.assertEqual(i_id, resp.data.id)
        self.assertEqual(3, resp.data.stage_id)

    def test_get_next_plan(self):
        """获取下一步方案"""
        resp = self.client.search(sales_id=D.user_allen_wang.employee_id, status='[1]')
        i_id = resp.data.list[0].get('id')
        resp = self.client.get_next_plan(i_id=i_id)
        self.assertEqual(10000, resp.code)

    def test_give_up(self):
        """申请放弃"""
        resp = self.client.search(sales_id=D.user_allen_wang.employee_id, status='[1]')
        i_id = resp.data.list[0].get('id')
        resp = self.client.give_up(i_id=i_id, give_up_reason=369023)
        self.assertEqual(10000, resp.code)

    def test_approve(self):
        """审批"""
        resp = self.client.search(sales_id=D.user_allen_wang.employee_id, status='[2,3,4]')
        i_id = resp.data.list[0].get('id')
        resp = self.client.approval(i_id=i_id)
        self.assertEqual(10000, resp.code)

    def test_count_sale(self):
        """统计接口-allen.wang 销售"""
        resp = self.client.count(sales_id=D.user_allen_wang.employee_id,contact_login_count=90,rcc_share_count=90)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.confirm_order.leads_count, 0)
        self.assertGreaterEqual(resp.data.confirm_order.expect_amount_sum, 0)
        self.assertGreaterEqual(resp.data.give_up.leads_count, 0)
        self.assertGreaterEqual(resp.data.give_up.expect_amount_sum, 0)
        self.assertEqual(resp.data.contact_login_count.stage_cn,"3个不同联系人有效试用登录")
        self.assertEqual(resp.data.rcc_share_count.stage_cn,"累计产生3次有效投屏")

    def test_count_sale_lead(self):
        """统计接口-allen.wang的队长 销售队长登录"""
        resp = self.client.count(sales_id=D.user_allen_wang.sales_leader_id,contact_login_count=90,rcc_share_count=90)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.confirm_order.leads_count, 0)
        self.assertGreaterEqual(resp.data.confirm_order.expect_amount_sum, 0)
        self.assertGreaterEqual(resp.data.give_up.leads_count, 0)
        self.assertGreaterEqual(resp.data.give_up.expect_amount_sum, 0)
        self.assertEqual(resp.data.contact_login_count.stage_cn,"3个不同联系人有效试用登录")
        self.assertEqual(resp.data.rcc_share_count.stage_cn,"累计产生3次有效投屏")
