from cakemail_openapi import UserApi


class User:
    def __init__(self, api):
        self.__api = UserApi(api)
        self.create = self.__api.create_user
        self.delete = self.__api.delete_user
        self.forgot_my_password = self.__api.forgot_my_password
        self.get_self = self.__api.get_self_user
        self.get = self.__api.get_user
        self.list = self.__api.list_users
        self.update = self.__api.patch_user
        self.reset_password_confirm = self.__api.reset_password_confirm
        self.reset_self_password = self.__api.reset_self_password
        self.reset_password = self.__api.reset_user_password
        self.suspend = self.__api.suspend_user
        self.unsuspend = self.__api.unsuspend_user

    create: UserApi.create_user
    delete: UserApi.delete_user
    forgot_my_password: UserApi.forgot_my_password
    get_self: UserApi.get_self_user
    get: UserApi.get_user
    list: UserApi.list_users
    update: UserApi.patch_user
    reset_password_confirm: UserApi.reset_password_confirm
    reset_self_password: UserApi.reset_self_password
    reset_password: UserApi.reset_user_password
    suspend: UserApi.suspend_user
    unsuspend: UserApi.unsuspend_user
