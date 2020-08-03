from cakemail.wrapper import WrappedApi
from cakemail_openapi import CustomAttributeApi


class CustomAttribute(WrappedApi):
    """ CustomAttribute view of CustomAttributeApi """
    create: CustomAttributeApi.create_custom_attribute
    delete: CustomAttributeApi.delete_custom_attribute
    get: CustomAttributeApi.get_custom_attribute
    list: CustomAttributeApi.list_custom_attributes
