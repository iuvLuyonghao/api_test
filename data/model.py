# -*- coding: utf-8 -*-

from qav5.datastore import GroupedAttr, LinkedAttr, MetaData


class VendorData(MetaData):
    """vendor 测试数据"""
    pass


class VendorAppData(MetaData):
    """vendor_app对象"""
    vendor = LinkedAttr("vendor")


class MerchantData(MetaData):
    """商户模型"""
    stores = GroupedAttr("stores")
    account = LinkedAttr("account")
    super_admin = LinkedAttr("super_admin")
    group = LinkedAttr("group")
    organization = LinkedAttr("organization")


class StoreData(MetaData):
    """门店模型"""
    merchant = LinkedAttr("merchant")
    terminals = GroupedAttr("terminals")
    cashiers = GroupedAttr("cashiers")
    admins = GroupedAttr("admins")
    organization = LinkedAttr("organization")


class TerminalData(MetaData):
    """终端模型"""
    store = LinkedAttr("store")
    merchant = LinkedAttr("merchant")


class AccountData(MetaData):
    """帐号模型, 不直接映射upay_user.account对象，而是结合了account与xx_user的对象"""
    merchant = LinkedAttr("merchant")
    store = LinkedAttr("store")   # 建议取值为backstage.store_user.store_id
    osp = LinkedAttr("osp")
    organization = LinkedAttr("organization")


class TerminalActivationCode(MetaData):
    """终端激活码"""
    store = LinkedAttr("store")
    merchant = LinkedAttr("merchant")


class GroupData(MetaData):
    """集团商户模型"""
    account = LinkedAttr("account")
    merchants = GroupedAttr("merchants")


class MiniAPPData(MetaData):
    """微信小程序模型 - （暂时为礼品卡项目设计）"""
    group = LinkedAttr("group")


class OrganizationData(MetaData):
    """CRM组织模型"""
    parent = LinkedAttr("parent")
    children = GroupedAttr("children")


class CustomerData(MetaData):
    """顾客模型"""
    customer = LinkedAttr("customer")
