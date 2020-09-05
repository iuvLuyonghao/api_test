#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, warnings
from apis.mega.menus.menus import MenusClient
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
        cls.client = MenusClient(base_url=services.mega, access_token=cls.token)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class TestMenus(BaseTestCase):

    def test_menus(self):
        """
        获取员工可见的导航
        :return:
        """
        resp = self.client.menus(show_all=True)
        self.assertEqual(resp.code, 10000)

    def test_menus1(self):
        """
        获取员工可见的导航
        :return:
        """
        resp = self.client.menus(show_all=False)
        self.assertEqual(resp.code, 10000)

    def test_department_menus(self):
        """
        修改/添加菜单的可见权限
        :return:
        """
        addresp = self.client.add_menus(name='test',level_id=1,sort_num=1,url="www.baidu.com")
        self.assertEqual(addresp.code, 10000)
        resp = self.client.department_menus(menu_id=addresp.data["id"])
        self.assertEqual(resp.code, 10000)
        delresp=self.client.del_menus(id=addresp.data["id"])
        self.assertEqual(delresp.code, 10000)

    def test_department_menus1(self):
        """
        修改/添加菜单的可见权限
        :return:
        """
        resp = self.client.department_menus(menu_id=1999999999999)
        self.assertEqual(resp.code, 101)

    def test_department_menus_get(self):
        """
        某一个菜单可见的部门和职位
        :return:
        """
        createresp = self.client.add_menus(name='test',level_id=1,sort_num=1,url="www.baidu.com")
        self.assertEqual(createresp.code, 10000)
        resp = self.client.department_menus_get(menu_id=createresp.data["id"])
        self.assertEqual(resp.code, 10000)
        delresp=self.client.del_menus(id=createresp.data["id"])
        self.assertEqual(delresp.code, 10000)

    def test_add_del_update_menus(self):
        """
        添加、删除、更新
        :return:
        """
        resp = self.client.add_menus(name='test',level_id=1,sort_num=1,url="www.baidu.com")
        self.assertEqual(resp.code, 10000)
        self.assertEqual(resp.data["name"],"test")
        self.assertEqual(resp.data["level_id"],1)
        self.assertEqual(resp.data["url"],"www.baidu.com")
        updateresp=self.client.update_menu(id=resp.data["id"],name='test111',level_id=2,sort_num=2,url="www.hao123.com")
        self.assertEqual(updateresp.code, 10000)
        self.assertEqual(updateresp.data["name"],"test111")
        self.assertEqual(updateresp.data["level_id"],2)
        self.assertEqual(updateresp.data["url"],"www.hao123.com")
        delresp=self.client.del_menus(id=resp.data["id"])
        self.assertEqual(delresp.code, 10000)

