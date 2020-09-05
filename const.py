# -*- coding: utf-8 -*-
from enum import Enum


class Framework:
    """框架常量"""
    CASE_DIR = "tests"


class RuntimeEnv:
    ENV_DEV = "dev"  # dev环境
    ENV_TEST = "test"  # test环境
    ENV_BETA = "beta"  # beta环境
    ENV_PRODUCTION = "prod"  # 生产环境


class RecallsBiz:
    SUCCESS_CODE = 10000
    ERROE_CODE = -995
    ERROE_CODE_DATE = -994
    ERROE_CODE_NO_DATA = -996
    SUCCESS = "success"
    Delay_OverLimit = "超过延期数量"

