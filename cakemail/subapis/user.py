from cakemail.wrapper import WrappedApi
from cakemail_openapi import UserApi


class User(WrappedApi):
    """ User view of UserApi """
    create: UserApi.create_user
    delete: UserApi.delete_user
    get_self: UserApi.get_self_user
    get: UserApi.get_user
    list: UserApi.list_users
    update: UserApi.patch_user
    suspend: UserApi.suspend_user
    unsuspend: UserApi.unsuspend_user
