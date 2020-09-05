# -*- coding: utf-8 -*-

import unittest, warnings
from apis.mega.platforms.platforms import PlatformsClient
from apis.mega.login.login import Login
from config import services
from data import DataCenter as D, load_local_data
from os.path import join, abspath
import qav5.log

file = abspath(join(__file__, "../../test.json"))
load_local_data(data_file=file)


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        login_client = Login(base_url=services.mega)
        resp = login_client.get_token(username=D.user_mega.username, password=D.user_mega.password)
        cls.token = resp.data.session_id
        cls.client = PlatformsClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestPart(BaseTestCase):

    def test_part_get(self):

        """
        获取员工工作台--快捷路径和模块
        :return:
        """
        resp = self.client.parts_get(is_edit=True,part_type=1)
        self.assertEqual(resp.code, 10000)

    def test_part_get1(self):

        """
        获取员工工作台--快捷路径和模块
        :return:
        """
        resp = self.client.parts_get(is_edit=True,part_type=2)
        self.assertEqual(resp.code, 10000)


    def test_part_get2(self):

        """
        获取员工工作台--快捷路径和模块
        :return:
        """
        resp = self.client.parts_get(is_edit=False,part_type=2)
        self.assertEqual(resp.code, 10000)

    def test_part_post(self):

        """
        获取员工工作台--快捷路径和模块
        :return:
        """
        resp = self.client.parts_post(platform_id=1,shortcuts=1)
        self.assertEqual(resp.code, -995)

    def test_part_post1(self):

        """
        获取员工工作台--快捷路径和模块
        :return:
        """
        short='[{"id":9,"url":"先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失","name":"先帝创业未半","active":true,"order_num":1},{"id":10,"url":"先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失","name":"先帝创业未半","active":true,"order_num":2},{"active":true,"name":"64563","url":"634563456","order_num":3}]'
        resp = self.client.parts_post(platform_id=1,shortcuts=short)
        self.assertEqual(resp.code, 10000)

    def test_part_post2(self):
        """
        获取员工工作台--快捷路径和模块
        :return:
        """
        short='[{"id":9,"url":"先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失","name":"先帝创业未半","active":true,"order_num":1},{"id":10,"url":"先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失","name":"先帝创业未半","active":true,"order_num":2},{"active":true,"name":"64563","url":"","order_num":3},{"id":,"url":"","name":"先帝创业未半","active":true,"order_num":1}]'
        resp = self.client.parts_post(platform_id=1,shortcuts=short)
        self.assertEqual(resp.code, -995)

    def test_part_post3(self):
        """
        获取员工工作台--快捷路径和模块
        :return:
        """
        short='[{"id":11,"url":"先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失","name":"先帝创业未半","active":true,"order_num":1},{"id":12,"url":"先帝创业未半而中道崩殂，今天下三分，益州疲弊，此诚危急存亡之秋也。然侍卫之臣不懈于内，忠志之士忘身于外者，盖追先帝之殊遇，欲报之于陛下也。诚宜开张圣听，以光先帝遗德，恢弘志士之气，不宜妄自菲薄，引喻失","name":"先帝创业未半","active":true,"order_num":2},{"id":13,"url":"634563456","name":"64563","active":true,"order_num":3},{"active":true,"name":"百度","url":"www.baidu.com","order_num":4}]'
        resp = self.client.parts_post(platform_id=1,shortcuts=short)
        self.assertEqual(resp.code, 10000)