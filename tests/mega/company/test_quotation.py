# -*- coding:utf-8 -*-
import unittest
from apis.mega.company.quotation import QuotationClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
from qav5.utils.util import gen_rand_str
import json

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)
global t, u
fid = D.leads_154990.sub_firm_id


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = QuotationClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestQuotationClient(BaseTestCase):

    def test_quotation_a_info01(self):
        """页面基本信息-首次访问不需token"""
        resp = self.client.quotation_a_info(firm_id=fid, token=None)
        self.assertEqual(10000, resp.code)
        self.assertEqual(fid, resp.data.sub_firm_id)
        self.assertEqual(0, resp.data.user_options.level)
        self.assertEqual(1, resp.data.user_options.type)
        global t, u
        t = resp['data']['token']
        u = resp['data']['user_options']

    def test_quotation_a_info02(self):
        """页面基本信息-添加token"""
        resp = self.client.quotation_a_info(firm_id=fid, token=t)
        self.assertEqual(10000, resp.code)
        self.assertEqual(t, resp.data.token)
        self.assertEqual(fid, int(resp.data.sub_firm_id))
        self.assertEqual(0, resp.data.user_options.level)
        self.assertEqual(1, resp.data.user_options.type)

    def test_quotation_calculate(self):
        """申请开始统计"""
        resp = self.client.quotation_calculate(token=t, user_options=u, firm_id=fid)
        self.assertEqual(10000, resp.code)

    def test_quotation_calculate_err01(self):
        """token失效"""
        resp = self.client.quotation_calculate(token=23333, user_options=u, firm_id=fid)
        self.assertEqual(1650, resp.code)

    def test_quotation_calculate_err02(self):
        """不传token"""
        resp = self.client.quotation_calculate(token=None, user_options=u, firm_id=fid)
        self.assertEqual(-995, resp.code)

    def test_quotation_calculate_err03(self):
        """不传user_option"""
        resp = self.client.quotation_calculate(token=t, user_options=None, firm_id=fid)
        self.assertEqual(-995, resp.code)


class TestQuotationList(BaseTestCase):

    def test_quotation_list(self):
        """创建报价书方案"""
        employee_ids = '[1]'
        resp = self.client.quotation_settings(employee_ids=employee_ids, order='[{"updated_at":"desc"}]', page=1,
                                              per_page=20)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.total, 1)

    def test_create_quotation_settings(self):
        """创建报价书方案-->查询报价书列表"""
        employee_id = 1
        setting_name = gen_rand_str(prefix='temp_')
        payload = {"pl_style": 0}
        resp = self.client.quotation_settings_create(employee_id=employee_id, setting_name=setting_name,
                                                     setting_payload=json.dumps(payload))
        self.assertEqual(10000, resp.code)
        resp_list = self.client.quotation_settings(employee_ids='[1]', order='[{"updated_at":"desc"}]', page=1,
                                                   per_page=50)
        self.assertEqual(10000, resp_list.code)
        self.assertEqual(setting_name, resp_list.data.list[0]['setting_name'])
        id = resp_list.data.list[0]['id']
        resp = self.client.quotation_delete(id=id)
        self.assertEqual(10000, resp.code)
