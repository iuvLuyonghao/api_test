# -*- coding: utf-8 -*-

import unittest
from apis.mega.recalls.recalls import RecallsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from const import RecallsBiz
from qav5.conn import OracleClient, MySQLConnectionMgr, PostGreSQLClient
from qav5 import log
import time
import json
import random

mysql = None
file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = RecallsClient(base_url=services.mega, access_token=cls.token)
        cls.oracle_client = OracleClient(services.oracle['username'], services.oracle['password'],
                                         services.oracle['conn_str'])

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestRecallSearchStatement(BaseTestCase):

    def test_search_statement_valid_wang(self):
        """create recall log"""
        sub_stages_ids = [1, ]
        sub_contact_id = random.randint(9, 9)
        sub_firm_id = random.randint(1, 3)
        resp = self.client.create_recall(completed_at=int(time.time()), completed_by=D.user_zoe_wang.employee_id,
                                         appt_date=int(time.time() - 30 * 60), employee_id=D.user_zoe_wang.employee_id,
                                         contact_by_value="rcc_share", stage_id=1,
                                         sub_stage_ids=json.dumps(sub_stages_ids),
                                         sub_contact_id=sub_contact_id, sub_firm_id=sub_firm_id)
        c_id = resp.data.id
        data = {"c_by": 0, "c_d": c_id}
        count = self.oracle_client.execute_no_query(
            sql="""update SALES_RECALLS set created_by = :c_by where id = :c_d""",
            bindvars=data)
        self.assertEqual(1, count)
        cursor = self.oracle_client.execute_query("""select * from SALES_RECALLS where ID= :id""", {"id": c_id})

        row = cursor.fetchone()

    def test_search_statement_valid_liu(self):
        """create recall log"""
        sub_stages_ids = [1, ]
        sub_contact_id = random.randint(1, 5)
        sub_firm_id = random.randint(1, 5)
        resp = self.client.create_recall(completed_at=int(time.time()), completed_by=D.user_irene_liu.employee_id,
                                         appt_date=int(time.time() - 30 * 60), employee_id=D.user_irene_liu.employee_id,
                                         contact_by_value="rcc_share", stage_id=1,
                                         sub_stage_ids=json.dumps(sub_stages_ids),
                                         sub_contact_id=sub_contact_id, sub_firm_id=255309)
        c_id = resp.data.id
        data = {"c_by": 0, "c_d": c_id}
        count = self.oracle_client.execute_no_query(
            sql="""update SALES_RECALLS set created_by = :c_by where id = :c_d""",
            bindvars=data)
        self.assertEqual(1, count)
        cursor = self.oracle_client.execute_query("""select * from SALES_RECALLS where ID= :id""", {"id": c_id})

        row = cursor.fetchone()
        print(row)

    def test_search_statement_valid_lai(self):
        """create recall log"""
        sub_stages_ids = [1, ]
        sub_contact_id = random.randint(1, 5)
        sub_firm_id = random.randint(1, 3)
        resp = self.client.create_recall(completed_at=int(time.time()), completed_by=D.user_tara_lai.employee_id,
                                         appt_date=int(time.time() - 30 * 60), employee_id=D.user_tara_lai.employee_id,
                                         contact_by_value="rcc_share", stage_id=1,
                                         sub_stage_ids=json.dumps(sub_stages_ids),
                                         sub_contact_id=sub_contact_id, sub_firm_id=sub_firm_id)
        c_id = resp.data.id
        data = {"c_by": 0, "c_d": c_id}
        count = self.oracle_client.execute_no_query(
            sql="""update SALES_RECALLS set created_by = :c_by where id = :c_d""",
            bindvars=data)
        self.assertEqual(1, count)
        cursor = self.oracle_client.execute_query("""select * from SALES_RECALLS where ID= :id""", {"id": c_id})

        row = cursor.fetchone()
        print(row)

    def test_search_statement_valid_allen(self):
        """create recall log"""
        sub_stages_ids = [1, ]
        sub_contact_id = random.randint(1, 5)
        sub_firm_id = random.randint(1, 3)
        resp = self.client.create_recall(completed_at=int(time.time()), completed_by=D.user_allen_wang.employee_id,
                                         appt_date=int(time.time() - 30 * 60),
                                         employee_id=D.user_allen_wang.employee_id,
                                         contact_by_value="rcc_share", stage_id=1,
                                         sub_stage_ids=json.dumps(sub_stages_ids),
                                         sub_contact_id=sub_contact_id, sub_firm_id=sub_firm_id)
        print(resp)
        c_id = resp.data.id
        data = {"c_by": 0, "c_d": c_id}
        count = self.oracle_client.execute_no_query(
            sql="""update SALES_RECALLS set created_by = :c_by where id = :c_d""",
            bindvars=data)
        self.assertEqual(1, count)
        cursor = self.oracle_client.execute_query("""select * from SALES_RECALLS where ID= :id""", {"id": c_id})

        row = cursor.fetchone()
        print(row)

    def test_search_statement_valid_amos(self):
        """create recall log"""
        sub_stages_ids = [1, ]
        sub_contact_id = random.randint(1, 5)
        sub_firm_id = random.randint(1, 3)
        resp = self.client.create_recall(completed_at=int(time.time()), completed_by=D.user_amos_sun.employee_id,
                                         appt_date=int(time.time() - 30 * 60), employee_id=D.user_allen_wang.employee_id,
                                         contact_by_value="rcc_share", stage_id=1,
                                         sub_stage_ids=json.dumps(sub_stages_ids),
                                         sub_contact_id=sub_contact_id, sub_firm_id=sub_firm_id)
        c_id = resp.data.id
        data = {"c_by": 0, "c_d": c_id}
        count = self.oracle_client.execute_no_query(
            sql="""update SALES_RECALLS set created_by = :c_by where id = :c_d""",
            bindvars=data)
        self.assertEqual(1, count)
        cursor = self.oracle_client.execute_query("""select * from SALES_RECALLS where ID= :id""", {"id": c_id})

        row = cursor.fetchone()
        print(row)
