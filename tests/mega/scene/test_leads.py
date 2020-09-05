# -*- coding: utf-8 -*-
import unittest,warnings
from apis.mega.company.leads import LeadsClient
from apis.mega.modifyauth.auth import AuthClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5.conn import OracleClient
from qav5 import log
from util.setroles import SetRoles
import pytest
file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.oracle_client = OracleClient(services.oracle['username'], services.oracle['password'],
                                         services.oracle['conn_str'])
        warnings.simplefilter('ignore',ResourceWarning)
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        data = {"sub_firm_id": 197610}
        self.oracle_client.execute_no_query(sql="delete FROM leads_give_up_reasons WHERE sub_firm_id=:sub_firm_id", bindvars=data)

class TestLeadsType(BaseTestCase):
    def test_get_leads(self):
        """
        详情页获取、分配leads
        :return:
        """
        SetRoles().mega("huimei.tao",job_title_id=10188,role_ids="[1,8,29,11,19,33,20]")
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        resp = self.client.get_leads(new_sales_id=D.get_leads_data.new_sales_id,sub_firm_id=D.get_leads_data.sub_firm_id,
                                     leads_type_id=D.get_leads_data.leads_type_id)
        self.assertEqual(resp.code, 10000)


class TestVacantLeads(BaseTestCase):

    @pytest.mark.scene
    def test_sale_releads_leads_level1_sanmi(self):
        """设置权限->登录->获取leads->释放leads"""
        r=SetRoles().mega("huimei.tao",job_title_id=D.get_leads_data_p1.job_title_id,role_ids=D.get_leads_data_p1.role_ids)
        self.assertEqual(r.code,10000)
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username="sanmi.yi", password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        rg=self.client.get_leads(new_sales_id=D.get_leads_data_p1.new_sales_id,sub_firm_id=D.get_leads_data_p1.sub_firm_id,
                              leads_type_id=D.get_leads_data_p1.leads_type_id)
        self.assertEqual(rg.code,10000)
        self.assertEqual(rg.message,'success')
        resp = self.client.release_leads(sub_firm_id=D.get_leads_data_p1.sub_firm_id,
                                         leads_type_id=D.get_leads_data_p1.leads_type_id,
                                         release_reason_id=D.get_leads_data_p1.release_reason_id,
                                         release_type_id=D.get_leads_data_p1.release_type_id)
        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.message,'success')

    @pytest.mark.scene
    def test_sale_releads_leads_level2_sanmi(self):
        """设置权限->登录->获取leads->释放leads"""
        r=SetRoles().mega("huimei.tao",job_title_id=D.get_leads_data_p1.job_title_id,role_ids=D.get_leads_data_p1.role_ids)
        self.assertEqual(r.code,10000)
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username="sanmi.yi", password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega,
                                  access_token=self.token)
        rg=self.client.get_leads(new_sales_id=D.get_leads_data_level2.new_sales_id,
                              sub_firm_id=D.get_leads_data_level2.sub_firm_id,
                              leads_type_id=10020)
        self.assertEqual(rg.code,10000)
        self.assertEqual(rg.message,'success')
        resp = login_client.get_token(username=D.user_mega.username_sanmi, password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level2.sub_firm_id,
                                         leads_type_id=10020,
                                         release_reason_id=D.get_leads_data_level2.release_reason_id,
                                         release_type_id=D.get_leads_data_p1.release_type_id)
        self.assertEqual(resp.code, 10000)
        self.assertTrue("success" in resp.message)

    @pytest.mark.scene
    def test_sale_releads_leads_level3_sanmi(self):
        """设置权限->登录->获取leads->释放leads"""
        r=SetRoles().mega("huimei.tao",job_title_id=D.get_leads_data_p1.job_title_id,role_ids=D.get_leads_data_p1.role_ids)
        self.assertEqual(r.code,10000)
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username="sanmi.yi", password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        rg=self.client.get_leads(new_sales_id=D.get_leads_data_level3.new_sales_id,sub_firm_id=D.get_leads_data_level3.sub_firm_id,
                              leads_type_id=D.get_leads_data_level3.leads_type_id)
        self.assertEqual(rg.code,10000)
        self.assertEqual(rg.message,'success')
        resp = login_client.get_token(username=D.user_mega.username_sanmi, password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level3.sub_firm_id,
                                         leads_type_id=D.get_leads_data_level3.leads_type_id,
                                         release_reason_id=D.get_leads_data_level3.release_reason_id,
                                         give_up_reason_id=D.get_leads_data_level3.give_up_reason_id,
                                         release_type_id=D.get_leads_data_p1.release_type_id,
                                         give_up_reason_note="123123")
        self.assertEqual(resp.code, 10000)
        self.assertTrue("success" in resp.message)

    @pytest.mark.scene
    def test_sale_releads_leads_level4_sanmi(self):
        """设置权限->登录->获取leads->释放leads"""
        r=SetRoles().mega("huimei.tao",job_title_id=D.get_leads_data_level4.job_title_id,role_ids=D.get_leads_data_p1.role_ids)
        self.assertEqual(r.code,10000)
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username="sanmi.yi", password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        rg=self.client.get_leads(new_sales_id=D.get_leads_data_level3.new_sales_id,sub_firm_id=D.get_leads_data_level3.sub_firm_id,
                              leads_type_id=D.get_leads_data_level3.leads_type_id)
        self.assertEqual(rg.code,10000)
        self.assertEqual(rg.message,'success')
        resp = login_client.get_token(username=D.user_mega.username_sanmi, password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level4.sub_firm_id,
                                         leads_type_id=D.get_leads_data_level4.leads_type_id,
                                         release_reason_id=D.get_leads_data_level4.release_reason_id,
                                         give_up_reason_id=D.get_leads_data_level4.give_up_reason_id,
                                         release_type_id=D.get_leads_data_p1.release_type_id)
        self.assertEqual(resp.code, 10000)
        self.assertTrue("success" in resp.message)

    @pytest.mark.scene
    def test_sale_releads_leads_level5_sanmi(self):
        """登录->获取leads->释放leads"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username="sanmi.yi", password=D.user_mega.password)
        self.assertEqual(resp.code,10000)
        self.token = resp.data.session_id
        self.client = AuthClient(base_url=services.mega, access_token=self.token)
        resp = self.client.right_roles(job_title_id=D.get_leads_data_level5.job_title_id,role_ids=D.get_leads_data_level5.role_ids)
        if resp.code==10000 and resp.message=='success':
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            rg=self.client.get_leads(new_sales_id=D.get_leads_data_level3.new_sales_id,sub_firm_id=D.get_leads_data_level3.sub_firm_id,
                                  leads_type_id=D.get_leads_data_level3.leads_type_id)
            self.assertEqual(rg.code,10000)
            self.assertEqual(rg.message,'success')
            resp = login_client.get_token(username=D.user_mega.username_sanmi, password=D.user_mega.password)
            self.token = resp.data.session_id
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level5.sub_firm_id,
                                             leads_type_id=D.get_leads_data_level5.leads_type_id,
                                             release_reason_id=D.get_leads_data_level5.release_reason_id,
                                             give_up_reason_id=D.get_leads_data_level5.give_up_reason_id,
                                             release_type_id=D.get_leads_data_p1.release_type_id)
            self.assertEqual(resp.code, 10000)
            self.assertTrue("success" in resp.message)

    @pytest.mark.scene
    def test_sale_releads_leads_level6_sanmi(self):
        """登录->获取leads->释放leads"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        self.assertEqual(resp.code,10000)
        self.token = resp.data.session_id
        self.client = AuthClient(base_url=services.mega, access_token=self.token)
        resp = self.client.right_roles(job_title_id=D.get_leads_data_level6.job_title_id,role_ids=D.get_leads_data_level6.role_ids)
        if resp.code==10000 and resp.message=='success':
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            rg=self.client.get_leads(new_sales_id=D.get_leads_data_level3.new_sales_id,sub_firm_id=D.get_leads_data_level3.sub_firm_id,
                                  leads_type_id=D.get_leads_data_level3.leads_type_id)
            self.assertEqual(rg.code,10000)
            self.assertEqual(rg.message,'success')
            resp = login_client.get_token(username=D.user_mega.username_sanmi, password=D.user_mega.password)
            self.token = resp.data.session_id
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level6.sub_firm_id,
                                             leads_type_id=D.get_leads_data_level6.leads_type_id,
                                             release_reason_id=D.get_leads_data_level6.release_reason_id,
                                             give_up_reason_id=D.get_leads_data_level6.give_up_reason_id,
                                             release_type_id=D.get_leads_data_p1.release_type_id)
            self.assertEqual(resp.code, 10000)
            self.assertTrue("success" in resp.message)

    @pytest.mark.scene
    def test_sale_releads_leads_p1_henry(self):
        """设置权限->登录->获取leads->释放leads"""
        r=SetRoles().mega("huimei.tao",job_title_id=D.get_leads_data_p1_service.job_title_id,role_ids=D.get_leads_data_p1_service.role_ids)
        self.assertEqual(r.code,10000)
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        rg=self.client.get_leads(new_sales_id=D.get_leads_data_p1_service.new_sales_id,sub_firm_id=D.get_leads_data_p1_service.sub_firm_id,
                              leads_type_id=D.get_leads_data_p1_service.leads_type_id)
        self.assertEqual(rg.code,10000)
        self.assertEqual(rg.message,'success')
        resp = login_client.get_token(username=D.user_mega.username_henry, password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        resp = self.client.release_leads(sub_firm_id=D.get_leads_data_p1_service.sub_firm_id,
                                         leads_type_id=D.get_leads_data_p1_service.leads_type_id,
                                         release_reason_id=D.get_leads_data_p1_service.release_reason_id,
                                         give_up_reason_id=D.get_leads_data_p1_service.give_up_reason_id,
                                         release_type_id=D.get_leads_data_p1.release_type_id)

        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.message,'success')

    @pytest.mark.scene
    def test_sale_releads_leads_level2_henry(self):
        """登录->获取leads->释放leads"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        self.assertEqual(resp.code,10000)
        self.token = resp.data.session_id
        self.client = AuthClient(base_url=services.mega, access_token=self.token)
        resp = self.client.right_roles(job_title_id=D.get_leads_data_level2_service.job_title_id,role_ids=D.get_leads_data_level2_service.role_ids)
        if resp.code==10000 and resp.message=='success':
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            rg=self.client.get_leads(new_sales_id=D.get_leads_data_p1_service.new_sales_id,sub_firm_id=D.get_leads_data_p1_service.sub_firm_id,
                                  leads_type_id=D.get_leads_data_p1_service.leads_type_id)
            self.assertEqual(rg.code,10000)
            self.assertEqual(rg.message,'success')
            resp = login_client.get_token(username=D.user_mega.username_henry, password=D.user_mega.password)
            self.token = resp.data.session_id
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level2_service.sub_firm_id,
                                             leads_type_id=D.get_leads_data_level2_service.leads_type_id,
                                             release_reason_id=D.get_leads_data_level2_service.release_reason_id,
                                             give_up_reason_id=D.get_leads_data_level2_service.give_up_reason_id,
                                             release_type_id=D.get_leads_data_p1.release_type_id)
            self.assertEqual(resp.code,10000)
            self.assertEqual(resp.message,'success')

    @pytest.mark.scene
    def test_sale_releads_leads_level3_henry(self):
        """登录->获取leads->释放leads"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        self.assertEqual(resp.code,10000)
        self.token = resp.data.session_id
        self.client = AuthClient(base_url=services.mega, access_token=self.token)
        resp = self.client.right_roles(job_title_id=D.get_leads_data_level3_service.job_title_id,role_ids=D.get_leads_data_level3_service.role_ids)
        if resp.code==10000 and resp.message=='success':
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            rg=self.client.get_leads(new_sales_id=D.get_leads_data_p1_service.new_sales_id,sub_firm_id=D.get_leads_data_p1_service.sub_firm_id,
                                  leads_type_id=D.get_leads_data_p1_service.leads_type_id)
            self.assertEqual(rg.code,10000)
            self.assertEqual(rg.message,'success')
            resp = login_client.get_token(username=D.user_mega.username_henry, password=D.user_mega.password)
            self.token = resp.data.session_id
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level3_service.sub_firm_id,
                                             leads_type_id=D.get_leads_data_level3_service.leads_type_id,
                                             release_reason_id=D.get_leads_data_level3_service.release_reason_id,
                                             give_up_reason_id=D.get_leads_data_level3_service.give_up_reason_id,
                                             release_type_id=D.get_leads_data_p1.release_type_id)
            self.assertEqual(resp.code,10000)
            self.assertEqual(resp.message,'success')

    @pytest.mark.scene
    def test_sale_releads_leads_level4_henry(self):
        """设置权限->登录->获取leads->释放leads"""
        r=SetRoles().mega("huimei.tao",job_title_id=D.get_leads_data_level4_service.job_title_id,role_ids=D.get_leads_data_p1.role_ids)
        self.assertEqual(r.code,10000)
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        rg=self.client.get_leads(new_sales_id=D.get_leads_data_p1_service.new_sales_id,sub_firm_id=D.get_leads_data_p1_service.sub_firm_id,
                              leads_type_id=D.get_leads_data_p1_service.leads_type_id)
        self.assertEqual(rg.code,10000)
        self.assertEqual(rg.message,'success')
        resp = login_client.get_token(username=D.user_mega.username_henry, password=D.user_mega.password)
        self.token = resp.data.session_id
        self.client = LeadsClient(base_url=services.mega, access_token=self.token)
        resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level4_service.sub_firm_id,
                                         leads_type_id=D.get_leads_data_level4_service.leads_type_id,
                                         release_reason_id=D.get_leads_data_level4_service.release_reason_id,
                                         give_up_reason_id=D.get_leads_data_level4_service.give_up_reason_id,
                                         release_type_id=D.get_leads_data_p1.release_type_id)
        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.message,'success')

    @pytest.mark.scene
    def test_sale_releads_leads_level5_henry(self):
        """登录->获取leads->释放leads"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        self.assertEqual(resp.code,10000)
        self.token = resp.data.session_id
        self.client = AuthClient(base_url=services.mega, access_token=self.token)
        resp = self.client.right_roles(job_title_id=D.get_leads_data_level5_service.job_title_id,role_ids=D.get_leads_data_level5_service.role_ids)
        if resp.code==10000 and resp.message=='success':
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            rg=self.client.get_leads(new_sales_id=D.get_leads_data_p1_service.new_sales_id,sub_firm_id=D.get_leads_data_p1_service.sub_firm_id,
                                  leads_type_id=D.get_leads_data_p1_service.leads_type_id)
            self.assertEqual(rg.code,10000)
            self.assertEqual(rg.message,'success')
            resp = login_client.get_token(username=D.user_mega.username_henry, password=D.user_mega.password)
            self.token = resp.data.session_id
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level5_service.sub_firm_id,
                                             leads_type_id=D.get_leads_data_level5_service.leads_type_id,
                                             release_reason_id=D.get_leads_data_level5_service.release_reason_id,
                                             give_up_reason_id=D.get_leads_data_level5_service.give_up_reason_id,
                                             release_type_id=D.get_leads_data_p1.release_type_id)
            self.assertEqual(resp.code,10000)
            self.assertEqual(resp.message,'success')

    @pytest.mark.scene
    def test_sale_releads_leads_level6_henry(self):
        """登录->获取leads->释放leads"""
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        self.assertEqual(resp.code,10000)
        self.token = resp.data.session_id
        self.client = AuthClient(base_url=services.mega, access_token=self.token)
        resp = self.client.right_roles(job_title_id=D.get_leads_data_level6_service.job_title_id,role_ids=D.get_leads_data_level6_service.role_ids)
        if resp.code==10000 and resp.message=='success':
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            rg=self.client.get_leads(new_sales_id=D.get_leads_data_p1_service.new_sales_id,sub_firm_id=D.get_leads_data_p1_service.sub_firm_id,
                                  leads_type_id=D.get_leads_data_p1_service.leads_type_id)
            self.assertEqual(rg.code,10000)
            self.assertEqual(rg.message,'success')
            resp = login_client.get_token(username=D.user_mega.username_henry, password=D.user_mega.password)
            self.token = resp.data.session_id
            self.client = LeadsClient(base_url=services.mega, access_token=self.token)
            resp = self.client.release_leads(sub_firm_id=D.get_leads_data_level6_service.sub_firm_id,
                                             leads_type_id=D.get_leads_data_level6_service.leads_type_id,
                                             release_reason_id=D.get_leads_data_level6_service.release_reason_id,
                                             give_up_reason_id=D.get_leads_data_level6_service.give_up_reason_id,
                                             release_type_id=D.get_leads_data_p1.release_type_id)
            self.assertEqual(resp.code,10000)
            self.assertEqual(resp.message,'success')












