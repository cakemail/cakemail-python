from cakemail_openapi import ContactApi


class Contact:
    def __init__(self, api):
        self.__api = ContactApi(api)
        self.create = self.__api.create_contact
        self.delete = self.__api.delete_contact
        self.get = self.__api.get_contact
        self.import_contacts = self.__api.import_contacts
        self.list = self.__api.list_contacts_of_list
        self.list_from_segments = self.__api.list_contacts_of_segment
        self.update = self.__api.patch_contact
        self.unsubscribe = self.__api.unsubscribe_contact

    create: ContactApi.create_contact
    delete: ContactApi.delete_contact
    get: ContactApi.get_contact
    import_contacts: ContactApi.import_contacts
    list: ContactApi.list_contacts_of_list
    list_from_segments: ContactApi.list_contacts_of_segment
    update: ContactApi.patch_contact
    unsubscribe: ContactApi.unsubscribe_contact
