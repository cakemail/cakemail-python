from cakemail_openapi import AccountApi


class Account:
    def __init__(self, api):
        self.__api = AccountApi(api)
        self.get_self = self.__api.get_self_account
        self.update_self = self.__api.patch_self_account

    get_self: AccountApi.get_self_account
    update_self: AccountApi.patch_self_account
