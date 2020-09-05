# -*- coding: utf-8 -*-
import random
import unittest
from apis.mega.account.personal_account import PersonalAccountClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from qav5 import log
from qav5.utils.util import gen_rand_str
import time
from random import randint
from util.rcc_phone import creat_phone as cp
from qav5.conn import PostGreSQLClient
import os

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_clinet = Login(base_url=services.mega)
        resp = login_clinet.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = PersonalAccountClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.pg_client = PostGreSQLClient(host=services.pg['host'], port=services.pg["port"], database="leads2018",
                                         user=services.pg['username'],
                                         password=services.pg['password'])
        # cls.pg_client.execute_no_query(sql="DELETE FROM person.person_users WHERE sub_firm_id=255309 and package_type=2",bindvar="tester")
        cls.pg_client.execute_no_query(sql="DELETE FROM person_user_mobiles WHERE id in (SELECT mobile_id FROM person_users WHERE sub_firm_id =169783)",bindvar="tester")
        cls.pg_client.execute_no_query(sql="DELETE FROM person_users WHERE sub_firm_id =169783",bindvar="tester")
        cls.pg_client.disconnect()


class TestSubContactsOptions(BaseTestCase):

    def test_sub_contacts_options_sub_firm_id(self):
        """联系人搜索选项-只传sub_firm_id"""
        resp = self.client.sub_contacts_options(sub_firm_id=D.sub_contact_40188.sub_firm_id)
        self.assertTrue(10000, resp.code)
        self.assertTrue(D.sub_contact_40188.sub_contact_id, resp.data.results[0]["id"])
        self.assertTrue(D.sub_contact_40188.contact_name, resp.data.results[0]["contact_name"])
        self.assertTrue(D.sub_contact_40188.sub_firm_id, resp.data.results[0]["sub_firm_id"])
        self.assertTrue(D.sub_contact_40188.mobile, resp.data.results[0]["mobile"])

    def test_sub_contacts_options_sub_firm_id_search_name(self):
        """联系人搜索选项-只传sub_firm_id, search_name 名字"""
        resp = self.client.sub_contacts_options(sub_firm_id=D.sub_contact_40188.sub_firm_id, search_name="仲")
        self.assertTrue(10000, resp.code)
        self.assertTrue(D.sub_contact_40188.sub_contact_id, resp.data.results[0]["id"])
        self.assertTrue(D.sub_contact_40188.contact_name, resp.data.results[0]["contact_name"])
        self.assertTrue(D.sub_contact_40188.sub_firm_id, resp.data.results[0]["sub_firm_id"])
        self.assertTrue(D.sub_contact_40188.mobile, resp.data.results[0]["mobile"])

    def test_sub_contacts_options_sub_firm_id_search_name_phone(self):
        """联系人搜索选项-只传sub_firm_id, search_name 手机号"""
        resp = self.client.sub_contacts_options(sub_firm_id=D.sub_contact_40188.sub_firm_id,
                                                search_name=D.sub_contact_40188.mobile)
        self.assertTrue(10000, resp.code)
        self.assertTrue(D.sub_contact_40188.sub_contact_id, resp.data.results[0]["id"])
        self.assertTrue(D.sub_contact_40188.contact_name, resp.data.results[0]["contact_name"])
        self.assertTrue(D.sub_contact_40188.sub_firm_id, resp.data.results[0]["sub_firm_id"])
        self.assertTrue(D.sub_contact_40188.mobile, resp.data.results[0]["mobile"])

    def test_sub_contacts_options_sub_firm_id_sub_contact_id(self):
        """联系人搜索选项-只传sub_firm_id, sub_contact_id"""
        resp = self.client.sub_contacts_options(sub_firm_id=26231, sub_contact_id=40188)
        self.assertTrue(10000, resp.code)
        self.assertTrue(D.sub_contact_40188.sub_contact_id, resp.data.results[0]["id"])
        self.assertTrue(D.sub_contact_40188.contact_name, resp.data.results[0]["contact_name"])
        self.assertTrue(D.sub_contact_40188.sub_firm_id, resp.data.results[0]["sub_firm_id"])
        self.assertTrue(D.sub_contact_40188.mobile in resp.data.results[0]["mobiles"])

    def test_sub_contacts_options_sub_firm_id_search_name_sub_contact_id(self):
        """联系人搜索选项-只传sub_firm_id,search_name,sub_contact_id"""
        resp = self.client.sub_contacts_options(sub_firm_id=26231, sub_contact_id=40188, search_name="仲")
        self.assertTrue(10000, resp.code)
        self.assertTrue(D.sub_contact_40188.sub_contact_id, resp.data.results[0]["id"])
        self.assertTrue(D.sub_contact_40188.contact_name, resp.data.results[0]["contact_name"])
        self.assertTrue(D.sub_contact_40188.sub_firm_id, resp.data.results[0]["sub_firm_id"])
        self.assertTrue(["13700000000"], resp.data.results[0]["mobiles"])
        self.assertTrue(D.sub_contact_40188.mobile in resp.data.results[0]["mobiles"])


class TestUserSearch(BaseTestCase):
    def test_user_search_exist(self):
        """查询账号-手机号"""
        moblie = gen_rand_str(length=8, prefix="130", s_type="digit")
        resp = self.client.sub_user_search(mobile=moblie)
        self.assertEqual(10000, resp.code)

    def test_user_search_exist1(self):
        """查询账号-手机号"""
        resp = self.client.sub_user_search(mobile=D.sub_contact_40188.mobile)
        self.assertEqual(5002, resp.code)
        self.assertEqual("该手机号已存在对应试用账号", resp.message)

    def test_user_search_sub_firm_id(self):
        """查询账号-手机号和sub_frim_id"""
        resp = self.client.sub_user_search(mobile=D.sub_contact_40188.mobile,
                                           sub_firm_id=D.sub_contact_40188.sub_firm_id)
        self.assertEqual(5002, resp.code)
        self.assertEqual("该手机号已存在对应试用账号", resp.message)


class TestUserCreate(BaseTestCase):
    def test_app_users_create_dup(self):
        """创建账号-重复手机号"""
        sub_start = int(time.time())
        sub_end = int(time.time() + 30 * 24 * 60 * 60)
        resp = self.client.app_users_create(mobile="13700000005", name=D.sub_contact_40188.contact_name,
                                            user_department="",
                                            email=D.sub_contact_40188.email,
                                            sub_firm_id=D.sub_contact_40188.sub_firm_id,
                                            sub_contact_id=D.sub_contact_40188.sub_contact_id,
                                            sub_start=sub_start, sub_end=sub_end, login_start=sub_start,
                                            login_end=sub_end, package_type=1, subs={})
        self.assertEqual(10000, resp.code)

    def test_app_users_create_mobile_null(self):
        """创建账号-手机号为空"""
        sub_start = int(time.time())
        sub_end = int(time.time() + 30 * 24 * 60 * 60)
        resp = self.client.app_users_create(mobile="", name=D.sub_contact_40188.contact_name, user_department="",
                                            email=D.sub_contact_40188.email,
                                            sub_firm_id=D.sub_contact_40188.sub_firm_id,
                                            sub_contact_id=D.sub_contact_40188.sub_contact_id,
                                            sub_start=sub_start, sub_end=sub_end, login_start=sub_start,
                                            login_end=sub_end, package_type=11, subs={})
        self.assertEqual(-995, resp.code)

    def test_app_users_create_valid_trail(self):
        """创建账号-11位手机号"""
        sub_start = int(time.time())
        sub_end = int(time.time() + 30 * 24 * 60 * 60)
        moblie = gen_rand_str(length=8, prefix="188", s_type="digit")
        name = gen_rand_str(length=2, prefix="试用账号_")
        resp = self.client.app_users_create(mobile=moblie, name=name, user_department="",
                                            email=D.sub_contact_40188.email,
                                            sub_firm_id=D.sub_contact_40188.sub_firm_id,
                                            sub_contact_id=D.sub_contact_40188.sub_contact_id,
                                            sub_start=sub_start, sub_end=sub_end, login_start=sub_start,
                                            login_end=sub_end, package_type=13, subs={})
        self.assertEqual(10000, resp.code)
        self.assertEqual('success', resp.message)

    def test_app_users_create_valid_fee(self):
        """创建账号-11位手机号"""
        sub_start = int(time.time())
        sub_end = int(time.time() + 30 * 24 * 60 * 60)
        moblie = gen_rand_str(length=8, prefix="177", s_type="digit")
        name = gen_rand_str(length=2, prefix="正式账号_")
        package_type = random.choice([1, 2, 3, 31])  # 1免费 2基础 3高级 31委任状 13试用
        resp = self.client.app_users_create(mobile=moblie, name=name, user_department="",
                                            email=D.sub_contact_40188.email,
                                            sub_firm_id=D.sub_contact_40188.sub_firm_id,
                                            sub_contact_id=D.sub_contact_40188.sub_contact_id,
                                            sub_start=sub_start, sub_end=sub_end, login_start=sub_start,
                                            login_end=sub_end, package_type=package_type, subs={})
        self.assertEqual(10000, resp.code)
        self.assertEqual('success', resp.message)


class TestUserList(BaseTestCase):

    def test_user_list_sub_firm_id(self):
        """个人账号列表-只传firm_id"""
        resp = self.client.app_user_list(sub_firm_id=D.sub_contact_40188.sub_firm_id)
        self.assertEqual(-995, resp.code)

    def test_user_list_package_type(self):
        """个人账号列表-只传package_type"""
        resp = self.client.app_user_list(package_types='[13]')
        self.assertEqual(-995, resp.code)

    def test_user_list_package_type_sub_firm_id(self):
        """个人账号列表-传firm_id和package_type"""
        resp = self.client.app_user_list(package_types='[13]', sub_firm_id=D.sub_contact_40188.sub_firm_id)
        self.assertEqual(10000, resp.code)

    def test_user_list_searchname_account(self):
        """个人账号列表-名字模糊搜索"""
        searchname = '个人账号_'
        resp = self.client.app_user_list(package_types='[13]', sub_firm_id=D.sub_contact_40188.sub_firm_id,
                                         search_name=searchname)
        self.assertEqual(10000, resp.code)

    def test_user_list_searchname_mobile(self):
        """个人账号列表-手机号模糊搜索"""
        searchname = '166'
        resp = self.client.app_user_list(package_types='[13]', sub_firm_id=D.sub_contact_40188.sub_firm_id,
                                         search_name=searchname)
        self.assertEqual(10000, resp.code)

    def test_user_list_last_login_orders(self):
        """个人账号列表-last_login_at排序"""
        orders = [{"last_login_at": "desc"}]
        searchname = '137'
        resp = self.client.app_user_list(package_types='[13,1]', sub_firm_id=D.sub_contact_40188.sub_firm_id,
                                         orders=orders, search_name=searchname)
        self.assertEqual(10000, resp.code)


class TestUserAccountDelay(BaseTestCase):

    def test_user_account_delay_invalid(self):
        """账号延期-不传用户ID和联系人ID"""
        resp = self.client.app_users_delay()
        self.assertEqual(-995, resp.code)
        self.assertEqual(['is missing'], resp.data.app_user_ids)
        self.assertEqual(['is missing'], resp.data.sub_contact_ids)
        self.assertEqual('is missing', resp.message)

    def test_user_account_delay_valid(self):
        """账号延期-单个账号"""
        resp = self.client.app_users_delay(app_user_ids="[13]", delay_days=3, sub_contact_ids="[40188]")
        self.assertEqual(10000, resp.code)
        self.assertEqual('success', resp.message)

    def test_user_account_delay_batch(self):
        """账号延期-批量延期"""
        resp = self.client.app_users_delay(app_user_ids="[13,56]", delay_days=3, sub_contact_ids="[40188]")
        self.assertEqual(10000, resp.code)
        self.assertEqual('success', resp.message)


class TestAccountSetAdmin(BaseTestCase):

    def test_user_account_set_admin_valid(self):
        """设置账号为主管理员"""
        resp = self.client.app_users_set_admin(app_user_id=357256, user_main_admin=1)
        self.assertEqual(10000, resp.code)

    def test_user_account_set_admin_not(self):
        """设置账号为主管理员-rollback"""
        resp = self.client.app_users_set_admin(app_user_id=357256, user_main_admin=0)
        self.assertEqual(10000, resp.code)

    def test_user_account_set_admin_user_id_null_not_exist(self):
        """设置账号为主管理员-不传用户ID或ID不存在"""
        resp = self.client.app_users_set_admin(app_user_id=0)
        self.assertEqual(5004, resp.code)


class TestAccountSetDacView(BaseTestCase):
    def test_user_set_dac_view_valid(self):
        """设置账号开通数据统计权限"""
        resp = self.client.app_users_set_dac_view(app_user_id=357256, dac_view_leader=1)
        self.assertEqual(10000, resp.code)

    def test_user_set_dac_view_valid1(self):
        """设置账号开通数据统计权限--rollback"""
        resp = self.client.app_users_set_dac_view(app_user_id=357256, dac_view_leader=0)
        self.assertEqual(10000, resp.code)

    def test_user_set_dac_view_id_not_exist(self):
        """设置账号开通数据统计权限"""
        resp = self.client.app_users_set_dac_view(dac_view_leader=357256)
        self.assertEqual(-995, resp.code)


class TestAccountSetViewLimit(BaseTestCase):
    def test_user_set_view_limit(self):
        """设置账号查看数量-都为0"""
        resp = self.client.app_users_set_view_limit(app_user_id=357256)
        self.assertEqual(10000, resp.code)

    def test_user_set_view_limit1(self):
        """设置账号查看数量-一个为0"""
        resp = self.client.app_users_set_view_limit(app_user_id=357256, limit_open_count=10)
        self.assertEqual(10000, resp.code)

    def test_user_set_view_limit2(self):
        """设置账号查看数量-都不为0"""
        resp = self.client.app_users_set_view_limit(app_user_id=357256, limit_open_count=10, limit_open_count_bid=10)
        self.assertEqual(10000, resp.code)

    def test_user_set_view_limit3(self):
        """设置账号查看数量-超过最大限制"""
        resp = self.client.app_users_set_view_limit(app_user_id=357256, limit_open_count=10000, limit_open_count_bid=10000)
        self.assertEqual(10000, resp.code)


class TestUserBatchCreate(BaseTestCase):

    def test_scenario_all(self):
        """上传Excel账号文件和pdf文件,校验，创建"""
        app_users_file = abspath(join(__file__, "../data/客服部创建基础和免费.xls"))
        sub_firm_id = 169783
        resp = self.client.app_users_uses_file_upload(app_users_file=app_users_file, sub_firm_id=sub_firm_id)
        self.assertEqual(10000, resp.code)
        self.assertGreaterEqual(resp.data.batch_id, 0)

        batch_id = resp.data.batch_id
        contract_file = abspath(join(__file__, "../data/erd.pdf"))
        resp = self.client.app_users_contract_upload(batch_id=batch_id, contract_file=contract_file)
        self.assertEqual(10000, resp.code)
        self.assertEqual(batch_id, resp.data.batch_id)

        resp = self.client.app_users_batch_create_preview(batch_id=batch_id)
        self.assertEqual(10000, resp.code)
        temp_id = resp.data.can_create_list[1].get('temp_id')
        resp = self.client.app_users_batch_create(temp_id=temp_id)
        self.assertEqual(10000, resp.code)

    def test_upload_contact(self):
        """上传合同文件"""
        batch_id = 29
        contract_file = abspath(join(__file__, "../data/erd.pdf"))
        resp = self.client.app_users_contract_upload(batch_id=batch_id, contract_file=contract_file)
        self.assertEqual(10000, resp.code)

    def test_batch_preview_and_create(self):
        """批量校验接口，创建"""
        batch_id = 85
        resp = self.client.app_users_batch_create_preview(batch_id=batch_id)
        self.assertEqual(10000, resp.code)
        temp_id = resp.data.can_create_list[1].get('temp_id')
        resp = self.client.app_users_batch_create(temp_id=temp_id)
        self.assertEqual(10000, resp.code)

    def test_batch_create_batch_id(self):
        """批量创建接口-batch_id-没有实现"""
        batch_id = 29
        resp = self.client.app_users_batch_create(batch_id=batch_id)
        self.assertEqual(-995, resp.code)
        self.assertEqual(resp.data.temp_id, ["is missing", "is empty"])


class TestAppUsersSubCreate(BaseTestCase):

    def test_app_users_sub_create(self):
        """创建基础免费账号"""
        phone_number = cp()
        sub_firm_id = 169783
        name = "test" + str(sub_firm_id)
        resp = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=1, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        self.assertEqual(10000, resp.code)


    def test_app_users_sub_create_mobile_none(self):
        """创建基础免费账号"""
        phone_number = cp()
        sub_firm_id = 169783
        name = "test" + str(sub_firm_id)
        resp = self.client.app_users_sub_create(name=name, package_type=1, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        self.assertEqual(5003, resp.code)
        self.assertIn("手机号为空！", resp.message)

    def test_app_users_sub_create_mobile_error(self):
        """创建基础免费账号"""
        phone_number = cp()
        sub_firm_id = 169783
        name = "test" + str(sub_firm_id)
        resp = self.client.app_users_sub_create(mobile="....", name=name, package_type=1, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        self.assertEqual(5003, resp.code)
        self.assertIn("手机号格式错误！", resp.message)

    def test_app_users_sub_create_name_none(self):
        """创建基础免费账号"""
        phone_number = cp()
        sub_firm_id = 169783
        name = "test" + str(sub_firm_id)
        resp = self.client.app_users_sub_create(mobile=phone_number, package_type=1, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        self.assertEqual(5001, resp.code)
        self.assertIn("使用人姓名不能为空", resp.message)


    def test_app_users_sub_create_base_out(self):
        """创建基础免费账号"""
        phone_number = cp()
        sub_firm_id = 370303
        name = "test" + str(sub_firm_id)
        resp1 = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=2, pl_style=0,
                                                 sub_firm_id=sub_firm_id)
        self.assertEqual(5001, resp1.code)
        self.assertIn("公司没有有效正式订阅", resp1.message)

    def test_app_users_sub_create_sub_exist(self):
        """创建基础免费账号,手机号为其他公司名下联系人手机号"""
        phone_number = cp()
        sub_firm_id = 169783
        name = "test" + str(sub_firm_id)
        resp = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=1, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        resp2 = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=1, pl_style=0,
                                                 sub_firm_id="52495")
        self.assertEqual(5001, resp2.code)


    def test_app_users_sub_create_base_to_free(self):
        """创建基础免费账号"""
        phone_number = cp()
        sub_firm_id = 169783
        name = "test" + str(sub_firm_id)
        resp = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=2, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        resp2 = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=1, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        self.assertEqual(10000, resp2.code)
        self.assertEqual(1, resp2.data.package_type)

    def test_app_users_sub_create_free_to_base(self):
        """创建基础免费账号"""
        phone_number = cp()
        sub_firm_id = 169783
        name = "test" + str(sub_firm_id)
        resp = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=1, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        resp2 = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=2, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        self.assertEqual(10000, resp2.code)
        self.assertEqual(2, resp2.data.package_type)

class TestAppUsersContractUploadForUser(BaseTestCase):

    def test_app_users_contract_upload_for_user(self):
        sub_firm_id = 29
        contract_file = abspath(join(__file__, "../data/erd.pdf"))
        resp = self.client.app_users_contract_upload_for_user(sub_firm_id=sub_firm_id, contract_file=contract_file)
        self.assertEqual(10000, resp.code)

    def test_app_users_contract_upload_for_user_no_pdf(self):
        sub_firm_id = 29
        contract_file = abspath(join(__file__, "../data/erd.yml"))
        resp = self.client.app_users_contract_upload_for_user(sub_firm_id=sub_firm_id, contract_file=contract_file)
        self.assertEqual(5006, resp.code)


class TestAppUsersShow(BaseTestCase):

    def create_acount(self, package_type):
        """创建基础免费账号"""
        phone_number = cp()
        sub_firm_id = 169783
        name = "test" + str(phone_number[5:])
        resp = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=package_type, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        return resp.data

    def test_app_users_show_free(self):
        """账号详情页,免费账号"""
        data = self.create_acount(package_type=1)
        uid = data.id

        resp = self.client.app_users_id_show(id=uid)
        self.assertEqual(10000, resp.code)
        self.assertEqual(data.name, resp.data.name)
        self.assertEqual(data.mobile, resp.data.mobile)
        self.assertEqual(data.sub_end, resp.data.sub_end)

    def test_app_users_show_base(self):
        """账号详情页，基础账号"""
        data = self.create_acount(package_type=2)
        uid = data.id

        resp = self.client.app_users_id_show(id=uid)
        self.assertEqual(10000, resp.code)
        self.assertEqual(data.name, resp.data.name)
        self.assertEqual(data.mobile, resp.data.mobile)
        self.assertEqual(data.sub_end, resp.data.sub_end)


class TestAppUsersSetting(BaseTestCase):

    def create_acount(self, package_type):
        """
        创建基础免费账号
        package_type:1免费 2基础
        """
        phone_number = cp()
        sub_firm_id = 169783
        name = "test" + str(phone_number[5:])
        resp = self.client.app_users_sub_create(mobile=phone_number, name=name, package_type=package_type, pl_style=0,
                                                sub_firm_id=sub_firm_id)
        print(resp)
        return resp.data

    def app_users_show(self, id):
        resp = self.client.app_users_id_show(id=id)
        return resp

    def test_app_users_setting_pl_style(self):
        """账号编辑设置 pl_style"""
        uid = self.create_acount(1).id
        resp1 = self.client.app_users_setting(id=uid, pl_style=1)
        resp2 = self.app_users_show(id=uid)
        self.assertEqual(10000, resp1.code)
        self.assertEqual(1, resp2.data.pl_style)

    def test_app_users_setting_allot_admin(self):
        """账号编辑设置 allot_admin"""
        uid = self.create_acount(1).id
        resp1 = self.client.app_users_setting(id=uid, allot_admin=0)
        resp2 = self.app_users_show(id=uid)
        self.assertEqual(10000, resp1.code)
        self.assertEqual(0, resp2.data.allot_admin)

    @unittest.skip("mark说先不改，这个功能还没人用，暂时跳过")
    def test_app_users_setting_allot_region_ids(self):
        """账号编辑设置 allot_region_ids"""
        uid = self.create_acount(1).id
        resp1 = self.client.app_users_setting(id=uid, allot_region_ids="[13, 15, 16, 26]",
                                              allot_province_ids="[3, 5, 6, 7, 8, 9, 15, 2, 13, 32, 4, 11, 12, 16, 29,30, 251]",
                                              allot_city_ids="[]")
        resp2 = self.app_users_show(id=uid)
        self.assertEqual(10000, resp1.code)
        self.assertIn("华东区", resp2.data.allot_region_names)
        self.assertIn("北京", resp2.data.allot_province_names)

    def test_app_users_setting_crm(self):
        """账号编辑设置 pl_style"""
        uid = self.create_acount(2).id
        resp1 = self.client.app_users_setting(id=uid, crm=1)
        resp2 = self.app_users_show(id=uid)
        self.assertEqual(10000, resp1.code)
        self.assertEqual(1, resp2.data.crm)

    def test_app_users_setting_pl_style2(self):
        """账号编辑设置 pl_style"""
        uid = self.create_acount(2).id
        resp1 = self.client.app_users_setting(id=uid, pl_style=1)
        resp2 = self.app_users_show(id=uid)
        self.assertEqual(10000, resp1.code)
        self.assertEqual(1, resp2.data.pl_style)

    def test_app_users_setting_allot_admin2(self):
        """账号编辑设置 allot_admin"""
        uid = self.create_acount(2).id
        resp1 = self.client.app_users_setting(id=uid, allot_admin=0)
        resp2 = self.app_users_show(id=uid)
        self.assertEqual(10000, resp1.code)
        self.assertEqual(0, resp2.data.allot_admin)

    @unittest.skip("mark说先不改，这个功能还没人用，暂时跳过")
    def test_app_users_setting_allot_region_ids2(self):
        """账号编辑设置 allot_region_ids"""
        uid = self.create_acount(2).id
        resp1 = self.client.app_users_setting(id=uid, allot_region_ids="[13, 15, 16, 26]",
                                              allot_province_ids="[3, 5, 6, 7, 8, 9, 15, 2, 13, 32, 4, 11, 12, 16, 29,30, 251]",
                                              allot_city_ids="[]")
        resp2 = self.app_users_show(id=uid)
        self.assertEqual(10000, resp1.code)
        self.assertIn("华东区", resp2.data.allot_region_names)
        self.assertIn("北京", resp2.data.allot_province_names)


    def test_app_users_setting(self):
        """dm订阅详情、经销商/项目包订阅信息详情"""
        resp = self.client.app_users_dms_subscription(order_id=118797,id=203)
        self.assertEqual(10000,resp.code)
        self.assertEqual(203,resp.data.id)
        self.assertEqual(118797,resp.data.order_id)

    def test_app_users_setting1(self):
        """dm订阅详情、经销商/项目包订阅信息详情"""
        resp = self.client.app_users_dms_subscription(order_id=118797,id=9999)
        self.assertEqual(10000,resp.code)
        self.assertIsNotNone(resp.data)
    def test_app_users_setting2(self):
        """dm订阅详情、经销商/项目包订阅信息详情"""
        resp = self.client.app_users_dms_subscription(order_id=9999999999)
        self.assertEqual(10000,resp.code)
        self.assertIsNotNone(resp.data)

    def test_app_users_dms_subscription_update(self):
        """dms订阅详情、经销商/项目包订阅信息编辑或创建"""
        resp = self.client.app_users_dms_subscription_update(sub_firm_id=255309,order_id=118797,dealer_num=199999,project_package=999999,
                                                             sub_start="2021-08-26",sub_end="2020-08-12")
        self.assertEqual(10000,resp.code)
        self.assertIsNotNone(resp.data)
        self.assertEqual(255309,resp.data.sub_firm_id)
        self.assertEqual(199999,resp.data.dealer_num)
        self.assertEqual(999999,resp.data.project_package)
        self.assertEqual('2021-08-26',resp.data.sub_start)
        self.assertEqual('2020-08-12',resp.data.sub_end)


    def test_app_users_dms_subscription_update1(self):
        """dms订阅详情、经销商/项目包订阅信息编辑或创建"""
        resp = self.client.app_users_dms_subscription_update(sub_firm_id=255309,order_id=118797,dealer_num=9999999999999999999,project_package=9999999999999,
                                                             sub_start="2021-08-26",sub_end="2020-08-12")
        self.assertEqual(10000,resp.code)
        self.assertIsNotNone(resp.data)
        self.assertEqual(255309,resp.data.sub_firm_id)
        self.assertEqual(9999999999999999999,resp.data.dealer_num)
        self.assertEqual(9999999999999,resp.data.project_package)
        self.assertEqual('2021-08-26',resp.data.sub_start)
        self.assertEqual('2020-08-12',resp.data.sub_end)

    def test_app_users_dms_subscription_update2(self):
        """dms订阅详情、经销商/项目包订阅信息编辑或创建"""
        resp = self.client.app_users_dms_subscription_update(sub_firm_id=255309,order_id=118797,dealer_num="你好",project_package="你好",
                                                             sub_start="2021-08-26",sub_end="2020-08-12")
        self.assertEqual(-995,resp.code)

    def test_app_users_dms_subscription_update3(self):
        """dms订阅详情、经销商/项目包订阅信息编辑或创建"""
        resp = self.client.app_users_dms_subscription_update(sub_firm_id=255309,order_id=118797,dealer_num=9999999999999999999,project_package=9999999999999,
                                                             sub_start="2021-08-26",sub_end="2020-08-12",id=9999)
        self.assertEqual(-995,resp.code)
        self.assertIsNotNone(resp.data)
        self.assertEqual(255309,resp.data.sub_firm_id)
        self.assertEqual(9999999999999999999,resp.data.dealer_num)
        self.assertEqual(9999999999999,resp.data.project_package)
        self.assertEqual('2021-08-26',resp.data.sub_start)
        self.assertEqual('2020-08-12',resp.data.sub_end)

    def test_app_users_dms_subscription_update4(self):
        """dms订阅详情、经销商/项目包订阅信息编辑或创建"""
        resp = self.client.app_users_dms_subscription_update(sub_firm_id=255309,order_id=118797,dealer_num=9999999999999999999,project_package=9999999999999,
                                                             sub_start="2021-08-26",sub_end="2020-08-12",id=202)
        self.assertEqual(10000,resp.code)
        self.assertIsNotNone(resp.data)
        resp1 = self.client.app_users_dms_subscription(order_id=118797,id=202)
        self.assertEqual(255309,resp1.data.sub_firm_id)
        self.assertEqual(9999999999999999999,resp1.data.dealer_num)
        self.assertEqual(9999999999999,resp1.data.project_package)
        self.assertEqual('2021-08-26',resp1.data.sub_start)
        self.assertEqual('2020-08-12',resp1.data.sub_end)

    def test_app_users_replace_apply_list(self):
        """更换使用人申请列表"""
        resp = self.client.app_users_replace_apply_list()
        self.assertEqual(10000,resp.code)

    def test_app_users_replace_apply_list1(self):
        """更换使用人申请列表"""
        resp = self.client.app_users_replace_apply_list(status="[1]",package_type="[2]")
        self.assertEqual(10000,resp.code)
        self.assertEqual(1,resp.data.list[0]['status'])
        self.assertEqual(2,resp.data.list[0]['package_type'])

    def test_app_users_replace_apply_pass(self):
        """审核通过"""
        resp = self.client.app_users_replace_apply_pass(id=30,operate_type=1)
        print(resp)
        self.assertEqual(10000,resp.code)

    def test_app_users_replace_apply_pass1(self):
        """审核通过"""
        resp = self.client.app_users_replace_apply_pass(id=30,operate_type=2)
        print(resp)
        self.assertEqual(10000,resp.code)

    def test_app_users_replace_apply_back(self):
        """审核退回"""
        resp = self.client.app_users_replace_apply_back(reject_reason=123,id=27,sub_firm_id=74,person_user_id=86573)
        print(resp)
        self.assertEqual(10000,resp.code)

    def test_app_users_replace_apply_back1(self):
        """审核退回"""
        with open('../../../data/files/testfile.txt','r', encoding='UTF-8') as f:
            data=f.read()
        resp = self.client.app_users_replace_apply_back(reject_reason=data,id=27,sub_firm_id=74,person_user_id=86573)
        self.assertEqual(10000,resp.code)

    def test_app_users_replace_user_info(self):
        """更换使用人申请详情"""
        resp = self.client.app_users_replace_user_info(id=28)
        print(resp)
        self.assertEqual(10000,resp.code)

    def test_app_users_replace_user_update(self):
        """更换人替换名片"""
        resp = self.client.app_users_replace_user_update(id=28,card_path="https://goss.veer.com/creative/vcg/veer/800water/veer-310687633.jpg")
        self.assertEqual(10000,resp.code)
        resp1 = self.client.app_users_replace_user_info(id=28)
        self.assertEqual("https://goss.veer.com/creative/vcg/veer/800water/veer-310687633.jpg",resp1.data.card_path)

    def test_app_users_replace_user_update1(self):
        """更换人替换名片"""
        with open('../../../data/files/testfile.txt','r', encoding='UTF-8') as f:
            data=f.read()
        resp = self.client.app_users_replace_user_update(id=28,card_path=data)
        self.assertEqual(10000,resp.code)
        resp1 = self.client.app_users_replace_user_info(id=28)
        self.assertEqual(data,resp1.data.card_path)



