# coding = utf-8
from qav5 import log
from qav5.conn import PostGreSQLClient, OracleClient, MySQLConnectionMgr
from config import services
import re


class OperDataBase(object):
    def execute(self, query_sql, result_number, action):
        pass

    def close(self):
        pass


class PgDataBase(OperDataBase):

    def __init__(self, database_name):
        self.pg_client = PostGreSQLClient(host=services.pg['host'], port=services.pg["port"], database=database_name,
                                          user=services.pg['username'],
                                          password=services.pg['password'])

    def execute(self, query_sql, result_number=1, action="select"):
        """

        @param action:
        @param query_sql:
        @param result_number:
        @return:
        """
        if action == "select":
            results_list = self.pg_client.execute_query(query_sql)
            try:
                if result_number:
                    if result_number == 1 or result_number == "1" or result_number == "one":
                        return results_list[0]
                    elif result_number == "all":
                        return results_list
                    elif isinstance(result_number, int):
                        return results_list[:result_number]
                    elif re.findall('([0-9])\w*', result_number):
                        return results_list[:int(result_number)]
            except:
                return results_list
        elif action == "update":
            self.pg_client.execute_no_query(query_sql, bindvar=None)
            self.pg_client.conn.commit()

    def close(self):
        self.pg_client.disconnect()


class MysqlDataBase(OperDataBase):

    def __init__(self):
        mysql_mgr = MySQLConnectionMgr(autocommit=True, charset='utf8',
                                       **services.mysql)
        mysql_mgr.backend = mysql_mgr.BACKEND_OFFICIALMYSQL
        self.mysql_client = mysql_mgr.connection
        self.cursor = self.mysql_client.cursor()

    def execute(self, query_sql, result_number=1, action="select"):
        """

        @param action:
        @param query_sql:
        @param result_number:
        @return:
        """
        if action == "select":
            self.cursor.execute(query_sql)
            if result_number:
                if result_number == 1 or result_number == "1" or result_number == "one":
                    return self.cursor.fetchone()
                elif result_number == "all":
                    return self.cursor.fetchall()
                elif isinstance(result_number, int):
                    return self.cursor.fetchmany(result_number)
                elif str(result_number) != "1" or str(result_number) != "one" or str(
                        result_number) != "all":
                    return self.cursor.fetchmany(int(result_number))
        elif action == "update":
            self.cursor.execute(query_sql)
            self.mysql_client.commit()

    def close(self):
        self.cursor.close()
        self.mysql_client.close()


class OracleDataBase(OperDataBase):

    def __init__(self):
        self.oracle_client = OracleClient(services.oracle['username'], services.oracle['password'],
                                          services.oracle['conn_str'])

    def execute(self, query_sql, result_number=1, action="select"):
        """

        @param action:
        @param query_sql:
        @param result_number:
        @return:
        """
        results_list = self.oracle_client.execute_query(query_sql)
        if result_number:
            if result_number == 1 or result_number == "1" or result_number == "one":
                return results_list.fetchone()
            elif result_number == "all":
                return results_list.fetchall()
            elif isinstance(result_number, int):
                return results_list.fetchmany(result_number)
            elif str(result_number) != "1" or str(result_number) != "one" or str(
                    result_number) != "all":
                return results_list.fetchmany(int(result_number))

    def close(self):
        self.oracle_client.disconnect()
