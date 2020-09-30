from cakemail_openapi import ListApi


class List:
    def __init__(self, api):
        self.__api = ListApi(api)
        self.accept_policy = self.__api.accept_list_policy
        self.archive = self.__api.archive_list
        self.create = self.__api.create_list
        self.delete = self.__api.delete_list
        self.get = self.__api.get_list
        self.list = self.__api.list_lists
        self.update = self.__api.patch_list
        self.unarchive = self.__api.unarchive_list

    accept_policy: ListApi.accept_list_policy
    archive: ListApi.archive_list
    create: ListApi.create_list
    delete: ListApi.delete_list
    get: ListApi.get_list
    list: ListApi.list_lists
    update: ListApi.patch_list
    unarchive: ListApi.unarchive_list
