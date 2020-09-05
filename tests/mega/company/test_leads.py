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
        print("tear down clean up rollback, delete sub_firm_id: %s............." %D.get_leads_data_p1.sub_firm_id)
        data = {"sub_firm_id": 197610}
        self.oracle_client.execute_no_query(sql="delete FROM leads_give_up_reasons WHERE sub_firm_id=:sub_firm_id", bindvars=data)
        pass

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













