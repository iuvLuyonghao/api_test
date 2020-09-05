#-*- coding:utf-8 -*-
'''
注入扫描
'''
from config import services
from util.scan.core.Spider import SpiderMain
def main():
    urllist=[services.mega,services.auth,services.pangu,services.dialapiprod,services.feedback,services.httpgrpc,services.logcloud2,services.np,services.panda,services.skyrimprod]
    # root = "https://yakeshi.baixing.com/"
    threadNum = 50
    for url in urllist:
        w8 = SpiderMain(url, threadNum)
        w8.craw()

if __name__ == "__main__":
    main()
