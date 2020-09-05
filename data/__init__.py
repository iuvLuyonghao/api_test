# -*- coding: utf-8 -*-

from .loader import DataCenter, DataHelper
from .loader import load_data, load_local_data, load_framework_data, load_package_data
from .model import *

DataHelper.update_obj_map({
    "merchant": MerchantData,
    "store": StoreData,
    "terminal": TerminalData,
    "account": AccountData,
    "activation code": TerminalActivationCode,
    "vendor": VendorData,
    "vendor_app": VendorAppData,
    "group": GroupData,
    "mini_app": MiniAPPData,
    "organization": OrganizationData,
    "customer": CustomerData
})

load_framework_data()
