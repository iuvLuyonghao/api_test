#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

class PasswordEncryption:
    def __init__(self,password):
        self.password=password

    def md5_password(self):
        m=hashlib.md5()
        b=self.password.encode(encoding='utf-8')
        m.update(b)
        password=m.hexdigest()
        return password

    def sha256_password(self):
        s=hashlib.sha256()
        b=self.password.encode(encoding='utf-8')
        s.update(b)
        password=s.hexdigest()
        return password

if __name__=='__main__':
    print(PasswordEncryption('it_test123').md5_password())
    print(PasswordEncryption('it_test123').sha256_password())
