from cakemail_openapi import SenderApi


class Sender:
    def __init__(self, api):
        self.__api = SenderApi(api)
        self.confirm = self.__api.confirm_sender
        self.create = self.__api.create_sender
        self.delete = self.__api.delete_sender
        self.get = self.__api.get_sender
        self.list = self.__api.list_senders
        self.update = self.__api.patch_sender
        self.resend_confirmation = self.__api.resend_confirmation_email

    confirm: SenderApi.confirm_sender
    create: SenderApi.create_sender
    delete: SenderApi.delete_sender
    get: SenderApi.get_sender
    list: SenderApi.list_senders
    update: SenderApi.patch_sender
    resend_confirmation: SenderApi.resend_confirmation_email
