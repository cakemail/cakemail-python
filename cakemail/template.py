from cakemail_openapi import TemplateApi


class Template:
    def __init__(self, api):
        self.__api = TemplateApi(api)
        self.create = self.__api.create_template
        self.delete = self.__api.delete_template
        self.get = self.__api.get_template
        self.list = self.__api.list_templates
        self.update = self.__api.patch_template

    create: TemplateApi.create_template
    delete: TemplateApi.delete_template
    get: TemplateApi.get_template
    list: TemplateApi.list_templates
    update: TemplateApi.patch_template
