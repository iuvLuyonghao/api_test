#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class PlatformsClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/platforms/parts",method="get")
    def parts_get(self,is_edit : bool,part_type:int):
        """
        获取员工工作台--快捷路径和模块
        :param is_edit: 是否是编辑状态？ 会判断操作人的权限 非编辑模式， 则是返回设置了显示的。
        :param part_type:1: 快捷路径， 2: 模块
        :return:
        """
        pass

    @api(rule="/platforms/parts",method="post")
    def parts_post(self,platform_id : int,shortcuts:list):
        """
        创建和修改快捷路径
        :param platform_id:工作台ID
        :param shortcuts:快捷路径
        :param modules:模块
        :return:
        """
        pass

