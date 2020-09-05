# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch




class QccFirmsClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    def files(self, firms_file):
        """
        上传Excel附件
        :param firms_file: excel 文件，企查查的导出文件。
        :return:
        """
        return self._call_api("/qcc_firms/files",method="post",req_kwargs={'files':{'firms_file':open(firms_file,'rb')}},disable_log=True)

    # @api(rule="/qcc_firms/preview_list",method="get")
    def preview_list(self,batch_id,page,ispass):
        """
        上传校验完成预览数据
        :param params:
        :return:
        """
        return self._call_api("/qcc_firms/preview_list",method="post",req_kwargs={"params":{
            "batch_id": batch_id,
            "page": page,
            "pass": ispass
        }})

    @api(rule="/qcc_firms/firms_create")
    def firms_create(self, batch_id,create):
        """
        确认保存上传的数据
        :param batch_id:上传附件对应的创建批次
        :param create:是否创建， true： 创建上传的数据， false: 取消上传的数据并且清除缓存数据。
        :return:
        """
        pass

    @api(rule="/qcc_firms/list")
    def list(self, view_type):
        """
        已上传的公司数据
        :param view_type:
        :return:
        """
        pass

    @api(rule="/qcc_firms/show/<id>",method="get")
    def show(self, id):
        """
        企查查公司详情
        :param id:
        :return:
        """
        pass