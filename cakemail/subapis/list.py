from cakemail.wrapper import WrappedApi
from cakemail_openapi import ListApi


class List(WrappedApi):
    """ List view of ListApi """
    archive: ListApi.archive_list
    create: ListApi.create_list
    delete: ListApi.delete_list
    get: ListApi.get_list
    list: ListApi.list_lists
    update: ListApi.patch_list
    unarchive: ListApi.unarchive_list
