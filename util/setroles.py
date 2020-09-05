#!/usr/bin/env python
# -*- coding: utf-8 -*-

import warnings
from config import services
from os.path import join, abspath
from apis.mega.modifyauth.auth import AuthClient
from data import DataCenter as D, load_local_data
from apis.pangu.auth.setroles import SetRolesClient
from apis.mega.login.login import Login as mega_login
from apis.pangu.login.login import Login as pangu_login


class SetRoles:
    def mega(self, user, job_title_id, role_ids):
        """
        mega权限设置
        :param user:用来设置权限的账号
        :param job_title_id:职位id
        :param role_ids: 权限list
        :return:
        """
        login_client = mega_login(base_url=services.mega)
        resp = login_client.get_token(username=user, password=D.user_mega.password)
        self.token = resp.data.session_id
        self.authclient = AuthClient(base_url=services.mega, access_token=self.token)
        res = self.authclient.right_roles(job_title_id=job_title_id, role_ids=role_ids)
        return res


class PanGu:
    @staticmethod
    def get_token():
        file = abspath(join(__file__, "../../tests/pangu/test.json"))
        load_local_data(data_file=file)
        login_client = pangu_login(base_url=services.pangu)
        login_resp = login_client.get_token(D.userpangu.username, D.userpangu.password, D.userpangu.key)
        token = login_resp.data.token
        return token

    @staticmethod
    def set_job(job_title_id, role_ids):
        """
        pangu权限设置
        :param job_title_id: 职位ID
        :param role_ids: 权限id（list）
        :return:
        """
        pg_object = PanGu()
        token = pg_object.get_token()
        auth_client = SetRolesClient(base_url=services.pangu, access_token=token)
        resp = auth_client.add_right_roles(job_title_id=job_title_id, role_ids=role_ids)
        if resp.code == 10000 and resp.message == '请求成功':
            return True
        else:
            return False

    @staticmethod
    def set_role(role_ids, client):
        pg_object = PanGu()
        pg_object.set_job(job_title_id=D.roles.job_title_id, role_ids=role_ids)
        login_client = pangu_login(base_url=services.pangu)
        login_resp = login_client.get_token(D.userpangu.user_lu, D.userpangu.password, D.userpangu.key)
        token = login_resp.data.token
        client = client(base_url=services.pangu, access_token=token)
        warnings.simplefilter('ignore', ResourceWarning)
        return client


if __name__ == '__main__':
    a = SetRoles().mega(user="w.deng", job_title_id=10188, role_ids="[1,26]")
    print(a)
