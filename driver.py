# -*- coding: utf-8 -*-
import subprocess
import json
import os, re
import requests

os.chdir("/Users/qianhongyang/PycharmProjects/RCC/rcc_api_test")


def send_sms(path: str, phone_numbers: str):
    """
    @param path: "open_auth"
    @param phone_numbers: "phone_number1,phone_number2,phone_number3,..."
    @param messge: dict {"prject_name":["interface_name1,interface_name2,interface_name3",...]}
    """
    messge = execute(path)
    content = []
    for prject_names, interface_names in messge.items():
        content.append(("报错模块:%s" % prject_names))
        content.append(("报错接口:%s" % interface_names))
    print(content)
    if content:
        host = "*"
        data = {"message": "线上监控报错情况:%s" % content,
                "receivers": phone_numbers,
                "message_type": "yuntong_content"}
        re = requests.post(url=host, data=data)
        print(re.text)
    else:
        pass


def execute(path: str):
    """

    @param path: "open_auth"
    @return: dic
    """
    dic = {}
    modules = []
    interfases = []
    cmd = subprocess.Popen(
        ['venv/bin/python', "runsuite.py", '--suites', path, '-rf'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    results = cmd.stdout.readlines()
    for i in results:
        str_i = str(i, "utf-8")
        if str_i.startswith("FAILED"):
            modules.append((re.findall(".*/(.*)/.*", str_i))[0])
            interfases.append((re.findall(".*::test_(.*)\B-", str_i)[0]))

    for i, j in zip(modules, interfases):
        if i not in dic.keys():
            dic[i] = [j]
        else:
            dic[i].append(j)
    return dic


if __name__ == '__main__':
    send_sms("open_auth", "17317812862")
