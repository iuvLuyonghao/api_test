# -*- coding: utf-8 -*-

from qav5.http.client import BaseClient
from qav5.http.helper import api
from qav5.utils import Bunch, low_case_to_camelcase


class SurveyClient(BaseClient):
    def __init__(self, base_url, access_token=None, **kwargs):
        super().__init__(base_url, kwargs)
        self.access_token = access_token
        self.req_kwargs.update({"headers": {"Authorization": self.access_token}})
        self.interceptor = lambda r, j: Bunch(j)

    @api(rule="/questionnaires/active_list", method="get", remove_null=True)
    def active_survey_list(self, page=None):
        """可用调研问卷列表
        :param page: 页数
        :return:
        """
        pass

    @api(rule="/questionnaires/firm_survey_url", method="get", is_json_req=True, remove_null=True)
    def firm_survey_url(self, sub_firm_id: int, questionnaire_id: int = 1):
        """
        生成问卷链接
        :param sub_firm_id:
        :param questionnaire_id:
        :return:
        """
        pass

    @api(rule="/firm_surveys/list", method="get", is_json_req=True)
    def firm_surveys_list(self, questionnaire_id: int = None, sub_firm_name=None, submit_at_gt: int = None,
                          submit_at_ls: int = None, sub_firm_id=None, page=1, per_page=20, is_submit=1):
        """
        公司的调查问卷结果列表
        :param questionnaire_id:
        :param sub_firm_name:
        :param submit_at_gt:
        :param submit_at_ls:
        :param sub_firm_id:
        :param page:
        :param per_page:
        :param is_submit: 1 提交
        :return:
        """
        pass

    @api(rule="/questionnaires/list", method="get", is_json_req=True)
    def firm_surveys_all(self, page=1):
        """
        所有调研问卷列表
        :param page
        :return:
        """
        pass
