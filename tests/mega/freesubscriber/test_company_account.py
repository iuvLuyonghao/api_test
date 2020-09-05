# -*- coding: utf-8 -*-

import unittest
from apis.mega.freesubscriber.freesubscriber import FreesubscriberClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
import json
from qav5.utils.util import gen_rand_str
import time
from util.setroles import SetRoles

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = FreesubscriberClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestCompanyAccounts(BaseTestCase):

    def test_account_detail(self):
        """企业试用账号-详情页"""
        SetRoles().mega("huimei.tao",job_title_id=10188,role_ids="[1,8,29,11,19,33,20]")
        resp = self.client.account_detail(a_id=807232)
        self.assertEqual(10000, resp.code)
        self.assertEqual(255309, resp.data.sub_firm_id)

    def test_account_detail_id_null(self):
        """企业试用账号-ID为空或不存在"""
        resp = self.client.account_detail(a_id=None)
        self.assertEqual(-996, resp.code)


    def test_account_create(self):
        """创建企业试用账号"""
        user_name = gen_rand_str(length=3, prefix="free_ent_")
        password = gen_rand_str()
        free_subscribers = [{
            "contact_id": 1225022,
            "contact_mobile": 18100000000,
            "username": user_name,
            "password": password,
            "notes": '说点啥呢'
        }]
        free_subscriber_setting = {
            "max_project_count": 50,
            "project_per_page": 50,
            "pl_style": 1,
            "estimate_payment": 20,
            "active": 1,
            "lock_count": 35,
            "language_id": 1,
            "vip_type": 1,
            "view_all_firms": 1,
            "other_options_attrs": {
                "next_login_without_welcome": 1,
                "email_when_login": 1,
                "ip_limit": 1,
                "login_to": 1,
                "show_all_projects": 1,
                "show_project_report": 1,
                "show_all_version": 1,
                "hide_rare_role": 1,
                "max_firm_export_per_day": 30,
                "bid_index_default_show": 1,
                "default_hide_pnews": 1,
                "default_hide_pmsg": 0,
                "default_hide_pfup": [
                    1,
                    3
                ],
                "hide_project_attrs": [
                    1,
                    2
                ]
            }
        }
        login_start = int(time.time())
        login_end = login_start + 7 * 24 * 60 * 60
        sub_start = login_start
        sub_end = login_end
        subscriptions = {
            "project_resource": 1,
            "project_type_ids": [
                1,
                2
            ],
            "purchase_limit": 5,
            "base": {
                "login_start": login_start,
                "login_end": login_end,
                "sub_start": sub_start,
                "sub_end": sub_end,
                "active": 1
            },
            "project_info_flag": True,
            "project_info": {
                "country_id": [
                    8,
                    66
                ],
                "region_id": [
                    16,
                    13
                ],
                "province_id": [
                    2,
                    13,
                    3,
                    9,
                    20
                ],
                "project_category": {
                    "category_ids": [
                        20,
                        19
                    ],
                    "sub_category_ids": [
                        1901
                    ]
                },
                "project_stage_id": [
                    11,
                    12
                ],
                "projectid": "111, 222",
                "ownerid": [
                    6,
                    7
                ],
                "devid": [
                    6,
                    2
                ],
                "foreign_participation": [
                    -1,
                    5
                ],
                "aircondition": [
                    -1,
                    0
                ],
                "major": [
                    -1,
                    0
                ],
                "heating_type": [
                    0,
                    4
                ],
                "curtain_wall": [
                    -1,
                    3
                ]
            },
            "bid_info_flag": True,
            "bid_info": {
                "country_id": [
                    8
                ],
                "region_id": [
                    16,
                    13
                ],
                "province_id": [
                    2,
                    13,
                    3,
                    9,
                    20
                ],
                "product_category": [
                    10020,
                    10049,
                    10050,
                    11484,
                    10069
                ],
                "product_kw": "LED,UPS电源",
                "usage_category": [
                    20,
                    3301
                ],
                "purchase_category": [
                    10020,
                    10049,
                    10050,
                    11484,
                    10069
                ]
            }

        }
        resp = self.client.account_create(sub_firm_id=123456, free_subscribers=json.dumps(free_subscribers),
                                          free_subscriber_setting=json.dumps(free_subscriber_setting),
                                          subscriptions=json.dumps(subscriptions))
        self.assertEqual(10000, resp.code)
        self.assertEqual(123456, resp.data.sub_firm_id)
        # self.assertEqual(password, resp.data.password)
        self.assertIsNotNone(resp.data.subscriptions)
        # delete
        resp = self.client.account_del(a_id=resp.data.id)
        self.assertEqual(10000, resp.code)


    def test_account_update(self):
        """编辑企业试用账号"""
        a_id = 807232
        user_name = gen_rand_str(length=3, prefix="free_update_")
        password = gen_rand_str()
        free_subscribers = [{
            "contact_id": 1225022,
            "contact_mobile": 18100000000,
            "username": user_name,
            "password": password,
            "notes": "update here"
        }]
        free_subscriber_setting = {
            "max_project_count": 50,
            "project_per_page": 50,
            "pl_style": 1,
            "estimate_payment": 20,
            "active": 1,
            "lock_count": 35,
            "language_id": 1,
            "vip_type": 1,
            "view_all_firms": 1,
            "other_options_attrs": {
                "next_login_without_welcome": 1,
                "email_when_login": 1,
                "ip_limit": 1,
                "login_to": 1,
                "show_all_projects": 1,
                "show_project_report": 1,
                "show_all_version": 1,
                "hide_rare_role": 1,
                "max_firm_export_per_day": 30,
                "bid_index_default_show": 1,
                "default_hide_pnews": 1,
                "default_hide_pmsg": 0,
                "default_hide_pfup": [
                    1,
                    3
                ],
                "hide_project_attrs": [
                    1,
                    2
                ]
            }
        }
        login_start = int(time.time())
        login_end = login_start + 7 * 24 * 60 * 60
        sub_start = login_start
        sub_end = login_end
        subscriptions = {
            "project_resource": 0,
            "project_type_ids": [
                1,
                2
            ],
            "purchase_limit": 5,
            "base": {
                "login_start": login_start,
                "login_end": login_end,
                "sub_start": sub_start,
                "sub_end": sub_end,
                "active": 1
            },
            "project_info_flag": True,
            "project_info": {
                "country_id": [
                    8,
                    66
                ],
                "region_id": [
                    16,
                    13
                ],
                "province_id": [
                    2,
                    13,
                    3,
                    9,
                    20
                ],
                "project_category": {
                    "category_ids": [
                        20,
                        19
                    ],
                    "sub_category_ids": [
                        1901
                    ]
                },
                "project_stage_id": [
                    11,
                    12
                ],
                "projectid": "111, 222",
                "ownerid": [
                    6,
                    7
                ],
                "devid": [
                    6,
                    2
                ],
                "foreign_participation": [
                    -1,
                    5
                ],
                "aircondition": [
                    -1,
                    0
                ],
                "major": [
                    -1,
                    0
                ],
                "heating_type": [
                    0,
                    4
                ],
                "curtain_wall": [
                    -1,
                    3
                ]
            },
            "bid_info_flag": True,
            "bid_info": {
                "country_id": [
                    8
                ],
                "region_id": [
                    16,
                    13
                ],
                "province_id": [
                    2,
                    13,
                    3,
                    9,
                    20
                ],
                "product_category": [
                    10020,
                    10049,
                    10050,
                    11484,
                    10069
                ],
                "product_kw": "LED,UPS电源",
                "usage_category": [
                    20,
                    3301
                ],
                "purchase_category": [
                    10020,
                    10049,
                    10050,
                    11484,
                    10069
                ]
            }

        }
        resp = self.client.account_edit(a_id=a_id, sub_firm_id=255309, free_subscribers=json.dumps(free_subscribers),
                                        free_subscriber_setting=json.dumps(free_subscriber_setting),
                                        subscriptions=json.dumps(subscriptions))
        self.assertEqual(10000, resp.code)
        self.assertNotEqual(None,resp.data)

