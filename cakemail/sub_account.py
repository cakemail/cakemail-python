from cakemail_openapi import SubAccountApi


class SubAccount:
    def __init__(self, api):
        self.__api = SubAccountApi(api)
        self.create = self.__api.create_account
        self.delete = self.__api.delete_account
        self.get = self.__api.get_account
        self.list = self.__api.list_accounts
        self.update = self.__api.patch_account
        self.suspend = self.__api.suspend_account
        self.unsuspend = self.__api.unsuspend_account

    create: SubAccountApi.create_account
    delete: SubAccountApi.delete_account
    get: SubAccountApi.get_account
    list: SubAccountApi.list_accounts
    update: SubAccountApi.patch_account
    suspend: SubAccountApi.suspend_account
    unsuspend: SubAccountApi.unsuspend_account
