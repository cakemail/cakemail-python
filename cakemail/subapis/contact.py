from cakemail.wrapper import WrappedApi
from cakemail_openapi import ContactApi


class Contact(WrappedApi):
    """ Contact view of ContactApi """
    create: ContactApi.create_contact
    delete: ContactApi.delete_contact
    get: ContactApi.get_contact
    import_contacts: ContactApi.import_contacts
    list: ContactApi.list_contacts_of_list
    list_from_segment: ContactApi.list_contacts_of_segment
    update: ContactApi.patch_contact
    unsubscribe: ContactApi.unsubscribe_contact
