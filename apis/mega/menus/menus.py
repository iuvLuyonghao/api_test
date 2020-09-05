# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class MenusClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/base/menus",method="get")
    def menus(self,show_all : bool):
        """
        获取员工可见的导航
        :param show_all: 是否显示所有
        :return:
        """
        pass

    @api(rule="/base/department_menus",is_json_req=True)
    def department_menus(self,menu_id : int,job_title_ids:list=None,department_ids:list=None):
        """
        修改/添加菜单的可见权限
        :param menu_id:菜单ID
        :param department_ids:部门ID ，对空则删除
        :param job_title_ids:职位ID， 对空则删除
        :return:
        """
        pass

    @api(rule="/base/menus",is_json_req=True)
    def add_menus(self,name : str,level_id:int,sort_num:int,url:str,parent_name:str=None,parent_id:int=None,notes:str=None,target:str=None):
        """
        添加菜单
        :param name:
        :param level_id:1， 2 级
        :param sort_num:
        :param url:
        :param parent_name:
        :param parent_id:
        :param notes:
        :param target:是否新窗口打开
        :return:
        """
        pass

    @api(rule="/base/del_menu/<id>")
    def del_menus(self,id):
        """
        删除菜单
        :param id:
        :return:
        """
        pass

    @api(rule="/base/department_menus",method="get")
    def department_menus_get(self,menu_id:int):
        """
        某一个菜单可见的部门和职位
        :param menu_id:菜单ID
        :return:
        """
        pass

    @api(rule="/base/update_menu/<id>",is_json_req=True)
    def update_menu(self,id,name:str,level_id:int,sort_num:int,url:str,target:str=None,parent_name:str=None,parent_id:int=None,notes:str=None):
        """
        修改菜单
        :param name:
        :param level_id:
        :param sort_num:
        :param url:
        :param target:
        :param parent_name:
        :param parent_id:
        :param notes:
        :return:
        """
        pass