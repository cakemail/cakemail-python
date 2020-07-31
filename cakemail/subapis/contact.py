from cakemail.wrapper import WrappedApi
from cakemail_openapi import ContactApi


class Contact(WrappedApi):
    """ Contact view of ContactApi """
    create: ContactApi.create_contact
    delete: ContactApi.delete_contact
    get: ContactApi.get_contact
    imp: ContactApi.import_contacts
    patch: ContactApi.patch_contact
    unsubscribe: ContactApi.unsubscribe_contact
