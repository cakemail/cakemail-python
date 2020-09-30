from cakemail_openapi import CustomAttributeApi


class CustomAttribute:
    def __init__(self, api):
        self.__api = CustomAttributeApi(api)
        self.create = self.__api.create_custom_attribute
        self.delete = self.__api.delete_custom_attribute
        self.get = self.__api.get_custom_attribute
        self.list = self.__api.list_custom_attributes

    create: CustomAttributeApi.create_custom_attribute
    delete: CustomAttributeApi.delete_custom_attribute
    get: CustomAttributeApi.get_custom_attribute
    list: CustomAttributeApi.list_custom_attributes
