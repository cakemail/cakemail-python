from cakemail_openapi import SuppressedEmailApi


class SuppressedEmail:
    def __init__(self, api):
        self.__api = SuppressedEmailApi(api)
        self.create = self.__api.create_suppressed_email
        self.delete = self.__api.delete_suppressed_email
        self.list = self.__api.list_suppressed_emails

    create: SuppressedEmailApi.create_suppressed_email
    delete: SuppressedEmailApi.delete_suppressed_email
    list: SuppressedEmailApi.list_suppressed_emails
