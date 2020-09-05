# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.monthly_reports.monthly_reports import MothlyReportsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
import pytest
import time
import qav5.log
file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_client = Login(base_url=services.mega)
        resp = cls.login_client.get_token(username="tony.hong", password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = MothlyReportsClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestMonthlyReports(BaseTestCase):

    @pytest.mark.scene
    def test_monthly_reports_audit(self):
        """添加月报->审核->添加预计到账客户->编辑预计到账客户->删除预计到账客户"""

        respadd = self.client.monthly_reports_edit(submit_type=2,personal_target=9999,bid_personal_target=888.22,order_income_target=4545.11,
                                                order_income_bid_target=1111.9999999999)
        self.assertEqual(respadd.code,10000)
        self.assertEqual(respadd.data.status,2)
        self.assertEqual(respadd.data.order_income_target,'4545.11')
        resp = self.login_client.get_token(username="felix.pan", password=D.user_mega.password)
        client = MothlyReportsClient(base_url=services.mega, access_token=resp.data.session_id)
        respaudit=client.monthly_reports_audit(id=respadd.data.id,status=1,note="")
        self.assertEqual(respaudit.code,10000)
        interested_customer='[{ "sub_firm_id": 1,\
                                "leads_type_id": 1,\
                                "subscription_region": "",\
                                "order_income_expect": "",\
                                "bid_order_income_expect": "",\
                                "order_years": "",\
                                "status_now": "",\
                                "sales_date_expect": "",\
                                "sales_date_expect_min": 1}]'
        respaic=self.client.monthly_reports_interested_customer(monthly_report_id=respadd.data.id,interested_customer=interested_customer)
        self.assertEqual(respaic.code,10000)
        self.assertEqual(respaic.data[0]['sub_firm_id'],1)
        respaicup=self.client.monthly_reports_interested_customer_update(id=respaic.data[0]['id'],sales_date_expect=time.time(),sales_date_expect_min=time.time())
        self.assertEqual(respaicup.code,10000)
        respaicdel=self.client.monthly_reports_interested_customer_delete(id=respaic.data[0]['id'])
        self.assertEqual(respaicdel.code,10000)


    @pytest.mark.scene
    def test_monthly_reports_audit1(self):
        """添加月报->审核->添加预计到账客户->编辑预计到账客户->删除预计到账客户"""

        respadd = self.client.monthly_reports_edit(id=6130,submit_type=2,personal_target=9999,bid_personal_target=888.22,order_income_target=4545.11,
                                                   order_income_bid_target=1111.9999999999)
        self.assertEqual(respadd.code,10000)
        self.assertEqual(respadd.data.status,2)
        self.assertEqual(respadd.data.order_income_target,'4545.11')
        resp = self.login_client.get_token(username="felix.pan", password=D.user_mega.password)
        client = MothlyReportsClient(base_url=services.mega, access_token=resp.data.session_id)
        respaudit=client.monthly_reports_audit(id=respadd.data.id,status=1,note="")
        self.assertEqual(respaudit.code,10000)
        interested_customer='[{ "sub_firm_id": 1,\
                                "leads_type_id": 1,\
                                "subscription_region": "",\
                                "order_income_expect": "",\
                                "bid_order_income_expect": "",\
                                "order_years": "",\
                                "status_now": "",\
                                "sales_date_expect": "",\
                                "sales_date_expect_min": 1}]'
        respaic=self.client.monthly_reports_interested_customer(monthly_report_id=respadd.data.id,interested_customer=interested_customer)
        self.assertEqual(respaic.code,10000)
        self.assertEqual(respaic.data[0]['sub_firm_id'],1)
        respaicup=self.client.monthly_reports_interested_customer_update(id=respaic.data[0]['id'],sales_date_expect=time.time(),sales_date_expect_min=time.time())
        self.assertEqual(respaicup.code,10000)
        respaicdel=self.client.monthly_reports_interested_customer_delete(id=respaic.data[0]['id'])
        self.assertEqual(respaicdel.code,10000)




