from cakemail_openapi import FormApi


class Form:
    def __init__(self, api):
        self.__api = FormApi(api)
        self.create = self.__api.create_form
        self.delete = self.__api.delete_form
        self.get = self.__api.get_form
        self.list = self.__api.list_forms
        self.update = self.__api.patch_form

    create: FormApi.create_form
    delete: FormApi.delete_form
    get: FormApi.get_form
    list: FormApi.list_forms
    update: FormApi.patch_form
