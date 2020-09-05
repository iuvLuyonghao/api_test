# coding=utf-8
from util import oper_database
import logging


class QureySqls:

    def __init__(self, client_name, database_name=None):

        name = client_name.capitalize()
        obj = name + "DataBase"
        if obj in dir(oper_database):
            client = getattr(oper_database, obj)
            if database_name:
                self.client = client(database_name)
            else:
                self.client = client()
        else:
            raise NameError(("选择数据库错误，不存在数据库名:%s") % obj)

    def select(self, **kwargs):
        """

        @param kwargs:
        { "qurey_char": String,  想查询的字段   不必填  默认*
          "tabel_name": String,  表名      必填
          "conditions": String, 查询条件   不必填 没有情况下不加条件查询
          "result_number": Int or String,  返回结果条数   不必填  默认返回一条
          "sql": String, 直接写sql执行  不必填 当有以上前三个参数时，不需要填写
        }
        EXAMPLE1:
            sql_dic = {"qurey_char": "person_user_id",
               "tabel_name": "person.person_subs",
               "conditions": "active = 0",
               "result_number": "all"
               }

        EXAMPLE2:
            sql_dic2 = {
                "qurey_char": "*",
                "tabel_name": "in2018_test.base_roles",
                "conditions": "",
                "result_number": "2"
            }

        EXAMPLE3:
            sql_dic3 = {
                "tabel_name": "LEADS_TYPES",
            }

        EXAMPLE4:
        sql_dic3 = {
                "sql": "select * from preson.users where active=0;",
            }
        @return: qurey_results
        """
        # 返回数量是多少
        if "result_number" not in kwargs.keys() or kwargs["result_number"] is None \
                or kwargs["result_number"] == "":
            result_number = 1
        else:
            result_number = kwargs["result_number"]
        # 如果是sql的话走这个逻辑
        if "sql" not in kwargs.keys() or kwargs["sql"] is None or kwargs["sql"] == "":
            tabel_name = kwargs["tabel_name"]
            if "qurey_char" not in kwargs.keys() or kwargs["qurey_char"] is None \
                    or kwargs["qurey_char"] == "":
                qurey_chars = "*"
            else:
                qurey_chars = kwargs["qurey_char"]

            if "conditions" not in kwargs.keys() or kwargs["conditions"] is None \
                    or kwargs["conditions"] == "":
                sql = "select %s from %s " % (qurey_chars, tabel_name)
            else:
                conditions = kwargs["conditions"]
                sql = "select %s from %s  where  %s " % (qurey_chars, tabel_name, conditions)

            results = self.client.execute(sql, result_number)
            logging.info(sql)
            return results
        else:
            sql = kwargs["sql"]
            results = self.client.execute(sql, result_number)
            logging.info(sql)
            return results

    def updata(self, **kwargs):
        # 如果是sql的话走这个逻辑
        if "sql" not in kwargs.keys() or kwargs["sql"] is None or kwargs["sql"] == "":
            tabel_name = kwargs["tabel_name"]
            if "set_values" not in kwargs.keys() or kwargs["set_values"] is None \
                    or kwargs["set_values"] == "":
                raise Exception("update的值不能为空")
            else:
                set_values = kwargs["set_values"]

            if "conditions" not in kwargs.keys() or kwargs["conditions"] is None \
                    or kwargs["conditions"] == "":
                sql = "upate %s set %s  " % (tabel_name, set_values)
            else:
                conditions = kwargs["conditions"]
                sql = "upate %s set %s where %s" % (tabel_name, set_values, conditions)

            results = self.client.execute(sql, result_number=None, action="update")
            logging.info(sql)
            return results
        else:
            sql = kwargs["sql"]
            results = self.client.execute(sql, result_number=None, action="update")
            logging.info(sql)
            return results

    def insert(self):
        pass
