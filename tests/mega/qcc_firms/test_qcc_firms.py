# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.qcc_firms.qcc_firms import QccFirmsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
from util.setroles import SetRoles
import qav5.log
import json
from util.myencoder import MyEncoder


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = QccFirmsClient(base_url=services.mega, access_token=cls.token)
        warnings.simplefilter('ignore', ResourceWarning)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestQccFirms(BaseTestCase):

    def test_files(self):
        """
        上传excel文件
        :return:
        """
        filepath=abspath(join(__file__,"../data/test.xls"))
        resp=self.client.files(firms_file=filepath)
        print(resp)
        self.assertEqual(10000,resp.code)

    def test_preview_list(self):
        """
        上传校验完成预览数据
        :return:
        """
        resp=self.client.preview_list(batch_id=1215,page=1,ispass=1)
        print(resp)
        self.assertEqual(10000,resp.code)
        self.assertEqual(1,resp.data.total)
        self.assertEqual("上海云蔚机电设备工程有限公司",resp.data.list[0]["qcc_firm_name"])


    def test_list(self):
        """
        已上传的公司数据
        :return:
        """
        resp=self.client.list(view_type=1)
        self.assertEqual(10000,resp.code)

    def test_show(self):
        """
        企查查公司详情
        :return:
        """
        resp=self.client.show(id=125191)
        self.assertEqual(10000,resp.code)
        self.assertEqual('上海兴尹装饰设计工程有限公司',resp.data.firm_name)


