from cakemail.wrapper import WrappedApi
from cakemail_openapi import SubAccountApi


class SubAccount(WrappedApi):
    """ SubAccount view of SubAccountApi """
    create: SubAccountApi.create_account
    delete: SubAccountApi.delete_account
    get: SubAccountApi.get_account
    list: SubAccountApi.list_accounts
    update: SubAccountApi.patch_account
    suspend: SubAccountApi.suspend_account
    unsuspend: SubAccountApi.unsuspend_account
