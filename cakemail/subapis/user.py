from cakemail.wrapper import WrappedApi
from cakemail_openapi import UserApi


class User(WrappedApi):
    """ User view of UserApi """
    create: UserApi.create_user
    delete: UserApi.delete_user
    forgot_my_password: UserApi.forgot_my_password
    get_self: UserApi.get_self_user
    get: UserApi.get_user
    list: UserApi.list_users
    reset_password: UserApi.reset_user_password
    reset_password_confirm: UserApi.reset_password_confirm
    reset_self_password: UserApi.reset_self_password
    suspend: UserApi.suspend_user
    update: UserApi.patch_user
    unsuspend: UserApi.unsuspend_user
