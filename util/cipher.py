# -*- coding: utf-8 -*-

import json
import subprocess
from os.path import abspath, join
from const import AES

file1 = abspath(join(__file__, "../rcc_decode.rb"))
file2 = abspath(join(__file__, "../rcc_encode.rb"))


class AESCipher:
    @staticmethod
    def decrypt(data, key, iv):
        cmd = subprocess.run(
            ['ruby', file1, data, key, iv],
            stdout=subprocess.PIPE)
        # 传递subprocess.PIPE捕获命令执行结果的正常输出
        result = json.loads(cmd.stdout.decode('utf-8'))  # 以utf-8编码进行解码
        return result

    @staticmethod
    def encrypt(aes_key, iv):
        cmd = subprocess.Popen(
            ['ruby', file2, aes_key, iv],
            stdout=subprocess.PIPE)
        results = cmd.stdout.readlines()
        return results



