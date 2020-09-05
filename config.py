# -*- coding: utf-8 -*-

from const import RuntimeEnv

environment = RuntimeEnv.ENV_DEV  # 默认运行环境


class _IP:
    TEST = "*.*.*.*"
    DEV = "*.*.*.*"

def _easy_domain(biz: object, is_https=False):
    """根据env返回业务域名（如果按规则命名的话）"""
    #  下面两行代码是工外用的，为了使用test环境新增的，不影响其他项目
    if environment == RuntimeEnv.ENV_PRODUCTION:
        # 为了在正式环境也能运行电话系统只能测试线运行的脚本(因为正式线测试线的前缀不一样。。)
        if biz in {"phone-cloud-api"}:
            return "http{}://{}.dev.*.com".format("s" if is_https else "", biz)
        return "http{}://{}.*.com".format("s" if is_https else "", biz)

    elif environment == RuntimeEnv.ENV_TEST:
        if biz in {"srm-api", "auth"}:
            return "http{}://{}.dev.*.com".format("s" if is_https else "", biz)

    elif environment == RuntimeEnv.ENV_DEV:
        if biz in {"phone-cloud-api", "bid-info-api", 'leads-web-api', "auth", "srm-api", "in4"}:
            return "http{}://{}.dev.*.com".format("s" if is_https else "", biz)
        elif biz in {"phone-cloud.api", "research.api"}:
            return "http{}://{}.*.com".format("s" if is_https else "", biz)

    return "http{}://{}.{}.*.com".format("s" if is_https else "", biz, environment)


class _Services:
    _mysql = {
        RuntimeEnv.ENV_DEV: dict(host="*", port=3306, user="*",
                                 password="*")
    }

    _mysql_bidding = {
        RuntimeEnv.ENV_DEV: dict(host="*", port=3306, user="*",
                                 password="*"),
    }

    _mysql_phone = {
        RuntimeEnv.ENV_DEV: dict(host="*", port=3306, user="*",
                                 password="*", db="*")
    }

    _mysql_auth = {
        RuntimeEnv.ENV_TEST: dict(host="*", port=3306, user="*",
                                  password="*", db="*"),
        RuntimeEnv.ENV_DEV: dict(host="*", port=3306, user="*",
                                 password="*", db="*")
    }


    _oracle = {
        RuntimeEnv.ENV_TEST: dict(username="*", password="*", conn_str="*"),
        RuntimeEnv.ENV_DEV: dict(username="*", password="*", conn_str="*")
    }

    _postgressql = {
        # RuntimeEnv.ENV_DEV: dict(host="192.168.2.248", port=5432, user="root",
        #                          password="rcc123"),
        RuntimeEnv.ENV_TEST: dict(host="*", port="*", username="*",
                                  password="*", database="*"),
        RuntimeEnv.ENV_DEV: dict(host="*", port="*", username="*",
                                 password="*", database="*")
    }

    _redis = {
        RuntimeEnv.ENV_TEST: dict(host="*", port=6379, password=""),
        RuntimeEnv.ENV_DEV: dict(host="*", port=6379, password="")
    }

    @property
    def mysql(self):
        return self._mysql[environment]

    @property
    def mysql_bidding(self):
        return self._mysql_bidding[environment]

    @property
    def mysql_phone(self):
        return self._mysql_phone[RuntimeEnv.ENV_DEV]

    @property
    def mysql_auth(self):
        return self._mysql_auth[environment]

    @property
    def mysql_in2018(self):
        return self._mysql_in2018[environment]

    @property
    def oracle(self):
        return self._oracle[environment]


    @property
    def pg(self):
        return self._postgressql[environment]


    @property
    def redis(self):
        return self._redis[environment]

    @property
    def mega(self):
        return _easy_domain("*")

    @property
    def megaprod(self):
        return _easy_domain("*", is_https=True)

    @property
    def pangu_redis(self):
        """盘古（信息部）redis"""
        return self._redis_pangu[environment]

    @property
    def pangu(self):
        """盘古（信息部）测试环境域名"""
        return _easy_domain("*")

    @property
    def pangu_pro(self):
        """盘古（信息部）正式环境域名"""
        return _easy_domain("*")

    @property
    def reach(self):
        return _easy_domain("*")

    @property
    def srm(self):
        return _easy_domain("*")

    @property
    def phone(self):
        return _easy_domain("*")  # 电话系统测试线前缀

    @property
    def phonePro(self):
        return _easy_domain("*")  # 电话系统正式线前缀


services = _Services()
