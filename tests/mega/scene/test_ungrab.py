# -*- coding: utf-8 -*-
import json
import unittest, warnings
from apis.mega.leads.leads import LeadsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from util.setroles import SetRoles
import pytest
import qav5.log
from qav5.conn import OracleClient

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = LeadsClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestUnGrab(BaseTestCase):

    @pytest.mark.scene
    def test_ungrab(self):
        """
        leads空置
        设置权限->获取leads->空置leads
        :return:
        """
        r=SetRoles().mega("huimei.tao", job_title_id=10188, role_ids="[1,19,29]")
        self.assertEqual(r.code,10000)
        self.assertEqual(r.message,"success")
        resp=self.client.grab(new_sales_id=D.grab.new_sales_id1, sub_firm_id=D.grab.sub_firm_id1,
                         leads_type_id=D.grab.leads_type_id1)
        self.assertEqual(resp.code,10000)
        self.assertEqual(resp.message,"success")
        resp = self.client.ungrab(new_sales_id=D.grab.new_sales_id1, sub_firm_id=D.grab.sub_firm_id1,
                                  leads_type_id=D.grab.leads_type_id1)
        self.assertEqual(resp.code, 10000)
        self.assertEqual(resp.message,"success")

