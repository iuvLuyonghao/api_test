# -*- coding: utf-8 -*-

import pytest
import logging
from _pytest.fixtures import SubRequest
from _pytest.unittest import TestCaseFunction
from qav5.conn import MySQLConnectionMgr
from config import services

"""
该文件存放全局的fixtures，当与子目录下的fixture重名时，会被替换
"""
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module", name="mysql", autouse=True)
def mysql_connection(request: SubRequest):
    """全局的mysql连接，用例层可以不使用MySQLConnectionMgr来进行连接"""
    # mgr = MySQLConnectionMgr(autocommit=True, charset='utf8',
    #                          **services.mysql)
    # mgr.backend = mgr.BACKEND_PYMYSQL
    # setattr(request.module, "mysql", mgr.connection)
