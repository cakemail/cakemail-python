from cakemail.wrapper import WrappedApi
from cakemail_openapi import FormApi


class Form(WrappedApi):
    """ Form view of FormApi """
    create: FormApi.create_form
    delete: FormApi.delete_form
    get: FormApi.get_form
    list: FormApi.list_forms
    patch: FormApi.patch_form
