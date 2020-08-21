from cakemail.wrapper import WrappedApi
from cakemail_openapi import AccountApi


class Account(WrappedApi):
    """ Account view of AccountApi """
    get_self: AccountApi.get_self_account
    update_self: AccountApi.patch_self_account
