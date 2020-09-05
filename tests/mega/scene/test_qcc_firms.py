# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.qcc_firms.qcc_firms import QccFirmsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
import time
import pytest
from util.setroles import SetRoles
import qav5.log
import json
from util.myencoder import MyEncoder
file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)

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

    @pytest.mark.scene
    def test_qcc_firms(self):
        """上传文件->上传校验完成预览数据->确认保存上传的数据"""
        filepath=abspath(join(__file__,"../../qcc_firms/data/test.xls"))
        respfiles=self.client.files(firms_file=filepath)
        self.assertEqual(10000,respfiles.code)
        time.sleep(1)
        resppreview=self.client.preview_list(batch_id=respfiles.data.batch_id,page=1,ispass=1)
        self.assertEqual(10000,resppreview.code)
        self.assertEqual(1,resppreview.data.total)
        self.assertEqual("上海云蔚机电设备工程有限公司",resppreview.data.list[0]["qcc_firm_name"])
        respfirmscreate=self.client.firms_create(batch_id=respfiles.data.batch_id,create=False)
        self.assertEqual(10000,respfirmscreate.code)


